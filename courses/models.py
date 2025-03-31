from auths.models import ExtendedUser

from django.db import models

class TaskTypesChoices(models.TextChoices):
    '''
    Типы заданий
    '''
    
    TEST = 'TEST', 'Тест'
    PROGRAMMING = 'PROGRAMMING', 'Программирование'
    SHORT_ANSWER = 'SHORT_ANSWER', 'Краткий ответ'
    FILE_UPLOAD = 'FILE_UPLOAD', 'Загрузка файла'
    TEXT_ANSWER = 'TEXT_ANSWER', 'Ответ в виде текста'
    MULTICHOICE = 'MULTISELECT', 'Мультиселект'
    RADIO = 'RADIO', 'Один вариант ответа'

class Course(models.Model):
    '''
    Курс
    '''
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    tags = models.ManyToManyField('tags.Tag', through='tags.CourseTag', verbose_name='Тэги')
    
    teachers = models.ManyToManyField(ExtendedUser, through='CourseTeacherRelation', related_name='teaching_courses', verbose_name='Преподаватели')
    students = models.ManyToManyField(ExtendedUser, through='CourseStudentRelation', related_name='enrolled_courses', verbose_name='Студенты')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

class CourseTeacherRelation(models.Model):
    '''
    Отношение Курс-Преподаватель
    '''
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    user = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE, verbose_name='Преподаватель')
    
    class Meta:
        verbose_name = "Отношение Курс-Преподаватель"
        verbose_name_plural = "Отношения Курсы-Преподаватели"
        unique_together = ('course', 'user')

class CourseStudentRelation(models.Model):
    '''
    Отношение Курс-Студент
    '''
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    user = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE, verbose_name='Студент')
    
    class Meta:
        verbose_name = "Отношение Курс-Студент"
        verbose_name_plural = "Отношения Курсы-Студенты"
        unique_together = ('course', 'user')

class Module(models.Model):
    '''
    Модуль курса
    '''
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules', verbose_name='Курс')

    name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Имя')
    order_index = models.PositiveIntegerField(blank=False, null=False, verbose_name='Порядок в курсе')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    
    def __str__(self):
        return f"{self.course.name} - {self.name}"
    

    class Meta:
        verbose_name = "Модуль курса"
        verbose_name_plural = "Модули курсов"        
        ordering = ['order_index']
        unique_together = ('course', 'order_index')

class Lecture(models.Model):
    '''
    Лекция
    '''
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lectures', blank=False, null=False, verbose_name='Имя')

    name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Название')
    text = models.TextField(blank=True, null=True, verbose_name='Содержание')
    video_url = models.URLField(blank=True, null=True, verbose_name='URL Video')
    order_index = models.PositiveIntegerField(blank=False, null=False, verbose_name='Порядок в модуле')
    
    def __str__(self):
        return f"{self.module.name} - {self.name}"
    
    class Meta:
        verbose_name = "Лекция"
        verbose_name_plural = "Лекции"      
        ordering = ['order_index']
        unique_together = ('module', 'order_index')

class Task(models.Model):
    '''
    Базовая модель задания
    '''
    
    module = models.ForeignKey(Module, on_delete=models.CASCADE, blank=False, null=False, related_name='tasks', verbose_name='Модуль')

    name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Имя')
    description = models.TextField(blank=True, null=False, verbose_name='Описание')
    autocheck = models.BooleanField(default=False, verbose_name='Автопроверка')
    type = models.CharField(max_length=128, choices=TaskTypesChoices, blank=False, null=False, verbose_name='Тип')

    def __str__(self):
        return f"{self.module.name} - {self.name}"
    
    class Meta:
        verbose_name = "База Задания"
        verbose_name_plural = "Базы Заданий"

class Test(models.Model):
    '''
    Тест
    '''
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='tests', blank=False, null=False, verbose_name='Модуль')
    name = models.CharField(max_length=255, blank=False, null=True, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    exam = models.BooleanField(default=False, verbose_name='Экзамен')
    order_index = models.PositiveIntegerField(blank=False, null=False, verbose_name='Порядок в модуле')

    tasks = models.ManyToManyField(Task, through='TestTaskRelation')
    
    def __str__(self):
        return f"{self.module.name} - {self.name}"
    
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        ordering = ['order_index']
    
class TestTaskRelation(models.Model):
    '''
    Отношение тест-задача
    '''
    test = models.ForeignKey(Test, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Тест')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Задача')
    order_index = models.PositiveIntegerField(blank=False, null=False, verbose_name='Порядок в тесте')

    class Meta:
        verbose_name = "Отношение тест-задача"
        verbose_name_plural = "Отношения тест-задача"
        ordering = ['order_index']
        unique_together = ('test', 'task')

class AnswerOption(models.Model):
    '''
    Вариант ответа для мультиселект вопросов
    '''
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='answer_options', blank=False, null=False, verbose_name='Задание')
    text = models.TextField(blank=False, null=False, verbose_name='Текст варианта ответа')
    correct = models.BooleanField(default=False, verbose_name='Правильный')
    
    def __str__(self):
        return f"{self.text[:50]}"
    
    class Meta:
        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответов"

class Answer(models.Model):
    '''
    База ответа на задание
    '''

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='answers', blank=False, null=False, verbose_name='Задание')
    user = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE, related_name='answers', blank=False, null=False, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    
    def __str__(self):
        return f"Ответ {self.user.username} на {self.task.name} от {self.created_at}"
    
    class Meta:
        verbose_name = "База ответа"
        verbose_name_plural = "Базы ответов"
        
class RadioAnswer(models.Model):
    '''
    Ответы на задачи с единственным вариантом ответа
    '''
    answer_option = models.OneToOneField(AnswerOption, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Выбранный ответ')
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE, blank=False, null=False, verbose_name="База ответа")

    class Meta:
        verbose_name = "Ответ на задачи с единственным вариантом ответа"
        verbose_name_plural = "Ответы на задачи с единственным вариантом ответа"

class MultiselectAnswer(models.Model):
    '''
    Ответы на задачи с множественными вариантами ответов
    '''
    text = models.TextField(blank=True, null=True, verbose_name='Текст ответа')
    selected_options = models.ManyToManyField(AnswerOption, through='SelectedOptions', verbose_name='Выбранные ответы')
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE, blank=False, null=False, verbose_name="База ответа")

    class Meta:
        verbose_name = "Ответ на задачу с множественными вариантами ответов"
        verbose_name_plural = "Ответы на задачи с множественными вариантами ответов"

class ProgrammingTaskAnswer(models.Model):
    '''
    Ответы на задачи на программирование
    '''
    code = models.TextField(blank=True, null=True, verbose_name='Код')
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE, blank=False, null=False, verbose_name="База ответа")

    class Meta:
        verbose_name = "Ответ на задачу на программирование"
        verbose_name_plural = "Ответы на задачи на программирование"

class ShortAnswer(models.Model):
    '''
    Ответы на задачи с которким ответом
    '''
    text = models.CharField(max_length=128, blank=True, null=True, verbose_name='Текст ответа')
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE, blank=False, null=False, verbose_name="База ответа")

    class Meta:
        verbose_name = "Ответ на задачу с которким ответом"
        verbose_name_plural = "Ответы на задачи с которким ответом"   

class TextAnswer(models.Model):
    '''
    Ответы на задачи с текстовым ответом
    '''
    text = models.TextField(max_length=30000, blank=True, null=True, verbose_name='Текст ответа')
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE, blank=False, null=False, verbose_name="База ответа")

    class Meta:
        verbose_name = "Ответ на задачу с текстовым ответом"
        verbose_name_plural = "Ответы на задачи с текстовым ответом"


class SelectedOptions(models.Model):
    '''
    Выбранные ответы для задач с множественным выбором
    '''
    answer_option = models.ForeignKey(AnswerOption, on_delete=models.CASCADE)
    options_task_answer = models.ForeignKey(MultiselectAnswer, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('answer_option', 'options_task_answer')
