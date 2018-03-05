from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^static_test$', views.static_test),

    url(r'^img_upload$', views.img_upload), # 表单图片上传
    url(r'^img_save$', views.img_save), # 上传图片保存处理

    url(r'^show_page(?P<pid>\d*)$', views.show_page), # 分页显示数据

    url(r'^show_areas$', views.show_areas), # 下拉列表显示省市县
    url(r'^get_prov$', views.get_prov), # 获取省信息
    url(r'^get_city$', views.get_city), # 获取市信息
    url(r'^get_dist$', views.get_city), # 获取县信息
    # url(r'^get_city(\d+)$', views.get_city), # 获取市信息
    # url(r'^get_dist(\d+)$', views.get_city), # 获取县信息,使用相同视图处理
]