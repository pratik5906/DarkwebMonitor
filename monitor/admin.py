from django.contrib import admin
from .models import Credential

@admin.register(Credential)
class CredentialAdmin(admin.ModelAdmin):
    list_display = ('email', 'user', 'is_breached', 'created_at')
    search_fields = ('email', 'user__username')
