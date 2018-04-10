#coding:utf-8
from django.contrib import admin

# Register your models here.

from models import *

class ih_user_profile_Admin(admin.ModelAdmin):
    list_display=['up_name','up_user_id','up_real_name','up_id_card','up_ctime']
    list_filter=['up_real_name']
    search_fields=['up_name']
    list_per_page=20
    fieldset=[
        ('用户ID', {'fields': ['up_user_id']}),
        ('用户昵称',{'fields':['up_name']}),
        ('用户手机',{'fields':['up_mobile']}),
        ('用户密码',{'fields':['up_passwd']}),
        ('用户真实姓名',{'fields':['up_real_name']}),
        ('用户身份证号',{'fields':['up_id_card']}),
        ('用户头像链接',{'fields':['up_avatar']}),
        ('用户是否是管理员',{'fields':['up_admin']}),
        ('用户创建时间',{'fields':['up_utime']}),
        ('用户更新时间',{'fields':['up_ctime']})
    ]
    up_avatar=models.CharField(max_length=128)              # varchar(128) NULL COMMENT '用户头像',
    up_admin=models.BooleanField(default=False)             # tinyint NOT NULL DEFAULT '0' COMMENT '是否是管理员，0-不是，1-是',
    up_utime=models.DateTimeField(null=False)              # datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
    up_ctime=models.DateTimeField(null=False)





class ih_area_info_Admin(admin.ModelAdmin):
    list_display=['ai_name','ai_area_id','ai_ctime']
    list_filter=['ai_area_id']
    search_fields=['ai_name']
    list_per_page=20
    fieldset=[
        ('区域名称',{'fields':['ai_name']}),
        ('区域ID',{'fields': ['ai_area_id']}),
        ('创建时间',{'fields': ['ai_ctime']})
    ]


class ih_house_info_Admin(admin.ModelAdmin):
    list_display=['hi_house_id','hi_title','hi_price','hi_house_unit','hi_order_count']
    list_filter=['hi_title']
    search_fields=['hi_address']
    list_per_page=20
    fieldset=[
        ('房屋ID',{'fields':['hi_house_id']}),
        ('房屋名称',{'fields':['hi_title']}),
        ('房屋价格',{'fields':['hi_price']}),
        ('房屋地址',{'fields':['hi_address']}),
        ('房间数',{'fields':['hi_room_count']}),
        ('房屋面积',{'fields':['hi_acreage']}),
        ('房屋户型',{'fields':['hi_house_unit']}),
        ('允许容纳人数',{'fields':['hi_capacity']}),
        ('床的尺寸',{'fields':['hi_beds']}),
        ('押金',{'fields':['hi_deposit']}),
        ('最短入住时间',{'fields':['hi_min_days']}),
        ('最长入住时间',{'fields':['hi_max_days']}),
        ('下单数量',{'fields':['hi_order_count']}),
        ('订单状态',{'fields':['hi_verify_status']}),
        ('房屋上线状态',{'fields':['hi_online_status']}),
        ('房屋主图片地址',{'fields':['hi_index_image_url']}),
        ('房屋更新时间',{'fields':['hi_utime']}),
        ('房屋发布时间',{'fields':['hi_ctime']}),
        ('房东ID',{'fields':['hi_user_id']}),
        ('房屋区域ID',{'fields':['hi_area_id']}),
    ]
class ih_house_facility_Admin(admin.ModelAdmin):
    list_display=['hf_house_id','hf_id','hf_facility_id','hf_ctime']
    list_filter=['hf_facility_id']
    search_fields=['hf_id']
    list_per_page=20
    fieldset=[
        ('序号',{'fields':['hf_id']}),
        ('设施ID',{'fields':['hf_facility_id']}),
        ('创建时间',{'fields':['hf_ctime']}),
        ('房屋ID',{'fields':['hf_house_id']}),
    ]
class ih_facility_catelog_Admin(admin.ModelAdmin):
    list_display=['fc_id','fc_name','fc_ctime']
    list_filter=['fc_name']
    search_fields=['fc_name']
    list_per_page=20
    fieldset=[
        ('序号',{'fields':['fc_id']}),
        ('设施名称',{'fields':['fc_name']}),
        ('创建时间',{'fields':['fc_ctime']}),
    ]
class ih_order_info_Admin(admin.ModelAdmin):
    list_display=['oi_order_id','oi_status','oi_days','oi_amount','oi_ctime']
    list_filter=['oi_begin_date']
    search_fields=['oi_house_price']
    list_per_page=20
    fieldset=[
        ('订单ID',{'fields':['oi_order_id']}),
        ('入住时间',{'fields':['oi_begin_date']}),
        ('离开时间',{'fields':['oi_end_date']}),
        ('入住天数',{'fields':['oi_days']}),
        ('房屋单价-单位分',{'fields':['oi_house_price']}),
        ('订单金额,-单价分',{'fields':['oi_amount']}),
        ('订单状态-0待接单-1待支付-2已支付-3待评价-4已完成-5已取消-6已拒单',{'fields':['oi_status']}),
        ('订单评论',{'fields':['oi_comment']}),
        ('更新时间',{'fields':['oi_utime']}),
        ('创建时间',{'fields':['oi_ctime']}),
        ('客户ID',{'fields':['oi_user_id']}),
        ('房屋ID',{'fields':['oi_house_id']}),
    ]
class ih_house_image_Admin(admin.ModelAdmin):
    list_display=['hi_house_id','hi_url','hi_ctime']
    list_filter=['hi_ctime']
    search_fields=['hi_url']
    list_per_page=20
    fieldset=[
        ('房屋图片ID',{'fields':['hi_image_id']}),
        ('房屋图片URL',{'fields':['hi_url']}),
        ('房屋创建时间',{'fields':['hi_ctime']}),
        ('房屋ID',{'fields':['hi_house_id']}),
    ]






admin.site.register(ih_user_profile,ih_user_profile_Admin)

admin.site.register(ih_area_info,ih_area_info_Admin)

admin.site.register(ih_house_facility,ih_house_facility_Admin)

admin.site.register(ih_facility_catelog,ih_facility_catelog_Admin)

admin.site.register(ih_order_info,ih_order_info_Admin)

admin.site.register(ih_house_image,ih_house_image_Admin)
