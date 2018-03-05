from django.conf.urls import url
from booktest import views
urlpatterns = [
    url(r'^areas$', views.areas),
    url(r'^login$', views.login),
    url(r'^login_check$', views.login_check),
    url(r'^login_check2$', views.login_check2),
    url(r'^index$', views.index),
    url(r'^login_ajax$', views.login_ajax),
    url(r'^login_ajax_check$', views.login_ajax_check),
    url(r'^cookie_set$', views.cookie_set),
    url(r'^cookie_get$', views.cookie_get),
    url(r'^failed$', views.failed),

    url(r'^set_c_cookie$', views.set_c_cookie),
]