from django.shortcuts import render
from django.views.generic import ListView, DetailView

from tpllist.models import Customer, Sites, Templates

# Create your views here.
# Main view - default 
class MainView(ListView):
    model = Customer
    template_name = "tpllist/main.html"
    context_object_name = "customers"

class CustomerView(ListView):
    model = Customer
    template_name = "tpllist/customer.html"
    context_object_name = "customers"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sites'] = Sites.objects.filter(customer_id=self.kwargs['pk'])
        context['customer_id'] = self.kwargs['pk']
        context['curr_customer'] = Customer.objects.filter(customer_id=self.kwargs['pk'])
        # context['customers'] =Customer.objects.all()
        return context

class CustomerInfoView(DetailView):
    model = Customer
    template_name = "tpllist/customer_info.html"
    context_object_name = "customers"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sites'] = Sites.objects.filter(customer_id=self.kwargs['pk'])
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
        context['sites'] = Sites.objects.filter(customer_id=self.kwargs['pk'])
        context['customer_id'] = self.kwargs['pk']
        context['curr_customer'] = Customer.objects.filter(customer_id=self.kwargs['pk'])
        # context['customers'] =Customer.objects.all()
        return context

class CustomerSiteDV(DetailView):
    model = Sites
    template_name = "tpllist/customer_site_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sites'] = Sites.objects.filter(site_id=self.kwargs['pk'])
        context['templates'] = Templates.objects.filter(site_id=self.kwargs['pk'])
        context['curr_customer'] = Customer.objects.filter(customer_id=self.kwargs['customer_id'])
        context['customer_id'] = self.kwargs['customer_id']
        context['site_path'] = Sites.objects.filter(site_id=self.kwargs['pk'])
        return context

class CustomerTplDV(DetailView):
    template_name = "tpllist/customer_tpl_detail.html"
    model = Sites
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = Customer.objects.filter(customer_id=self.kwargs['customer_id'])
        context['sites'] = Sites.objects.filter(customer_id=self.kwargs['customer_id'])
        context['templates'] = Templates.objects.filter(site_id=self.kwargs['pk'])
        return context
