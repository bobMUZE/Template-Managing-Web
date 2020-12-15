from django.urls import path, re_path
from tpllist import views

app_name = 'tpl_manage'
urlpatterns = [
    # main view - full dashboard 
    path('main/', views.MainView.as_view(), name='main'),
    
    # main - addcustomer
    # path('main/addinfo', views.MainView.as_view(), name='main_add'),


    path('main/<pk>/', views.CustomerView.as_view(), name="customer_main"),
    path('main/<pk>/init', views.CustomerInitView.as_view(), name="customer_init"),
    path('main/<pk>/info', views.CustomerInfoView.as_view(), name="customer_info"),
    path('main/<pk>/site', views.CustomerSiteLV.as_view(), name="customer_site"),
    path('main/<pk>/report', views.CustomerReportView.as_view(), name="customer_report"),
    path('main/<pk>/permissions', views.CustomerPermissionLV.as_view(), name="customer_user"),
    path('main/<str:customer_id>/site/<pk>/', views.CustomerSiteDV.as_view(), name="customer_site_detail"), 
    path('main/<str:customer_id>/site/<pk>/tpl_add', views.CustomerTplCV.as_view(), name="customer_tpl_add"), 


    path('getSitemapInfo/', views.getSitemapData)
]