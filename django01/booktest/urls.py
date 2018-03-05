from django.conf.urls import url
from booktest import views

urlpatterns = [
                # 首页url
                url(r'^$', views.index),
                # 详细页url
                url(r'^(\d+)/$',views.detail)
                ]
