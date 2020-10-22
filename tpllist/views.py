from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView, UpdateView
from django.urls import reverse, reverse_lazy

from tpllist.models import Customer, Site, Template, User


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
        context['sites'] = Site.objects.filter(customer_id=self.kwargs['pk'])
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
        context['sites'] = Site.objects.filter(customer_id=self.kwargs['pk'], is_root=1)
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
        path_regex = self.get_regex(current_path.site_url)
        context = super().get_context_data(**kwargs)
        context['sites'] = Site.objects.filter(site_id=self.kwargs['pk'])
        context['subpages'] = Site.objects.filter(site_url__regex=path_regex)
        context['templates'] = Template.objects.filter(site_id=self.kwargs['pk'])
        context['curr_customer'] = Customer.objects.filter(customer_id=self.kwargs['customer_id'])
        context['curr_site'] = current_path
        context['customer_id'] = self.kwargs['customer_id']
        context['current_path'] = current_path.site_url
        return context
    
    def get_regex(self, curr_path):
        curr_path = curr_path.replace('/', '\/')
        # example = '^http:\/\/218.146.55.65\/[^\/]*\/$'
        regex = "^"+curr_path+r"[^\/]*\/$"
        return regex
    
        

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
