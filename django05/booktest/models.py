from django.db import models
from django.contrib import admin

# Create your models here.
class AreaInfo(models.Model):
    atitle = models.CharField(max_length=20)
    aParent = models.ForeignKey('self', null=True, blank=True)

#定义图书模型类BookInfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)#图书名称
    bpub_date = models.DateField()#发布日期
    bread = models.IntegerField('阅读量',default=0)#阅读量
    bcomment = models.IntegerField(default=0)#评论量
    isDelete = models.BooleanField(default=False)#逻辑删除

    def get_title(self):
        return self.btitle
    get_title.admin_order_field = 'bcomment'    # 为方法指定排序依据
    get_title.short_description = '自定义标题'   #

    def __str__(self):
        return self.btitle

    class Meta:
        verbose_name = '元选项标题'
        verbose_name_plural = verbose_name
        pass

#定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)#英雄姓名
    hgender = models.BooleanField(default=True)#英雄性别
    isDelete = models.BooleanField(default=False)#逻辑删除
    hcomment = models.CharField(max_length=200)#英雄描述信息
    hbook = models.ForeignKey('BookInfo')#英雄与图书表的关系为一对多，所以属性定义在英雄模型类中

    # 在后台管理类显示关联对象的属性时,要通过方法返回,在管理类中注册方法名
    def book(self):
        if self.hbook is None:
            return ''
        return self.hbook.btitle

# 图片上传保存
class ImgUpload(models.Model):
    image = models.ImageField(upload_to='booktest') # 图片保存路径

# 图片上传信息
class ImgInfo(models.Model):
    ipath = models.CharField(max_length=1000)  # 保存路径信息