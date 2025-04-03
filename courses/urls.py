from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import (CourseViewSet,
                    ModuleViewSet,
                    AddStudentToCourse,
                    DeleteStudentFromCourse,
                    AddTeacherToCourse,
                    DeleteTeacherFromCourse)

router = DefaultRouter()
router.register(r'course', CourseViewSet)
router.register(r'modules', ModuleViewSet)

urlpatterns = [
    path('students/add', AddStudentToCourse.as_view(), name="add_student"),
    path('students/delete/<int:student_id>/<int:course_id>/', DeleteStudentFromCourse.as_view(), name="delete_student"),

    path('teachers/add', AddTeacherToCourse.as_view(), name="add_student"),
    path('teachers/delete/<int:teacher_id>/<int:course_id>/', DeleteTeacherFromCourse.as_view(), name="delete_student"),
    *router.urls,
]
