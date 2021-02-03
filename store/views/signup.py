from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from store.forms.signup import Signup_form
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):

    def get(self, request):
        form = Signup_form()
        return render(request, 'store/signup.html', {'signup': form})

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        error_message = None
        form = Signup_form(request.POST)
        if form.is_valid():
            customer = Customer(
                name=name,
                email=email,
                phone=phone,
                password=password,
            )
            if customer.is_exist():
                error_message = 'Email address Already Exist !'
            else:
                customer.password = make_password(password)
                Customer.register_user(customer)
                return redirect('store')

        return render(request, 'store/signup.html', {'signup': form, 'error': error_message})
