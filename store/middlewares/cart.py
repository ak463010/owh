def cart_create(get_response):

    def response(request):
        if not request.session.get('cart'):
            request.session['cart'] = {}
        return get_response(request)
    return response
