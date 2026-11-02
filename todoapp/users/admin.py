from django.contrib import admin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display =['first_name','last_name','email','password','last_login','is_staff','is_superuser','date_joined']
    search_fields = ['email']

admin.site.register(CustomUser, CustomUserAdmin)

