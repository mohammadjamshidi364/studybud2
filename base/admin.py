from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

class UserAccount(UserAdmin):
    pass

admin.site.register(User , UserAccount)
admin.site.register(Topics)
admin.site.register(Room)