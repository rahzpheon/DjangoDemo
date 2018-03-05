from django.http import HttpResponse

class My_middleware(object):

    # 实例:根据用户ip,禁止用户访问
    def process_request(self, request):
        ban_ip = ['192.168.109.1',]
        user_ip = request.META['REMOTE_ADDR']

        if user_ip in ban_ip:
            return HttpResponse("<h1>您已被禁止访问.</h1>")

    def __init__(self):
        print('----init----')

    # 后覆盖前
    def process_request(self, request):
        print('----request----')

    def process_view(self,request, *args, **kwargs):
        print('----view----')

    def process_response(self, request, response):
        print('----response----')
        return response

    def process_exception(self, request, exception):
        print(exception)
