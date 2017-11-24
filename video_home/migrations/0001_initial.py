# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveWord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
            ],
            managers=[
                ('lw_m', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='MessageBoard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
            managers=[
                ('mb_m', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('headerImg', models.ImageField(default='static/images/1.jpg', upload_to='static/images/')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('isVip', models.NullBooleanField()),
                ('isDelete', models.NullBooleanField()),
            ],
            managers=[
                ('u_m', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='VideoCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vc_name', models.CharField(max_length=50)),
                ('remark', models.TextField()),
            ],
            managers=[
                ('vc_m', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='VideoLove',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vl_n', models.CharField(max_length=50)),
                ('vl_u', models.CharField(max_length=50)),
            ],
            managers=[
                ('vl_m', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='VideoResource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vr_name', models.CharField(max_length=50)),
                ('vr_img', models.ImageField(upload_to='')),
                ('vr_resource', models.FileField(upload_to='static/resource')),
                ('vr_description', models.TextField()),
                ('vr_score', models.CharField(max_length=10)),
                ('vr_director', models.CharField(max_length=50)),
                ('vr_actor', models.CharField(max_length=100)),
                ('vr_release_time', models.CharField(max_length=50)),
                ('vr_play_view', models.CharField(max_length=10)),
                ('vr_remark', models.CharField(max_length=50)),
                ('vr_zone', models.CharField(max_length=20)),
                ('vr_tag', models.CharField(max_length=20)),
                ('VideoType_id', models.IntegerField()),
            ],
            managers=[
                ('vr_m', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='VideoType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vt_name', models.CharField(max_length=50)),
                ('videocategory_id', models.IntegerField()),
            ],
            managers=[
                ('vt_m', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='messageboard',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video_home.User'),
        ),
        migrations.AddField(
            model_name='leaveword',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video_home.User'),
        ),
    ]