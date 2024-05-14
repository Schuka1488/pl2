from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Account(models.Model):
    loginAccount = models.CharField('Логин', max_length=60, default="") # Ключевой параметр loginAccount
    passwordAccount = models.CharField('Пароль', max_length=60, default="")
    roleTitleAccount = models.CharField('Название роли', max_length=50, default="")
    idNameInGameAccount = models.CharField('ID игрока (ник в игре)', max_length=100, default="")
    emailBuyerAccount = models.CharField('Email игрока', max_length=150, default="", blank=True)
    onlineStatusAccount = models.BooleanField('Статус нахождения в сети', default=True)
    authorizationStatusAccount = models.BooleanField('Статус авторизации пользователя на сайте', default=False)
    serverPlayerAccount = models.CharField('Игровой сервер', max_length=50, default="", blank=True)
    idNumberOrder = models.ForeignKey('Order', on_delete=models.PROTECT, null=True)
    objectsAccount = models.Manager()

    def __str__(self):
        return self.loginAccount

    class Meta:
        verbose_name = 'Аккаунты'
        verbose_name_plural = 'Аккаунты'


class Product(models.Model):
    nameProduct = models.CharField('Название продукта', max_length=150, default="")
    photoProduct = models.ImageField('Фото товара', upload_to="photos/photoProduct/nameProduct", default="", blank=True)
    priceOnCronOrNotProduct = models.BooleanField('В кронах ли цена?', default=True)
    priceOnCronProduct = models.IntegerField('Цена в игровой валюте (кроны или гемы)', default=0, blank=True)
    priceOnMoneyProduct = models.IntegerField('Цена в реальной валюте', default=0)
    descriptionProduct = models.CharField('Описание товара', max_length=200, default="", blank=True)
    statusViewsOnSiteProduct = models.BooleanField('Статус отображения на сайте', default=True)
    promotionStatusProduct = models.BooleanField('Статус акции у товара', default=False)
    idCategory = models.ForeignKey('Category', on_delete=models.PROTECT)
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)
    objectsProduct = models.Manager()

    def __str__(self):
        return self.nameProduct

    def get_absolute_url(self):
        return reverse('product', kwargs={'Product_slug': self.slug})

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    numberOrder = models.IntegerField('Номер заказа', default=0) # Ключевой параметр numberOrder
    sellProductOrder = models.CharField('Проданные товары', max_length=250, default="")
    statusSellOrder = models.BooleanField('Статус выполнения заказа', default=False)
    dateSellProductOrder = models.DateTimeField('Дата выполнения заказа', max_length=75, auto_now_add=True)
    loginOrder = models.CharField('Логин заказчика', max_length=60, default="")
    idPlayerOrder = models.CharField('ID игрока (ник в игре)', max_length=100, default="")
    emailBuyerOrder = models.CharField('Email игрока', max_length=150, default="", blank=True)
    paymentGatewayOrder = models.CharField('Выбранный платежный шлюз', max_length=100, default="")
    countSameTypeOrder = models.IntegerField('Количество проданных товаров одного типа', default=0, blank=True)
    countDifferentTypeOrder = models.IntegerField('Количество проданных товаров разного типа', default=0, blank=True)
    playServerOrder = models.CharField('Игровой сервер', max_length=50, default="")
    orderPriceRememberOrder = models.IntegerField('Цена заказа', default=0)
    statusReadyAgreementPurchaseOfGood = models.BooleanField('Статус подтверждения ПС', default=False)
    objectsOrder = models.Manager()

    def __str__(self):
        return self.numberOrder

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'


class Category(models.Model):
    nameCategory = models.CharField('Название категории', max_length=200, default="", db_index=True) # Ключевой параметр nameCategory
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)
    objectsCategory = models.Manager()
    def __str__(self):
        return self.nameCategory

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'



class Review(models.Model):
    starReview = models.ForeignKey('Star', default=0, on_delete=models.PROTECT, verbose_name='Оценка от 1 до 5')
    textReview = models.CharField('Ваш отзыв', max_length=500, default="", blank=True)
    nameReview = models.CharField('Ваше имя', max_length=50, default="")
    emailBuyerAccount = models.CharField('Ваш email', max_length=150, default="")
    answerReview = models.CharField('Ответ на отзыв', max_length=500, default="", blank=True)
    statusViewsOnSiteReview = models.BooleanField('Статус отображения на сайте', default=True)
    dateReview = models.DateTimeField('Дата написания отзыва', max_length=75, auto_now_add=True)
    objectsReview = models.Manager()
    def __str__(self):
        return str(self.starReview)

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'
        ordering = ['-dateReview']


class Chat(models.Model):
    loginAccountChat = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    dateWriteChat = models.DateTimeField('Дата написания сообщения', max_length=75, auto_now_add=True)
    textReview = models.CharField('Текст сообщения', max_length=500, default="")
    statusViewsOnSiteChat = models.BooleanField('Статус отображения на сайте', default=True)
    objectsChat = models.Manager()

    def __str__(self):
        return self.loginAccountChat

    class Meta:
        verbose_name = 'Сообщения в чате'
        verbose_name_plural = 'Сообщения в чате'

class Star(models.Model):
    countStar = models.IntegerField('Количество звезд у отзыва', default=0)
    objectsStar = models.Manager()
    def __str__(self):
        return str(self.countStar)

    class Meta:
        verbose_name = 'Количество звезд у отзыва'
        verbose_name_plural = 'Количество звезд у отзыва'

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)  # Ссылка на модель Product
    purchased = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objectsCartItem = models.Manager()

    def __str__(self):
        return f'{self.product.nameProduct}'

    def get_product_name(self):
        return self.product.nameProduct

    def get_product_photo(self):
        return self.product.photoProduct.url

    def get_product_price_cron_or_not(self):
        return self.product.priceOnCronOrNotProduct

    def get_product_price(self):
        if self.product.priceOnCronOrNotProduct:
            return self.product.priceOnCronProduct
        else:
            return self.product.priceOnMoneyProduct

    def get_product_description(self):
        return self.product.descriptionProduct


