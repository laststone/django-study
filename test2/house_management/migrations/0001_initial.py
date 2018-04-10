# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ih_area_info',
            fields=[
                ('ai_area_id', models.AutoField(serialize=False, primary_key=True)),
                ('ai_name', models.CharField(max_length=32)),
                ('ai_ctime', models.DateTimeField()),
            ],
            options={
                'db_table': 'ih_area_info',
            },
        ),
        migrations.CreateModel(
            name='ih_facility_catelog',
            fields=[
                ('fc_id', models.AutoField(serialize=False, primary_key=True)),
                ('fc_name', models.CharField(max_length=32)),
                ('fc_ctime', models.DateTimeField()),
            ],
            options={
                'db_table': 'ih_facility_catelog',
            },
        ),
        migrations.CreateModel(
            name='ih_house_facility',
            fields=[
                ('hf_id', models.AutoField(serialize=False, primary_key=True)),
                ('hf_facility_id', models.IntegerField()),
                ('hf_ctime', models.DateTimeField()),
                ('hf_house_id', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'ih_house_facility',
            },
        ),
        migrations.CreateModel(
            name='ih_house_image',
            fields=[
                ('hi_image_id', models.AutoField(serialize=False, primary_key=True)),
                ('hi_url', models.CharField(max_length=256)),
                ('hi_ctime', models.DateTimeField()),
                ('hi_house_id', models.IntegerField()),
            ],
            options={
                'db_table': 'ih_house_image',
            },
        ),
        migrations.CreateModel(
            name='ih_house_info',
            fields=[
                ('hi_house_id', models.AutoField(serialize=False, primary_key=True)),
                ('hi_title', models.CharField(max_length=64)),
                ('hi_price', models.IntegerField(default=0)),
                ('hi_address', models.CharField(max_length=512)),
                ('hi_room_count', models.IntegerField(default=1)),
                ('hi_acreage', models.IntegerField(default=0)),
                ('hi_house_unit', models.CharField(default=b'', max_length=32)),
                ('hi_capacity', models.IntegerField(default=1)),
                ('hi_beds', models.CharField(default=b'', max_length=64)),
                ('hi_deposit', models.IntegerField(default=0)),
                ('hi_min_days', models.IntegerField(default=1)),
                ('hi_max_days', models.IntegerField(default=0)),
                ('hi_order_count', models.IntegerField(default=0)),
                ('hi_verify_status', models.IntegerField(default=0)),
                ('hi_online_status', models.IntegerField(default=1)),
                ('hi_index_image_url', models.CharField(max_length=256)),
                ('hi_utime', models.DateTimeField()),
                ('hi_ctime', models.DateTimeField()),
                ('hi_user_id', models.IntegerField()),
                ('hi_area_id', models.IntegerField()),
            ],
            options={
                'db_table': 'ih_house_info',
            },
        ),
        migrations.CreateModel(
            name='ih_order_info',
            fields=[
                ('oi_order_id', models.AutoField(serialize=False, primary_key=True)),
                ('oi_begin_date', models.DateTimeField()),
                ('oi_end_date', models.DateTimeField()),
                ('oi_days', models.IntegerField()),
                ('oi_house_price', models.IntegerField()),
                ('oi_amount', models.IntegerField()),
                ('oi_status', models.IntegerField()),
                ('oi_comment', models.TextField()),
                ('oi_utime', models.DateTimeField()),
                ('oi_ctime', models.DateTimeField()),
                ('oi_user_id', models.IntegerField()),
                ('oi_house_id', models.IntegerField()),
            ],
            options={
                'db_table': 'ih_order_info',
            },
        ),
        migrations.CreateModel(
            name='ih_user_profile',
            fields=[
                ('up_user_id', models.AutoField(serialize=False, primary_key=True)),
                ('up_name', models.CharField(unique=True, max_length=32)),
                ('up_mobile', models.CharField(unique=True, max_length=11)),
                ('up_passwd', models.CharField(max_length=64)),
                ('up_real_name', models.CharField(max_length=32)),
                ('up_id_card', models.CharField(max_length=20)),
                ('up_avatar', models.CharField(max_length=128)),
                ('up_admin', models.BooleanField(default=False)),
                ('up_utime', models.DateTimeField()),
                ('up_ctime', models.DateTimeField()),
            ],
            options={
                'db_table': 'ih_user_profile',
            },
        ),
    ]
