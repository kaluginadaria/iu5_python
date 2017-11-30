from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
def var(request):
    # return HttpResponse('response from function view')
    return render(request, 'temp.html', {'myvariable': 'hello world'})


# class ExampleClassBased():
#     def get(self, request):
#         return HttpResponse('response from class based')
class OrdersView(View):
    def get(self, request):
        data = {
            'orders': [
                {'title': 'Первый заказ', 'id': 1},
                {'title': 'Второй заказ', 'id': 2},
                {'title': 'Третий заказ', 'id': 3}
            ]
        }
        return render(request, 'orders.html', data)


class OrderView(View):
    def get(self, request, id):
        data = {
            'order': {
                'id': id
            }
        }
        return render(request, 'order.html', data)


def home(request):
    params = {
        'phrase': 'Переход на страницу с заказами'
    }
    return render(request, 'home.html', context=params)
