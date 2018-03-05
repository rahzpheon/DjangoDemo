# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('atitle', models.CharField(max_length=20)),
                ('aParent', models.ForeignKey(blank=True, null=True, to='booktest.AreaInfo')),
            ],
        ),
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_date', models.DateField()),
                ('bread', models.IntegerField(verbose_name='阅读量', default=0)),
                ('bcomment', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '元选项标题',
                'verbose_name_plural': '元选项标题',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField(default=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('hcomment', models.CharField(max_length=200)),
                ('hbook', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
        migrations.CreateModel(
            name='ImgInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ipath', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ImgUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to='booktest')),
            ],
        ),
    ]
