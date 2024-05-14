from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from .models import CartItem
from django.conf import settings
import stripe
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *
def index(request):
    posts = Product.objectsProduct.all()
    return render(request, "main/index.html", {'posts': posts, 'cat_selected': 3,})


def helpAndQuestions(request):
    return render(request, "main/help-and-questions.html")

def aboutUS(request):
    return render(request, "main/about.html")

def profile(request):
    return render(request, "main/profile.html")

def searchOrCategories(request):
    return render(request, "main/search.html")

def reviewsAndOpinions(request):
    rev = Review.objectsReview.all()
    paginator = Paginator(rev,4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = AddReviews(request.POST)
        if form.is_valid():
            try:
                form.save()
                form = AddReviews()
                return redirect('/reviews')
            except:
                form.add_error(None, 'Ошибка добавления отзыва')
    else:
        form = AddReviews()
    context = {
        'form': form,
        'rev': rev,
        'page_obj': page_obj,
    }
    return render(request, "main/reviews.html", context=context)

def privacyPolicy(request):
    return render(request, "main/privacy-policy.html")

def userAgreement(request):
    return render(request, "main/user-agreement.html")

def show_post(request, Product_slug):
    post = get_object_or_404(Product, slug=Product_slug)

    context = {
        'post': post,
        'cat_selected': post.idCategory_id,
    }
    return render(request,'main/post.html', context=context)

def show_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objectsProduct.filter(idCategory=category)

    return render(request, 'main/index.html', {'products': products, 'cat_selected': category})

def myAccount(request):
    if request.method == 'POST':
        formMyAccount = UserRegistrationForm(request.POST)
        if formMyAccount.is_valid():
            formMyAccount.save()
            username = formMyAccount.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/auto')  # Перенаправление на страницу входа после успешной регистрации
    else:
        formMyAccount = UserRegistrationForm()
    return render(request, "main/my-account.html", {'formMyAccount': formMyAccount})

def userLogin(request):
    if request.method == 'POST':
        formMyAccountAuto = UserLoginForm(data=request.POST)
        if formMyAccountAuto.is_valid():
            username = formMyAccountAuto.cleaned_data.get('username')
            password = formMyAccountAuto.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/profile')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        formMyAccountAuto = UserLoginForm()
    return render(request, 'main/auto.html', {'formMyAccountAuto': formMyAccountAuto})

def logout_user(request):
    logout(request)
    return redirect('/auto')

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Product.objectsProduct.filter(nameProduct__icontains=query)
    return render(request, "main/index.html", {'results': results, 'query': query})

def change_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        if new_password:
            user = request.user
            user.set_password(new_password)
            user.save()
            # Обновляем сессию пользователя после изменения пароля
            request.session.cycle_key()
            # Вход пользователя после изменения пароля
            # Это может быть полезно, если вы хотите, чтобы пользователь оставался в системе после изменения пароля
            # Пример:
            # login(request, user)
            return redirect('/auto')  # Перенаправляем на страницу профиля после успешного изменения пароля
    return render(request, 'main/profile.html')

@login_required  # Декоратор, который требует авторизации пользователя
def add_to_cart(request, product_id):
    if request.method == 'POST':
        # Получаем экземпляр объекта Product по его идентификатору
        product = Product.objectsProduct.get(pk=product_id)

        # Создаем экземпляр CartItem и сохраняем его в базе данных
        cart_item = CartItem(user=request.user, product=product)  # Передаем объект Product, а не поля nameProduct и priceOnMoneyProduct
        cart_item.save()

        return redirect('/basket')  # Перенаправляем пользователя на страницу корзины
    else:
        return redirect('/home')  # Если это не POST-запрос, перенаправляем пользователя на главную страницу


def basket(request):
    cart_items = CartItem.objectsCartItem.filter(user=request.user, purchased=False)
    return render(request, 'main/basket.html', {'cart_items': cart_items})

stripe.api_key = settings.STRIPE_SECRET_KEY

@require_POST
@csrf_exempt
def payment_process(request):
    # Получаем все товары в корзине пользователя
    cart_items = CartItem.objectsCartItem.filter(user=request.user, purchased=False)

    # Если есть товары в корзине
    if cart_items.exists():
        try:
            # Создаем сессию платежа через Stripe API
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.product.nameProduct,
                        },
                        'unit_amount': item.get_product_price(),  # Стоимость товара
                    },
                    'quantity': 1,
                } for item in cart_items],
                mode='payment',
                success_url=request.build_absolute_uri(reverse('profile')),  # Ссылка на страницу успешной оплаты
                cancel_url=request.build_absolute_uri(reverse('basket')),   # Ссылка на страницу отмены оплаты
            )

            # Отмечаем все товары в корзине как оплаченные
            cart_items.update(purchased=True)

            # Перенаправляем пользователя на страницу оплаты Stripe
            return redirect(session.url)
        except stripe.error.InvalidRequestError as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Ваша корзина пуста'})


