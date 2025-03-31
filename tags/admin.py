from django.contrib import admin

# Register your models here.
from .models import (Tag,
                     CourseTag)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tag._meta.fields]

@admin.register(CourseTag)
class CourseTagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CourseTag._meta.fields]

