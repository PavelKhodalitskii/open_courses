from django.contrib import admin

from .models import ExtendedUser

@admin.register(ExtendedUser)
class ExtendedUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ExtendedUser._meta.fields]
