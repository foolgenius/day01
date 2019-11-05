# from django.http import JsonResponse
# from django.utils.deprecation import MiddlewareMixin
#
# class AuthMiddleware(MiddlewareMixin):
#     API_WHITE_LIST = [
#        '/get_vcode/',
#         '/submit_vcode',
#     ]
#     #
#     def process_request(self, request):
#         if request.path in AuthMiddleware.API_WHITE_LIST:
#             return
#
#         if 'uid' in request.seesion:
#             uid = request.seesion.get('uid')
#             if not uid:
#                 return JsonResponse({'code':1002, 'data':'None'})
