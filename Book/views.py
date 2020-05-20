from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from Book.models import BookInfo
from Book.models import AreaInfo


def index(request):
    temp = loader.get_template('Book/index.html') # 加载模板文件，生成一个模板对象
    context = {'name': '小杨', 'datas': list(range(1, 20))} # 给模板传数据
    html = temp.render(context) # 渲染模板，生成html页面
    return HttpResponse(html) # 返回给浏览器html页面es

def study(request):
    temp = loader.get_template('Book/study.html')
    html = temp.render()
    return HttpResponse(html)

def show_books(request):
    """显示图书网页"""
    # 通过模型M查找数据库中的书籍信息
    book = BookInfo.objects.all()

    # 把数据返回HTML文件
    temp = loader.get_template('Book/books.html')
    context = {'books': book}
    html = temp.render(context)
    return HttpResponse(html)

def details_books(request, ID):
    """显示图书信息"""
    # 根据ID查找书籍
    book = BookInfo.objects.get(id=ID)
    # 根据书籍信息找到人物信息
    people = book.book_peoples.all()
    
    # 返回HTML文件
    return render(request, "Book/details.html", {"book":book, "people":people})

def are(request):
    """广州的信息"""
    area = AreaInfo.objects.get(pk=440100)
    return render(request, 'Book/area.html', {'area': area})

def login(request):
    return render(request, "Book/login.html")

def login_submit(request):
    # 使用request.POST.gey获取参数
    username = request.POST.get("username")
    password = request.POST.get("password")
    # 模拟账号密码判断是否正确
    if "yzy"==username and "123"==password:
        # 密码正确，重定向致首页
        return redirect("index/")
    else:
        # 错误则重定向致登录页面
        return redirect("login/")