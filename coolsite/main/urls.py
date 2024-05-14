from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('my-account', views.myAccount, name='myAccount'),
    path('auto', views.userLogin, name='userLogin'),
    path('about', views.aboutUS),
    path('profile/', views.profile, name='profile'),
    path('logout', views.logout_user),
    path('help-and-questions', views.helpAndQuestions),
    path('search/', views.search, name='search'),
    path('reviews', views.reviewsAndOpinions),
    path('privacy-policy', views.privacyPolicy),
    path('user-agreement', views.userAgreement),
    path('product/<slug:Product_slug>/', views.show_post, name ='product'),
    path('category/<slug:category_slug>/', views.show_category, name='category'),
    path('change-password/', views.change_password, name='change_password'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('basket', views.basket, name='basket'),
    path('payment/process/', views.payment_process, name='payment_process'),
]
