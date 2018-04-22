#coding:utf-8
from django.contrib import admin

# Register your models here.

from models import *

class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 3

class BookInfoAdmin(admin.ModelAdmin):
    list_display=['id','btitle','bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 2
    fieldsets = [
        ('书籍名称',{'fields':['btitle']}),
        ('出版日期',{'fields':['bpub_date']})
    ]
    inlines = [HeroInfoInline]


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)
