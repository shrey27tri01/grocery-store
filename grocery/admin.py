from django.contrib import admin
from .models import User, GroceryItem
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(GroceryItem)