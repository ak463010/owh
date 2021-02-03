from django.http.response import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from store.forms.login import Login_form
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        login_form = Login_form()
        return render(request, 'store/login.html', {'login': login_form, 'active': 'active'})

    def post(self, request):
        print(Login.return_url)
        error_message = None
        login = Login_form(request.POST)
        if login.is_valid():
            email = login.cleaned_data['email']
            password = login.cleaned_data['password']
            customer = Customer.get_customer_by_email(email)
            if customer:
                if check_password(password, customer.password):
                    request.session['customer'] = customer.id
                    if Login.return_url:
                        return redirect(Login.return_url)
                    else:
                        Login.return_url = None
                        return redirect('store')
                else:
                    error_message = 'You are enter wrong password !'
            else:
                error_message = 'Email does not exist !'
        return render(request, 'store/login.html', {'login': login, 'error': error_message, 'active': 'active'})


def logout(request):
    request.session.clear()
    return redirect('store')
