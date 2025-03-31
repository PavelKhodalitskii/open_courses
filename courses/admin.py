from django.contrib import admin

from .models import (Course,
                     CourseTeacherRelation,
                     CourseStudentRelation,
                     Module,
                     Lecture,
                     Task,
                     Test,
                     TestTaskRelation,
                     Answer)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Course._meta.fields]

@admin.register(CourseTeacherRelation)
class CourseTeacherRelationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CourseTeacherRelation._meta.fields]
    
@admin.register(CourseStudentRelation)
class CourseStudentRelationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CourseStudentRelation._meta.fields]

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Module._meta.fields]

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Lecture._meta.fields]

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Task._meta.fields]

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Test._meta.fields]

@admin.register(TestTaskRelation)
class TestTaskRelationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TestTaskRelation._meta.fields]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Answer._meta.fields]