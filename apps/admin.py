from django.contrib.admin import ModelAdmin
from django.contrib import admin
from django.contrib.auth.models import Group, User

from apps.models import Category, Product


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    pass


# @admin.register(Blog)
# class BlogInfoAdmin(admin.ModelAdmin):
#     list_display = ['name']
#
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name']
#
#
# @admin.register(CustomUser)
# class UserModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'username']
#
#
# @admin.register(Product)
# class ProductModelAdmin(admin.ModelAdmin):
#     list_display = ['name', 'price']
#     fields = [_('name'), _('price')]
