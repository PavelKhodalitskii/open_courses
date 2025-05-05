from django.db.models import QuerySet

from .models import Course

from auths.models import ExtendedUser

class CourseController:
    @staticmethod
    def get_all_user_courses(user: ExtendedUser) -> QuerySet | None:
        courses = Course.objects.filter(author__pk = user.pk)
        if courses.exists():
            return courses.all()
        return None