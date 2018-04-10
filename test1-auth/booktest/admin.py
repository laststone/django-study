from django.contrib import admin
from models import *

from booktest import models
from user_admin import UserAdmin

admin.site.register(models.UserProfile,UserAdmin)


# Register your models here.

class HeroInfoInline(admin.TabularInline):
	model = HeroInfo
	extra = 3


class BookInfoAdmin(admin.ModelAdmin):
	list_display=['id','btitle','bpub_date']
	list_filter=['btitle']
	search_fields=['btitle']
	list_per_page=1
	fieldsets=[
		('base',{'fields':['btitle']}),
		('super',{'fields':['bpub_date']})
	]
	inlines = [HeroInfoInline]


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)


