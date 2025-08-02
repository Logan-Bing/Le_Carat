from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'created_at')
    search_fields = ('first_name', 'email')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

admin.site.register(Customer, CustomerAdmin)
