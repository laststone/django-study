from django.shortcuts import render

# Create your views here.

#from django.http import *
#from django.template import RequestContext,loader
from .models import *


def index(request):
    return render(request,'booktest/index.html')


from . import user_auth


@user_auth.login
def booklist(request):
#    temp = loader.get_template('booktest/index.html')
#    return HttpResponse(temp.render())
#    context = {'title':'23456'}
    all_book_list = BookInfo.objects.all()
    context = {'book_list':all_book_list}
    return  render(request,'booktest/booklist.html',context)

@user_auth.login
def show(request,id):
    book=BookInfo.objects.get(pk=id)
    bookname=book.btitle
    herolist=book.heroinfo_set.all()
    context = {'hero_list':herolist,'book_name':bookname}
    return render(request,'booktest/show.html',context)


