from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from booktest.models import BookInfo


# Create your views here.
def index(request):
    return render(request, 'booktest/index.html', {})

def set_session(request):
    # 设置session信息,注意默认是保存在数据库的表django_session中
    request.session['name'] = 'cool Li'
    request.session['age'] = 18
    return HttpResponse('这是设置session的测试页面，请检查页面，查看cookie中有无sessionid')

def get_session(request):
    # 获取session信息,用字典的方式获取值
    username = request.session['name']
    age = str(request.session['age'])
    rep_str = '这是获取session的测试页面，通过cookie中带有的sessionid(同域名下所有cookie都会发出)查询数据库,验证数据查询成功与否'
    if username is not None and age is not None:
        rep_str += '&gt;'+username+'&gt;'+str(age)
    else:
        rep_str = '没有查到session信息.'

    return HttpResponse(rep_str)

def del_session(request):
    # 删除session信息,包括缓存与数据库
    request.session.clear()
    # 强制缓存内容与数据库中同步
    request.session.flush()
    return HttpResponse('清除cookie的所有值')

# 记录用户登陆状态
# 1.在登陆校验页面,设置登陆状态的session
# 2.在首页,查找session信息,根据内容显示不同结果
def login(request):
    return render(request, 'booktest/login.html', {})

def login_check(request):
    # 校验验证码,应放在最前面
    if request.POST.get('yzm') != request.session['verifycode']:
        return JsonResponse({'b':2})
    username = request.POST.get('username')
    print('用户名：', username)
    if username == 'xiaoming':
        request.session['islogin'] = True
        request.session['username'] = 'xiaoming'
        return JsonResponse({'b':1})
    else:
        return JsonResponse({'b':0})
    # return redirect('/index')

# 模板变量
def temp_var(request):
    # 模板变量解析顺序 1.字典/列表 2.对象属性 3.对象方法
    # 都是通过.调用
    a = {'name':'xiaoming'}
    b = BookInfo.objects.get(id=1)
    c = [1,2,3,4,5,6,7,8]
    return render(request, 'booktest/temp_var.html', {'a':a, 'b':b,'c':c})

# 模板标签
def temp_tags(request):
    # 模板标签 for,if
    # 条件判断
    books = BookInfo.my_objects.all()
    return render(request, 'booktest/temp_tags.html', {'books':books})

# 模板变量过滤器演示
def temp_filter(request):
    # {{ 模板变量 | 过滤器:参数 }}  参数可以省略
    # 常用: date日期 default默认值 length元素个数
    books = BookInfo.my_objects.all()
    return render(request, 'booktest/temp_filter.html', {'books':books})

# 自定义模板变量过滤器
# 1.在应用下创建templatetags目录
# 2.在templatetags目录下创建一个.py文件,存放自定义过滤器函数
# 3.具体定义在那边查看
def temp_self_filter(request):
    # {{ 模板变量 | 过滤器:参数 }}  参数可以省略
    # 常用: date日期 default默认值 length元素个数
    books = BookInfo.my_objects.all()
    return render(request, 'booktest/temp_self_filter.html', {'books':books})

# 模板继承
# 节省代码,提高复用率
# 可多重继承 父——子——孙
def temp_inherit(request):
    books = BookInfo.my_objects.all()
    # 直接访问孙模块
    return render(request, 'booktest/temp_inherit_grandson.html', {'books': books})

# 反向解析1:在模板中反向解析
# 格式: {% url 'namespace:name' %}
# 填写在原本是url的地方,会根据namespace与name
# 从urls.py中定向至指定视图
def rev_resolve(request):
    return render(request, 'booktest/rev_resolve.html', {})

# 显示参数
# urls中的正则要设置位置分组接收
# (\d+)/(\d+)
def show_args(request, a, b):
    return HttpResponse(a + ':' + b)

# 显示关键字参数
def show_kwargs(request, a, b):
    return HttpResponse(a + ':' + b)

# 反向解析2:视图
# 传递参数无需增加url正则分组
def redirect_test(request):
    from django.core.urlresolvers import reverse
    re_rul = reverse('booktest1:show_args', args=(1,2))

    return redirect(re_rul)

# html转义:对于上下文中的部分字符,模板会将其转为转义字符
# 目的:避免用户输入操作html页面,提高html安全性
# 可以使用过滤器/标签 对转义进行 开/关
def html_escape(request):
    context = {'text1':'<h1>文本内容</h1>'}
    return render(request, 'booktest/html_escape.html', context)

# 登陆验证装饰器:把验证登陆状态的功能抽取为装饰器
# 登陆状态等用户信息应在登陆验证时写入session,cookie
# 方便其他页面调用
def check_decorator(func):
    def wrapper(request,*args, **kwargs):
        # 验证islogin是否存在
        if request.session.has_key('islogin'):
            # 成功则返回原本要返回的结果
            return func(request, *args, **kwargs)
            # 失败则重定向至登陆页面
        else:
            print('未登录用户尝试访问')
            return redirect('/login')
    return wrapper

# 验证装饰器具测试:只有登陆状态才可进入此页面
@check_decorator
def test_login_check(request):
    username = request.session['username']
    return render(request, 'booktest/test_login_check.html', {'username':username})

# csrf跨域访问伪造测试
# 如果有一个页面B伪装成A页面的样子,隐藏了表单中自己的card_id
# 那么用户点击提交时就会用自己的username向card_id转账
def transfer_a(request):    # 页面A
    return render(request, 'booktest/transfer_a.html', {})
def transfer_b(request):    # 页面B
    return render(request, 'booktest/transfer_b.html', {})

@check_decorator
def transfer_action(request):
    """转账处理"""
    # 获取转账金额和卡号
    amount = request.POST.get('amount')
    card_id = request.POST.get('card_id')

    # 获取登录的用户名
    username = request.session.get('username')
    # 进行转账处理...
    msg = '%s给%s卡号转了%s元' % (username, card_id, amount)
    return HttpResponse(msg)

# 生成验证码
# 生成的值保存在session中,生成的图片数据返回,在模板的img标签中赋予src
# 提示1：随机生成字符串后存入session中，用于后续判断。
# 提示2：视图返回mime-type为image/png。
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
def verify_code(request, a):
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    buf = BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')