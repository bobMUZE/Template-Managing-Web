from django.urls import path, re_path
from tpllist import views

app_name = 'tpl_manage'
urlpatterns = [
    # main view - full dashboard 
    path('make_tpl/', views.MaketplLV.as_view(), name='make_tpl'),

    path('tpl_main/', views.TplMainView.as_view(), name='index'),
    path('main/', views.MainView.as_view(), name='main'),
    path('customer_list/', views.CustomerLV.as_view(), name='customer_list'),
    re_path(r'^customer_list/(?P<pk>[-\w]+)/$', views.CustomerDV.as_view(), name='customer_detail'), 
    # customer_list/<customer_id>/<site_id>
    path('customer_list/<str:customer_id>/<pk>/', views.CustomerTplDV.as_view(), name='customer_tpl_detail')


    # # Example: /blog/
    # path('', views.PostLV.as_view(), name='index'),

    # # Example : /blog/post/
    # path('', views.PostLV.as_view(), name='post_list'),

    # # Example : /blog/post/django-example/
    # re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),
]