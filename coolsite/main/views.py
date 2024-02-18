from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm

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

def basketAndBuy(request):
    return render(request, "main/basket.html")

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

