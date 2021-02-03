from django.shortcuts import redirect, render
from django.views import View
from store.models.product import Product
from store.models.category import Category


class Index(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        category_id = request.GET.get('category_id')
        products = None
        categories = Category.get_all_categories()
        if category_id:
            products = Product.get_product_by_category_id(category_id)
        else:
            products = Product.get_all_product()
        data = {}
        data['products'] = products
        data['categories'] = categories
        return render(request, 'store/index.html', data)

    def post(self, request):
        product = request.POST.get('product')
        add = request.POST.get('add')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if int(cart.get(product)) <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = cart.get(product) - 1
                else:
                    cart[product] = cart.get(product) + 1
            else:
                cart[product] = 1
        else:
            cart = request.session['cart'] = {}
            cart[product] = 1

        request.session['cart'] = cart
        return redirect('store')
