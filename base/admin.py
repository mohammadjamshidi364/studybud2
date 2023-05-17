from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

class UserAccount(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password", "bio", "avatar")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    
    
admin.site.register(User , UserAccount)
admin.site.register(Topics)
admin.site.register(Room)
admin.site.register(Message)