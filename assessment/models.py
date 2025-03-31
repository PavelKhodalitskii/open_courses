from django.db import models

from courses.models import Answer
from auths.models import ExtendedUser


class Assessment(models.Models):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, blank=False, null=False, verbose_name="Ответ")
    teacher = models.ForeignKey(ExtendedUser, on_delete=models.SET_NULL, blank=False, null=True, verbose_name="Преподаватель")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    value = models.CharField(blank=True, null=True, verbose_name="Оценка")

    def __str__(self):
        if self.value:
            return f"{self.answer}-{self.value}"
        return self.answer

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"