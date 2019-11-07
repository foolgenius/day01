from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class AuthMiddleware(MiddlewareMixin):
    API_WHITE_LIST = [
       '/userapp/get_vcode/',
        '/userapp/submit_vcode/',
    ]
    #
    def process_request(self, request):
        if request.path in AuthMiddleware.API_WHITE_LIST:
            return

        uid = request.session.get('uid')
        if not uid:
            return JsonResponse({'code':1002, 'data':'None'})
