from django.contrib import admin
from .models import Account


class PostAdmin(admin.ModelAdmin):
    list_display = ('Email', 'First_name', 'Last_name', 'unique_id', 'password')


admin.site.register(Account, PostAdmin)
