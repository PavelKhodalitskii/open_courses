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

class TaskBaseSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Task

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