from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print('got',request.session.get('customer'),' in middleware')
        returnurl = request.META['PATH_INFO']
        if not request.session.get('customer'):
            return redirect(f'login.html?return_url={returnurl}')

        response = get_response(request)
        return response

    return middleware