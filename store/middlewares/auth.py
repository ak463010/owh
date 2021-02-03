from django.shortcuts import redirect


def auth_middleware(get_respone):

    def middleware(request):
        if not request.session.get('customer'):
            return_url = request.META.get('PATH_INFO')

            return redirect(f'/login?return_url={ return_url }')
        return get_respone(request)
    return middleware
