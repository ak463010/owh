from django.shortcuts import redirect, render
from django.views import View
from store.models.oder import Oder


class OderView(View):
    def get(self, request):
        customer_id = request.session.get('customer')
        oders = Oder.get_all_product_by_customer_id(customer_id)
        return render(request, 'store/oders.html', {'oders': oders})
