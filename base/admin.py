from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import Room, Topic, Message, User


class UserAdmin(UserAdmin):
    list_display = ('email', 'name', 'bio', 'is_active')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, UserAdmin)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
