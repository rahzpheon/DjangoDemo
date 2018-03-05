from django.shortcuts import render
from django05 import settings
from django.http import HttpResponse,JsonResponse
from booktest.models import ImgInfo,AreaInfo
from django.core.paginator import Paginator

# Create your views here.
# 静态文件测试
def static_test(request):
    return render(request, 'booktest/static_test.html', {})

def index(request):
    ip = request.META["REMOTE_ADDR"]
    print(ip)
    raise Exception("抛出异常")
    return render(request, 'booktest/index.html')

# 表单文件上传页面
def img_upload(request):
    return render(request, 'booktest/img_upload.html')

# 表单图片上传处理
def img_save(request):
    # 从FILES中获取图片对象(表单上传方法为post)
    f1 = request.FILES.get('img1')
    # 定义存储路径
    f_name = settings.MEDIA_ROOT + '/booktest/' + f1.name
    # 写入文件
    with open(f_name, 'wb') as file:
        for c in f1.chunks():
            file.write(c)

    # 保存图片信息至数据库
    ImgInfo.objects.create(ipath=f_name)

    return HttpResponse('上传成功')

# 分页显示数据
# /show_page(\d*)
def show_page(request, pid):
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    # 建立Paginator对象,决定每页显示数量
    my_pages = Paginator(areas, 8)
    # 按页码获取指定分页对象 注意传递来的为str,且要处理pid为“”时
    if pid == "":
        my_page = my_pages.page(1)
    else:
        my_page = my_pages.page(int(pid))

    areas = my_page.object_list

    # 动态在底部生成分页链接,要求首页时没有上一页,尾页时没有下一页
    # 注意在模板关闭自动转义
    link_str = ""
    # 上一页
    if my_page.has_previous():
        link_str += "<a href='" + '/show_page' + str(my_page.previous_page_number()) + "'>上一页</a>"
    # 中间页码
    for num in my_pages.page_range:
        link_str += "<a href='" + '/show_page' + str(num) + "'>" + str(num) + "</a>"
    # 下一页
    if my_page.has_next():
        link_str += "<a href=" + '/show_page' + str(my_page.next_page_number()) + ">下一页</a>"

    # 返回分页内容
    return render(request, 'booktest/show_page.html',{"areas":areas, 'link_str':link_str})

# 三个下拉列表显示省,市,县信息
# 逻辑:在页面加载时显示全部省信息,选择省信息后出现市信息,选择市信息后出现县信息
#       不重要信息用ajax的get方式提交,视图可用request.GET与url正则分组的方式获得提交数据
# 实现:1.注册省下拉列表select事件change:选项改变,显示省对应的市信息
#     2.多次切换时,注意清除之前的信息empty(),而且要保留首行提示行
#     3.切换省信息时,市与县的信息都要清空
#     4.多个ajax请求用多个视图处理
def show_areas(request):    # 主页面
    return render(request, 'booktest/show_areas.html')

# 获取省信息
def get_prov(request):
    # 页面加载时就显示省信息
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    # 要获取的信息内容:地区名,id(用于获取关联地区)
    # 封装成Json字典
    list_area = []
    for area in areas:
        list_area.append([area.atitle,area.id])
    # print(JsonResponse(list_area))
    return JsonResponse({'data':list_area})

# 根据地区的id获取获取子级地区信息,可处理各级子地区
# def get_city(request, aid):
def get_city(request):
    print('ookk')
    # 用aid获取关联地区信息
    aid = request.GET.get('aid')
    areas = AreaInfo.objects.filter(aParent=aid)
    # 要获取的信息内容:地区名,id(用于获取关联地区)
    # 封装成Json字典
    list_area = []
    for area in areas:
        list_area.append([area.atitle,area.id])
    # print(JsonResponse(list_area))
    return JsonResponse({'data':list_area})