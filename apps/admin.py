from django.contrib.admin import ModelAdmin
from django.contrib import admin
from django.contrib.auth.models import Group, User

from apps.models import Profile, Work


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Work)
class WorkModelAdmin(admin.ModelAdmin):
    pass

#
# @admin.register(Product)
# class ProductModelAdmin(admin.ModelAdmin):
#     list_display = ['name', 'price']
#     fields = [_('name'), _('price')]
