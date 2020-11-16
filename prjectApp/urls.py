from django.conf.urls import url

from prjectApp import views


urlpatterns = [
    url(r'^login/',views.login,name="login"),
    url(r'^home/',views.home,name='home'),
    url(r'^user/',views.user,name="user"),
    url(r'^$',views.index,name='index'),
    url(r'^manage/',views.manage,name='manage'),
    url(r'^error/',views.error,name='error'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^choujiang/',views.choujiang,name='choujiang'),
    url(r'^chongzhi/', views.chongzhi, name='chongzhi'),

]