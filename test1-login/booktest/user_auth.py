#!/usr/bin/env python
#coding:utf-8

from django.http import HttpResponseRedirect

def login(func):
    def login_func(request,*args,**kwargs):
        if request.session.has_key('user_id'):
            return func(request,*args,**kwargs)
        else:
            response=HttpResponseRedirect('/login')
            response.set_cookie('uri',request.get_full_path())
            return response
    return login_func
