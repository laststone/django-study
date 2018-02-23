from django.shortcuts import render

# from django.http import *
# from django.template import RequestContext,loader

# Create your views here.
from .models import *

def index(request):
    # temp = loader.get_template('house_management/index.html')
    # return HttpResponse(temp.render())
    userlist = ih_user_profile.objects.all()
    usercount = ih_user_profile.objects.count()
    context = {'user_list':userlist,'user_sum':usercount}
    return render(request,'house_management/index.html',context)

def userinfo(request,uid):
    user = ih_user_profile.objects.get(up_user_id=uid)
    context = {'user':user}
    return render(request,'house_management/userinfo.html',context)

def userhouse(request,uid):
    user_name = ih_user_profile.objects.get(up_user_id=uid).up_name
    house_list = ih_house_info.objects.filter(hi_user_id=uid)
    context = {'house_list':house_list,'user_name':user_name}
    return render(request,'house_management/userhouse.html',context)

def userorder(request,uid):
    user_name = ih_user_profile.objects.get(up_user_id=uid).up_name
    order_list = ih_order_info.objects.filter(oi_user_id=uid)
    context = {'order_list':order_list,'user_name':user_name}
    return render(request,'house_management/userorder.html',context)