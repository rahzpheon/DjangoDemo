from django.db import models

# Create your models here.
class Areas(models.Model):

    # 自关联表
    atitle = models.CharField(max_length=20)
    aParent = models.ForeignKey('self', null=True, blank=True)

    class Meta:
        db_table = "booktest_areainfo"

# 自定义管理器
# 作用：1.修改原始查询集  2.添加自定义方法
class AreasManager(models.Manager):

    def all(self):
        return super().all().filter(aParent__isNull=True)

    def create_area(self, title, Parent=None):
        a = self.model()
        a.atitle = title
        a.aParent = Parent
        a.save()