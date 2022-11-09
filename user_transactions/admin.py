from django.contrib import admin

from .models import *


@admin.register(Balance)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('owner', 'balance')


@admin.register(Category)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'action', 'owner')


@admin.register(UserTransactions)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('owner', 'sum', 'time', 'date', 'category', 'organization', 'description')
