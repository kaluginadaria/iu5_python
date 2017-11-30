from .models import *
from django.views.generic import ListView


# Create your views here.
class OrdersView(ListView):
    model = Orders
    template_name = 'templ.html'
    context_object_name = 'orders_list'
