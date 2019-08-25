from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from BookTest.models import BookInfo,HeroInfo


# Create your views here.


def index(request):
    # # 1.加载模板文件,模板对象
    # temp = loader.get_template('BookTest/index.html')
    # # 2.定义模板上下文:给模板文件传递数据
    # context = RequestContext(request, {})
    # # 3.模板渲染:产生标准的html内容
    # ret_html = temp.render(context)
    ret_html = render(request, 'BookTest/index.html', {'content': '内容', 'list': list(range(1, 9))})
    return HttpResponse(ret_html)


def index2(request):
    return HttpResponse('hello python index2')


def show_books(request):
    books = BookInfo.objects.all()
    return render(request, 'BookTest/show_books.html', {'books': books})


def detail(request, bid):
    book = BookInfo.objects.get(id=bid)
    heros = book.heroinfo_set.all()
    return render(request, 'BookTest/details.html', {'book': book, 'heros': heros})
