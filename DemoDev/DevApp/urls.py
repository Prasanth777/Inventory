from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login,name='index'),
    url(r'^login/$', views.login,name='login'),
    url(r'^register/$', views.register,name='register'),
    url(r'^gallery/$', views.gallery,name='gallery'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^upload/$',views.upload_image,name='upload'),
    url(r'^flip/(?P<id1>\d+)/(?P<id2>\d+)/$',views.flip,name='flip'),
    url(r'^inventory/(?P<id>\d+)/$',views.gallery,name="gallery_with_pk"),
    url(r'^inventory/(?P<id1>\d+)/Images/(?P<id2>\d+)/$',views.gallery_details,name="gallery_details_with_pk"),
    url(r'^thumb/(?P<id>\d+)$',views.thumbnail_change,name="thumbnail_change"),
    url(r'^order_thumb/(?P<id>\d+)$',views.order_thumbnail_change,name="order_thumbnail_change"),
    url(r'^class/(?P<id>\d+)$',views.class_change,name="class_change"),
    url(r'^inventory_admin/(?P<id>\d+)/$',views.gallery_admin,name="gallery_admin_with_pk"),
    url(r'^filter/$',views.gallery_filter,name="gallery_admin_filter"),
    url(r'^order_filter/$', views.order_filter, name="order_admin_filter"),
    url(r'^orders_admin/(?P<id>\d+)/$',views.orders_admin,name="orders_admin_with_pk"),
    url(r'^orders/(?P<id>\d+)/$',views.orders,name="orders_with_pk"),
    url(r'^orders/(?P<id1>\d+)/Images/(?P<id2>\d+)/$',views.orders_details,name="orders_details_with_pk"),
    url(r'flip_details/(?P<id1>\d+)/Images/(?P<id2>\d+)/$',views.flip_details,name="flip_details_with_pk"),
    url(r'^delete_inventory/(?P<id>\d+)/$',views.delete_inventory,name='delete_invent'),
    url(r'^delete_orders/(?P<id>\d+)/$',views.delete_orders,name='delete_orders'),
    url(r'^orderform/(?P<id>\d+)$',views.order_form,name="order_form"),
    url(r'^orderavailform/(?P<id>\d+)$',views.order_avail_form,name="order_avail_form"),
    url(r'^upload_order/$',views.upload_order,name='upload_order'),

]
