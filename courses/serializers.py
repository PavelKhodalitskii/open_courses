from auths.serializers import ExtendedUserBaseSerializer
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
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']
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
        fields = ['id', 'name', 'description', 'order_index', 'tasks', 'lectures']
        model = Module

class CourseStructSerializer(CourseBaseSerializers):
    modules = ModuleStructSerializer(many=True)

    class Meta:
        fields = CourseBaseSerializers.Meta.fields + ['modules']
        model = Course

class CourseStudentsSerializer(CourseBaseSerializers):
    students = ExtendedUserBaseSerializer(many=True)

    class Meta:
        fields = CourseBaseSerializers.Meta.fields + ['students']
        model = Course

class CourseTeachersSerializer(CourseBaseSerializers):
    teachers = ExtendedUserBaseSerializer(many=True)

    class Meta:
        fields = CourseBaseSerializers.Meta.fields + ['teachers']
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