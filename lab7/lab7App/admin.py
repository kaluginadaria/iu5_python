from django.contrib import admin
from lab7App.models import *




@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    # fields = ('first_name', 'last_name')
    list_display = ('user', 'first_name')
    list_filter = ('first_name',)
    search_fields = ['last_name', 'first_name']


@admin.register(Orders)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ['name']

