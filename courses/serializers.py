from .models import (Course,
                     CourseStudentRelation,
                     CourseTeacherRelation,
                     Module,
                     Lecture,
                     Task,
                     AnswerOption,
                     Answer,
                     MultiselectAnswer) 

from rest_framework import serializers

class CourseBaseSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Course

class CourseStudentRelationBaseSerialzier(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = CourseStudentRelation

class CourseTeacherRelationBaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = CourseTeacherRelation 

class ModuleBaseSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Module

class LectureBaseSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Lecture

class TaskBaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Task

class ModuleStructSerializer(serializers.ModelSerializer):
    tasks = TaskBaseSerializer(many=True)
    lectures = LectureBaseSerializers(many=True)

    class Meta:
        fields = ['name', 'description', 'order_index', 'tasks', 'lectures']
        model = Module

class CourseStructSerializer(serializers.ModelSerializer):
    modules = ModuleStructSerializer(many=True)

    class Meta:
        fields = ['name', 'description', 'modules']
        model = Course

class AnswerOptionBaseSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = AnswerOption

class AnswerBaseSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Answer

class MultiselectAnswer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Answer