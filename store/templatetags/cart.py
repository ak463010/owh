from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product_id, cart):
    for i in cart:
        if int(i) == product_id:
            return True
    return False


@register.filter(name='quantity')
def quantity(product_id, cart):
    return cart.get(str(product_id))


@register.filter(name='multiply')
def multiply(a, b):
    return a * b


@register.filter(name='total_price')
def total_price(product, cart):
    price = product.price
    q = quantity(product.id, cart)
    return int(price) * q


@register.filter(name='all_products_price')
def all_products_price(products, cart):
    total = 0
    for product in products:
        price = int(product.price)
        q = quantity(product.id, cart)
        total += q * price
    return total
