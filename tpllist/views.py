from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView,CreateView, UpdateView, TemplateView
from django.urls import reverse, reverse_lazy

import json

from tpllist.modules.MainCrawlingServer import CrawlingServer
import tpllist.modules.MongoDBManager as MongoDBManager

from tpllist.models import Customer, Site, Template, User


# Create your views here.
# Main view - default 
class MainView(ListView):
    model = Customer
    template_name = "main/main.html"
    context_object_name = "customers"

class CustomerView(ListView):
    model = Customer
    template_name = "customer_page/dashboard.html"
    context_object_name = "customers"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sites'] = Site.objects.filter(customer_id=self.kwargs['pk'])
        context['customer_id'] = self.kwargs['pk']
        context['curr_customer'] = Customer.objects.filter(customer_id=self.kwargs['pk'])
        context['total_data'] = MongoDBManager.getTotalData(int(1), self.kwargs['pk'])
        context['log_progress_data_alert'] = MongoDBManager.getLogProgressData(int(1),self.kwargs['pk'])['-1']
        context['log_progress_data_process'] = MongoDBManager.getLogProgressData(int(1), self.kwargs['pk'])['0']
        context['log_progress_data_finish'] = MongoDBManager.getLogProgressData(int(1), self.kwargs['pk'])['1']
        # context['customers'] =Customer.objects.all()
        return context

def getStatusCodeData(request, pk):
    period = request.GET.get('period')
    status_code_data = MongoDBManager.getStatusCodeData(int(period), pk)
    return HttpResponse(json.dumps(status_code_data), content_type='application/json')

def getLoadData(request, pk):
    period = request.GET.get('period')
    load_time_data = MongoDBManager.getLoadData(int(period), pk)
    return HttpResponse(json.dumps(load_time_data), content_type='application/json')

def getApdexData(request, pk):
    period = request.GET.get('period')
    apdex_data = MongoDBManager.getApdexData(int(period), pk)
    return HttpResponse(json.dumps(apdex_data), content_type='application/json')

def getModuleData(request, pk):
    period = request.GET.get('period')
    module_data = MongoDBManager.getModuleData(int(period), pk)
    return HttpResponse(json.dumps(module_data), content_type='application/json')

def changeLogProgress(request, pk):
    time = request.GET.get('time')
    progress = request.GET.get('progress')
    change = request.GET.get('change')
    result = MongoDBManager.changeLogProgress(float(time), int(progress), int(change), pk)
    if result:
        return HttpResponse(json.dumps({}), content_type='application/json')




class CustomerInfoView(DetailView):
    model = Customer
    template_name = "tpllist/customer_info.html"
    context_object_name = "customers"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sites'] = Site.objects.filter(customer_id=self.kwargs['pk'])
        context['customer_id'] = self.kwargs['pk']
        context['curr_customer'] = Customer.objects.filter(customer_id=self.kwargs['pk'])
        # context['customers'] =Customer.objects.all()
        return context

class CustomerSiteLV(ListView):
    model = Customer
    template_name = "tpllist/customer_site.html"
    context_object_name = "customers"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sites'] = Site.objects.filter(customer_id=self.kwargs['pk'], parent_site=-1)
        context['customer_id'] = self.kwargs['pk']
        context['curr_customer'] = Customer.objects.filter(customer_id=self.kwargs['pk'])
        # context['customers'] =Customer.objects.all()
        return context

class CustomerSiteDV(DetailView):
    model = Site
    template_name = "tpllist/customer_site_detail.html"
    def get_context_data(self, **kwargs):
        current_path = Site.objects.get(site_id=self.kwargs['pk'])
        # call get_regex and return raw string which gets regex with curr_path
        # path_regex = self.get_regex(current_path.site_url)
        context = super().get_context_data(**kwargs)
        context['sites'] = Site.objects.filter(site_id=self.kwargs['pk'])
        context['subpages'] = Site.objects.filter(parent_site=self.kwargs['pk'])
        context['templates'] = Template.objects.filter(site_id=self.kwargs['pk'])
        context['curr_customer'] = Customer.objects.filter(customer_id=self.kwargs['customer_id'])
        context['curr_site'] = current_path
        context['customer_id'] = self.kwargs['customer_id']
        context['current_path'] = current_path.site_url
        return context


class CustomerDataAddView():
    model = Customer
    template_name = "tpllist/customer_data_add.html"
    context_object_name = "customers"
    
        

class CustomerTplCV(CreateView):
    model = Template
    template_name = "tpllist/customer_tpl_add.html"
    fields = ['customer_id', 'site_id', 'permissions', 'module_id', 'tpl_url', 'tpl_path'] 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = Customer.objects.filter(customer_id=self.kwargs['customer_id'])
        context['sites'] = Site.objects.filter(customer_id=self.kwargs['customer_id'])
        context['customer_id'] = self.kwargs['customer_id']
        context['curr_customer'] = Customer.objects.filter(customer_id=self.kwargs['customer_id'])
        context['templates'] = Template.objects.filter(site_id=self.kwargs['pk'])
        context['curr_site'] = Site.objects.get(site_id=self.kwargs['pk'])
        return context
    
    def get_success_url(self, **kwargs):
        return reverse('tpl_manage:customer_site_detail', args=(self.kwargs['customer_id'], self.kwargs['pk'], ))

class CustomerPermissionLV(ListView):
    model = Customer
    template_name = "tpllist/customer_permissions.html"
    context_object_name = "customers"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs['pk'])
        context['permissions'] = User.objects.filter(customer_id=self.kwargs['pk'])
        context['customer_id'] = self.kwargs['pk']
        context['curr_customer'] = Customer.objects.filter(customer_id=self.kwargs['pk'])
        return context

class CustomerInitView(TemplateView):
    model = Customer
    template_name = "tpllist/customer_init.html"
    context_object_name = "customers"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs['pk'])
        context['customer_id'] = self.kwargs['pk']
        context['curr_customer'] = Customer.objects.filter(customer_id=self.kwargs['pk'])
        return context

class CustomerReportView(TemplateView):
    model = Customer
    template_name = "tpllist/customer_report.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer_id'] = self.kwargs['pk']
        context['report_data'] = MongoDBManager.getTotalReportData(self.kwargs['pk'])
        context['curr_customer'] = Customer.objects.filter(customer_id=self.kwargs['pk'])
        return context


def getSitemapData(request):
    url = request.GET.get('url')
    sitemap_data = CrawlingServer.showSitemap(url)
    return HttpResponse(json.dumps(sitemap_data), content_type='application/json')



# def addCustomerView():
# render
