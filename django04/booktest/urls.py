from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),

    # session的设置与获取
    url(r'^set_session', views.set_session),
    url(r'^get_session', views.get_session),
    url(r'^del_session', views.del_session),

    # 模板相关
    url(r'^temp_var', views.temp_var),
    url(r'^temp_tags', views.temp_tags),
    url(r'^temp_filter', views.temp_filter),
    url(r'^temp_self_filter', views.temp_self_filter),
    url(r'^temp_inherit', views.temp_inherit),

    # 反向解析
    url(r'^rev_resolve', views.rev_resolve),
    url(r'^/(\d+)/(\d+)$', views.show_args, name='show_args'),
    url(r'^show_kwargs/(?P<a>\d+)/(?P<b>\d+)$', views.show_kwargs, name='show_kwargs'),
    url(r'^redirect_test$' ,views.redirect_test),

    # html转义
    url(r'^html_escape$', views.html_escape),

    # 登陆验证装饰器
    url(r'^login$', views.login),
    url(r'^login_check$', views.login_check),
    url(r'^test_login_check$', views.test_login_check),

    # csrf跨站请求伪造
    # 官方站点A,访问后会在session中保存登陆信息
    url(r'^transfer_a$', views.transfer_a),
    # 第三方站点B,隐含了使用session偷偷访问站点A的操作
    url(r'^transfer_b$', views.transfer_b),
    url(r'^transfer_action$', views.transfer_action), # 配置好csrf后,第三方站点访问会出现403

    # 验证码
    url(r'^verify_code/(\d+)$', views.verify_code)
]