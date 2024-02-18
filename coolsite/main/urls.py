from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('my-account', views.myAccount, name='myAccount'),
    path('auto', views.userLogin, name='userLogin'),
    path('about', views.aboutUS),
    path('profile', views.profile),
    path('logout', views.logout_user),
    path('help-and-questions', views.helpAndQuestions),
    path('basket', views.basketAndBuy),
    path('search/', views.search, name='search'),
    path('reviews', views.reviewsAndOpinions),
    path('privacy-policy', views.privacyPolicy),
    path('user-agreement', views.userAgreement),
    path('product/<slug:Product_slug>/', views.show_post, name ='product'),
    path('category/<slug:category_slug>/', views.show_category, name='category'),
]