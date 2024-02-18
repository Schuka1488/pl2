from django.contrib import admin

from .models import *


class AccountAdmin(admin.ModelAdmin):
    list_display = ('loginAccount',  'idNameInGameAccount', 'emailBuyerAccount', 'roleTitleAccount', 'onlineStatusAccount')
    search_fields = ('loginAccount', )
    list_filter = ('roleTitleAccount', 'onlineStatusAccount')

admin.site.register(Account, AccountAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('nameProduct', 'priceOnCronOrNotProduct', 'statusViewsOnSiteProduct', 'promotionStatusProduct')
    search_fields = ('nameProduct', )
    list_filter = ('priceOnCronOrNotProduct', 'statusViewsOnSiteProduct', 'promotionStatusProduct')

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('statusSellOrder', 'dateSellProductOrder', 'loginOrder', 'orderPriceRememberOrder')
    search_fields = ('statusSellOrder', 'dateSellProductOrder', 'loginOrder')
    list_filter = ('statusSellOrder', 'dateSellProductOrder')

admin.site.register(Order, OrderAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'nameCategory')
    search_fields = ('nameCategory', )

admin.site.register(Category, CategoryAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('starReview', 'nameReview', 'statusViewsOnSiteReview', 'dateReview')
    search_fields = ('starReview', 'nameReview', 'statusViewsOnSiteReview')
    list_filter = ('statusViewsOnSiteReview', 'dateReview')

admin.site.register(Review, ReviewAdmin)

class ChatAdmin(admin.ModelAdmin):
    list_display = ('loginAccountChat', 'dateWriteChat', 'statusViewsOnSiteChat')
    search_fields = ('loginAccountChat', 'statusViewsOnSiteChat')
    list_filter = ('dateWriteChat', 'statusViewsOnSiteChat')


admin.site.register(Chat, ChatAdmin)


admin.site.register(Star)

admin.site.site_title = 'Elder Shop Administration'
admin.site.site_header = 'Elder Shop Administration'
