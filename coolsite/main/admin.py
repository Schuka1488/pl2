from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('nameProduct', 'priceOnCronOrNotProduct', 'statusViewsOnSiteProduct', 'promotionStatusProduct')
    search_fields = ('nameProduct', )
    list_filter = ('priceOnCronOrNotProduct', 'statusViewsOnSiteProduct', 'promotionStatusProduct')

admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'nameCategory')
    search_fields = ('nameCategory', )

admin.site.register(Category, CategoryAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('starReview', 'nameReview', 'statusViewsOnSiteReview', 'dateReview')
    search_fields = ('starReview', 'nameReview', 'statusViewsOnSiteReview')
    list_filter = ('statusViewsOnSiteReview', 'dateReview')

admin.site.register(Review, ReviewAdmin)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'purchased', 'product')
    search_fields = ('user', 'product')

admin.site.register(CartItem, CartItemAdmin)


admin.site.site_title = 'Elder Shop Administration'
admin.site.site_header = 'Elder Shop Administration'
