from store.models.customer import Customer
from django.views import View
from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.oder import Oder


class Cart(View):
    def get(self, request):
        cart = request.session.get('cart')
        product_ids = cart.keys()
        products = Product.get_product_by_ids(product_ids)
        return render(request, 'store/cart.html', {'products': products})

    def post(self, request):
        customer = request.session.get('customer')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        cart = request.session.get('cart')
        products = Product.get_product_by_ids(cart.keys())

        for product in products:
            oder = Oder(
                product=product,
                customer=Customer(customer),
                quantity=cart.get(str(product.id)),
                price=product.price,
                address=address,
                phone=phone,
            )
            oder.place_oder()
        request.session['cart'] = {}
        return redirect('oders')
