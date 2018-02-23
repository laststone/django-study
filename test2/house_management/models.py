#coding:utf-8
from django.db import models

# Create your models here.



#1用户信息表
class ih_user_profile(models.Model):
    up_user_id=models.AutoField(null=False,primary_key=True)                   # bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '用户ID',
    up_name=models.CharField(max_length=32,null=False,unique=True)             # varchar(32) NOT NULL COMMENT '昵称',
    up_mobile=models.CharField(max_length=11,null=False,unique=True)           # char(11) NOT NULL COMMENT '手机号',
    up_passwd=models.CharField(max_length=64)               # varchar(64) NOT NULL COMMENT '密码',
    up_real_name=models.CharField(max_length=32)            # varchar(32) NULL COMMENT '真实姓名',
    up_id_card=models.CharField(max_length=20)              # varchar(20) NULL COMMENT '身份证号',
    up_avatar=models.CharField(max_length=128)              # varchar(128) NULL COMMENT '用户头像',
    up_admin=models.BooleanField(default=False)             # tinyint NOT NULL DEFAULT '0' COMMENT '是否是管理员，0-不是，1-是',
    up_utime=models.DateTimeField(null=False)              # datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
    up_ctime=models.DateTimeField(null=False)              # datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    class Meta:
        db_table='ih_user_profile'
    def __str__(self):
        return self.up_name.encode('utf-8')

#2房源区域表
class ih_area_info(models.Model):
    ai_area_id=models.AutoField(null=False,primary_key=True)  # bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '区域id',
    ai_name=models.CharField(max_length=32)                   # varchar(32) NOT NULL COMMENT '区域名称',
    ai_ctime=models.DateTimeField(null=False)                 # datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    class Meta:
        db_table='ih_area_info'
    def __str__(self):
        return self.ai_name.encode('utf-8')

#3房屋信息表
class ih_house_info(models.Model):
    hi_house_id=models.AutoField(null=False,primary_key=True) # bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '房屋id',
    hi_title=models.CharField(max_length=64)                  # varchar(64) NOT NULL COMMENT '房屋名称',
    hi_price=models.IntegerField(null=False,default=0)        # int unsigned NOT NULL DEFAULT '0' COMMENT '房屋价格，单位分',
    hi_address=models.CharField(max_length=512)               # varchar(512) NOT NULL DEFAULT '' COMMENT '地址',
    hi_room_count=models.IntegerField(null=False,default=1)   # tinyint unsigned NOT NULL DEFAULT '1' COMMENT '房间数',
    hi_acreage=models.IntegerField(null=False,default=0)      # int unsigned unsigned NOT NULL DEFAULT '0' COMMENT '房屋面积',
    hi_house_unit=models.CharField(max_length=32,null=False,default='') # varchar(32) NOT NULL DEFAULT '' COMMENT '房屋户型',
    hi_capacity=models.IntegerField(null=False,default=1)     #int unsigned NOT NULL DEFAULT '1' COMMENT '容纳人数',
    hi_beds=models.CharField(max_length=64,default='')        # varchar(64) NOT NULL DEFAULT '' COMMENT '床的配置',
    hi_deposit=models.IntegerField(null=False,default=0)      # int unsigned NOT NULL DEFAULT '0' COMMENT '押金，单位分',
    hi_min_days=models.IntegerField(null=False,default=1)     # int unsigned NOT NULL DEFAULT '1' COMMENT '最短入住时间',
    hi_max_days=models.IntegerField(null=False,default=0)     # int unsigned NOT NULL DEFAULT '0' COMMENT '最长入住时间，0-不限制',
    hi_order_count=models.IntegerField(null=False,default=0)  # int unsigned NOT NULL DEFAULT '0' COMMENT '下单数量',
    hi_verify_status=models.IntegerField(null=False,default=0) # tinyint NOT NULL DEFAULT '0' COMMENT '审核状态，0-待审核，1-审核未通过，2-审核通过',
    hi_online_status=models.IntegerField(null=False,default=1) # tinyint NOT NULL DEFAULT '1' COMMENT '0-下线，1-上线',
    hi_index_image_url=models.CharField(max_length=256)        # varchar(256) NULL COMMENT '房屋主图片url',
    hi_utime=models.DateTimeField(null=False)                  # datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
    hi_ctime=models.DateTimeField(null=False)                  # datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    hi_user_id=models.IntegerField(null=False)                 # CONSTRAINT FOREIGN KEY (`hi_user_id`) REFERENCES `ih_user_profile` (`up_user_id`),
    hi_area_id=models.IntegerField(null=False)                 # CONSTRAINT FOREIGN KEY (`hi_area_id`) REFERENCES `ih_area_info` (`ai_area_id`)
    class Meta:
        db_table='ih_house_info'
    def __str__(self):
        return self.hi_title

#4房屋设施表
class ih_house_facility(models.Model):
    hf_id=models.AutoField(null=False,primary_key=True)        # bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
    hf_facility_id=models.IntegerField(null=False)             # int unsigned NOT NULL COMMENT '房屋设施',
    hf_ctime=models.DateTimeField(null=False)                  # datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    hf_house_id=models.IntegerField(null=False,default=0)      # bigint unsigned NOT NULL COMMENT '房屋id',
    class Meta:
        db_table='ih_house_facility'



#5设施记录表
class ih_facility_catelog(models.Model):
    fc_id=models.AutoField(null=False,primary_key=True)        # int unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
    fc_name=models.CharField(max_length=32,null=False)         # varchar(32) NOT NULL COMMENT '设施名称',
    fc_ctime=models.DateTimeField(null=False)                 # datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    class Meta:
        db_table='ih_facility_catelog'
    def __str__(self):
        return self.fc_name.encode('utf-8')

#6订单表
class ih_order_info(models.Model):
    oi_order_id=models.AutoField(null=False,primary_key=True)  # bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '订单id',
    oi_begin_date=models.DateTimeField(null=False)             # date NOT NULL COMMENT '入住时间',
    oi_end_date=models.DateTimeField(null=False)               # date NOT NULL COMMENT '离开时间',
    oi_days=models.IntegerField(null=False)                    # int unsigned NOT NULL COMMENT '入住天数',
    oi_house_price=models.IntegerField(null=False)             # int unsigned NOT NULL COMMENT '房屋单价，单位分',
    oi_amount=models.IntegerField(null=False)                  # int unsigned NOT NULL COMMENT '订单金额，单位分',
    oi_status=models.IntegerField(null=False)                  # tinyint NOT NULL DEFAULT '0' COMMENT '订单状态，0-待接单，1-待支付，2-已支付，3-待评价，4-已完成，5-已取消，6-拒接单',
    oi_comment=models.TextField()                              # text NULL COMMENT '订单评论',
    oi_utime=models.DateTimeField(null=False,)                 # datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
    oi_ctime=models.DateTimeField(null=False,)                 # datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    oi_user_id=models.IntegerField(null=False)                 # CONSTRAINT FOREIGN KEY (`oi_user_id`) REFERENCES `ih_user_profile` (`up_user_id`)
    oi_house_id=models.IntegerField(null=False)                # CONSTRAINT FOREIGN KEY (`oi_house_id`) REFERENCES `ih_house_info` (`hi_house_id`),
    class Meta:
        db_table='ih_order_info'
    def __str__(self):
        return str(self.oi_order_id)



#7房屋图片表
class ih_house_image(models.Model):
    hi_image_id=models.AutoField(null=False,primary_key=True)   # bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '图片id',
    hi_url=models.CharField(max_length=256)                      # varchar(256) NOT NULL COMMENT '图片url',
    hi_ctime=models.DateTimeField(null=False)                   # datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    hi_house_id=models.IntegerField(null=False)                # bigint unsigned NOT NULL COMMENT '房屋id',
    class Meta:
        db_table='ih_house_image'

