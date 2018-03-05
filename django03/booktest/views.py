from django.shortcuts import render
from booktest.models import Areas
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.shortcuts import redirect
# from django.views.decorators.csrf import csrf_exempt,csrf_protect



# Create your views here.
# 自关联表练习

def areas(request):

    # 获取广州市的父级地区 出错：关联查询未执行,建议自关联时使用另一种方式关联查询
    # af = Areas.objects.filter(areas__atitle='广州市')
    # 获取广州市的子级地区
    # ason = Areas.objects.filter(aParent__atitle__exact='广州市')

    # 获取广州市的地区对象
    a = Areas.objects.get(atitle='广州市')
    # 获取广州市的父级地区
    af = a.aParent
    # 获取广州市的子级地区
    ason = a.areas_set.all()
    return render(request, 'booktest/areas.html',{'area':a, 'father':af, 'son':ason})

# 首页
def index(request):
    return render(request, 'index.html', {})

# 登陆校验练习:通过HttpRequest对象获取表单提交信息
# @csrf_exempt
def login(request):

    # 判断用户名是否存在
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
        checked = 'checked'
    else:
        username = ''
        checked = ''

    return render(request, 'login/login.html', {'username':username,'checked':checked})

# 登陆校验
def login_check(request):

    # 用get方法获取表单提交的用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 是否勾选记住用户名
    checked = request.POST.get('remember')
    if checked is not None:
        request.COOKIES['username']:username

    # 验证：username=abc,password=123
    # 根据结果 重定向 至相应页面
    if username=='abc' and password=='123':
        # return HttpResponseRedirect('/index')
        return redirect('/index')
    else:
        # return HttpResponseRedirect('/login')
        return redirect('/failed')

# 登陆校验:ajax请求版本
def login_ajax(request):
    return render(request, 'login/login_ajax.html')

# 登陆校验:ajax请求版本
# 从前端ajax请求发来的json字典中获取数据
# 前端在没有用表单的情况下,手动装入字典,并以post方式发出ajax请求
# 所以此处的后端仍然能用POST获得值
# 注意:前端的ajax请求有简化写法$.get()与$.post()
def login_ajax_check(request):

    username = request.POST.get('username')
    password = request.POST.get('password')

    if username == 'abc' and password == '123':
        return JsonResponse({'b':1})
    else:
        return JsonResponse({'b':0})

# cookie设置:通过HttpResponse对象.set_cookie('键','值')设置
# 可用max_age设置存活时间(秒),默认浏览器关闭消亡
# cookie消息在Http Response 的响应头 Set-Cookie
def cookie_set(request):
    res = HttpResponse('cookie设置测试')
    res.charset='gbk'
    res.set_cookie('username', '小明')
    return res
# 获取cookie:通过HttpRequest对象的属性COOKIES(Python字典)获取
# 浏览器会在访问某域名时把其下的所有cookie发至服务器
# cookie信息在Http Request的请求头 Cookie
def cookie_get(request):
    res = HttpResponse('cookie获取测试')
    res.write('<h1>'+ request.COOKIES['username'] +'</h1>')
    return res


def failed(request):
    return render(request, 'failed.html')

# 登陆2:完美版,记住用户名勾选框完美实现
# 登陆校验
def login_check2(request):

    # 用get方法获取表单提交的用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username == 'abc' and password == '123':
        response = redirect('/index')

        # 是否勾选记住用户名
        checked = request.POST.get('remember')
        if checked is not None:  # 勾选框的值: on none
            response.set_cookie('username', username)
        else:
            response.delete_cookie('username')
        return response
    else:
        # return HttpResponseRedirect('/login')
        return redirect('/failed')

# 设置中文cookie测试
def set_c_cookie(request):
    response = HttpResponse("设置中文cookie测试")
    s = "你好"
    s = str(s)
    response.set_cookie("h1",s)
    return response