from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=100)
    hbook = models.ForeignKey(BookInfo)

    def __str__(self):
        return self.hname