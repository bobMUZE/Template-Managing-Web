from django.shortcuts import render
from django.views.generic import ListView, DetailView

from tpllist.models import Customer, Sites, Templates

# Create your views here.
# Main view - default 
class MainView(ListView):
    model = Customer
    template_name = "tpllist/main.html"
    context_object_name = "customers"



class TplMainView(ListView):
    model = Customer
    template_name = "tpllist/tpl_main.html"
    context_object_name = 'customers'

class MaketplLV(ListView): 
    # one view multi model test
    model = Customer
    context_object_name = 'customers'
    extra_context = {
        'sites' : Sites.objects.all()
    }
    template_name = "tpllist/maketpl_all.html"


class CustomerLV(ListView):
    template_name = "tpllist/customer_list.html"
    model = Customer
    context_object_name = 'customers'

class CustomerDV(DetailView):
    template_name = "tpllist/customer_detail.html"
    model = Customer
    context_object_name = 'customers'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sites'] = Sites.objects.filter(customer_id=self.kwargs['pk'])
        # context['customers'] =Customer.objects.all()
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
