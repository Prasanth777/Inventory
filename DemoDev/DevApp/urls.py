from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login,name='index'),
    url(r'^login/$', views.login,name='login'),
    url(r'^register/$', views.register,name='register'),
    url(r'^gallery/$', views.gallery,name='gallery'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^upload/$',views.upload_image,name='upload'),
    url(r'^gallery/(?P<id>\d+)/$',views.gallery,name="gallery_with_pk"),
    url(r'^gallery/(?P<id1>\d+)/Images/(?P<id2>\d+)/$',views.gallery_details,name="gallery_details_with_pk"),
    url(r'thumb/(?P<id>\d+)$',views.thumbnail_change,name="thumbnail_change"),
    url(r'class/(?P<id>\d+)$',views.class_change,name="class_change"),
    url(r'^gallery_admin/(?P<id>\d+)/$',views.gallery_admin,name="gallery_admin_with_pk"),
    url(r'^filter/$',views.gallery_filter,name="gallery_admin_filter"),
    url(r'^delete/(?P<id>\d+)/$',views.delete_inventory,name='delete_invent')
]
