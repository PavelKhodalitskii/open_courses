from django.db import models

from courses.models import Course

class Tag(models.Model):
    '''
    Тэг для категоризации курсов
    '''

    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

class CourseTag(models.Model):
    '''
    Отношение крус-тэг
    '''
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Отношение крус-тэг'
        verbose_name_plural = 'Отношения крусы-тэги'
        unique_together = ('course', 'tag')