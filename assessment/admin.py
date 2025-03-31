from django.contrib import admin

from .models import Assessment

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Assessment._meta.fields]
