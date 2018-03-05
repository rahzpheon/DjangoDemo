from django.shortcuts import render
from booktest.models import BookInfo,HeroInfo
# Create your views here.
def index(request):
    # 获取所有书本数据
    booklist = BookInfo.objects.all()
    return render(request, 'booktest/index.html', {'booklist':booklist})

def detail(request, bid):   # book的id要传进来作为参数
    # 注意：一对多的关系中,先获取‘一’的对象，再用对象.xxx_set.all()获取‘多’
    # 获取书本
    book = BookInfo.objects.get(id=int(bid))
    # 获取书本对应的英雄
    herolist = book.heroinfo_set.all()

    # 将所有的英雄数据
    return render(request, 'booktest/detail.html', {'book':book,'herolist': herolist})