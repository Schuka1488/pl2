from django import template
from main.models import *


register = template.Library()


@register.inclusion_tag('main/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objectsCategory.all()
    else:
        cats = Category.objectsCategory.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}

@register.inclusion_tag('main/list_product.html')
def show_product(idCategory_id=None):
    if idCategory_id is None:
        products = Product.objectsProduct.all()
    else:
        products = Product.objectsProduct.filter(idCategory_id=idCategory_id)
    return {'products': products, 'cat_selected': idCategory_id}
