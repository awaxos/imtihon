from django.contrib import admin
from django.contrib.auth.models import Group, User

from apps.models import Friend


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass
