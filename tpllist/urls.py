from django.urls import path, re_path
from tpllist import views

app_name = 'tpl_manage'
urlpatterns = [
    # main view - full dashboard 
    path('main/', views.MainView.as_view(), name='main'),
    re_path(r'^main/(?P<pk>[-\w]+)/$', views.CustomerView.as_view(), name='customer_main'),    
    path('main/<pk>/info', views.CustomerInfoView.as_view(), name="customer_info"),
    path('main/<pk>/site', views.CustomerSiteLV.as_view(), name="customer_site"),
    path('main/<pk>/permissions', views.CustomerPermissionLV.as_view(), name="customer_user"),
    path('main/<str:customer_id>/site/<pk>/', views.CustomerSiteDV.as_view(), name="customer_site_detail"), 
    path('main/<str:customer_id>/site/<pk>/tpl_add', views.CustomerTplCV.as_view(), name="customer_tpl_add"), 



    # # Example: /blog/
    # path('', views.PostLV.as_view(), name='index'),

    # # Example : /blog/post/
    # path('', views.PostLV.as_view(), name='post_list'),

    # # Example : /blog/post/django-example/
    # re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),
]