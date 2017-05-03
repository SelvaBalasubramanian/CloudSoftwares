
from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^login/$',views.log_pg, name='log_pg'),
   url(r'^softwares/$',views.G_softwares,name='g_softwares'),
   url(r'^softwares/search$',views.G_softwares,name='g_softwares1'),
   url(r'^softwares/(?P<soft_id>[0-9]+)/$',views.G_softwares_view,name='g_softwares_view'),
   url(r'^softwares/(?P<soft_id>[0-9]+)/download/$',views.g_down,name='g_down'),
   url(r'^profile/$',views.login, name='login'),
   url(r'^profile/uploads/(?P<user_id>[0-9]+)$',views.upload_pg, name='upload_pg'),
   url(r'^profile/uploads/(?P<user_id>[0-9]+)/ud$',views.upload, name='upload'),
   url(r'^profile/downloads/(?P<user_id>[0-9]+)$',views.download_pg, name='download_pg'),
   url(r'^profile/softwares/(?P<user_id>[0-9]+)$',views.softwares_pg, name='softwares_pg'),
   url(r'^profile/softwares/(?P<user_id>[0-9]+)/search$',views.softwares_pg, name='soft_search'),
   url(r'^profile/softwares/(?P<user_id>[0-9]+)/(?P<soft_id>[0-9]+)$',views.soft_view, name='soft_view'),
   url(r'^profile/softwares/(?P<user_id>[0-9]+)/(?P<soft_id>[0-9]+)/down$',views.down, name='down'),
   url(r'^profile/view/(?P<user_id>[0-9]+)$',views.view_pg, name='view_pg'),
   url(r'^profile/edit/(?P<user_id>[0-9]+)$',views.edit_pg, name='edit_pg'),
   url(r'^profile/logout/(?P<user_id>[0-9]+)$',views.logout, name='logout'),
   url(r'^reg/$',views.reg_pg, name='reg_pg'),
   url(r'^register/$',views.register, name='register'),

]
