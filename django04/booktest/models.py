from django.db import models

# 自定义管理器
class MyObjects(models.Manager):
    def all(self):
        return super().all().filter(isDelete__exact=0)

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    # 使用了自定义管理器,系统不再提供默认管理器objects
    my_objects = MyObjects()

    class Meta:
        db_table = 'bookinfo'

    def get_pub_date(self):
        return self.bpub_date


