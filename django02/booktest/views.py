from django.shortcuts import render,redirect
from booktest.models import HeroInfo,BookInfo

# Create your views here.
def index(request):
    booklist = BookInfo.objects.all()
    return render(request, 'booktest/index.html', {'booklist':booklist})

def create(request):
    b = BookInfo()
    b.btitle = '风月宝鉴'
    from datetime import date
    b.bpub_date = date(1153,2,3)
    b.save()

    return redirect('/')

def delete(request, bid):
    b = BookInfo.objects.get(id=int(bid))
    b.delete()

    return redirect('/')