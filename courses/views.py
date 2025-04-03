from django.shortcuts import render

from rest_framework.generics import (CreateAPIView, 
                                     RetrieveAPIView, 
                                     UpdateAPIView, 
                                     DestroyAPIView)
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import (Course, 
                     CourseStudentRelation,
                     CourseTeacherRelation,
                     Module)
from .serializers import (CourseBaseSerializers, 
                          CourseStudentRelationBaseSerialzier,
                          CourseTeacherRelationBaseSerializer,
                          ModuleBaseSerializers)


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseBaseSerializers

class AddStudentToCourse(CreateAPIView):
    queryset = CourseStudentRelation.objects.all()
    serializer_class = CourseStudentRelationBaseSerialzier

class AddTeacherToCourse(CreateAPIView):
    queryset = CourseTeacherRelation.objects.all()
    serializer_class = CourseTeacherRelationBaseSerializer

class DeleteStudentFromCourse(APIView):
    def delete(self, request, student_id, course_id):
        student_course_rel_obj = CourseStudentRelation.objects.filter(user__id = student_id, course__id = course_id)

        if student_course_rel_obj.exists():
            student_course_rel_obj.delete()
        
        return Response({"status": "ok"})

class DeleteTeacherFromCourse(APIView):
    def delete(self, request, teacher_id, course_id):
        teacher_course_rel_obj = CourseTeacherRelation.objects.filter(user__id = teacher_id, course__id = course_id)

        if teacher_course_rel_obj.exists():
            teacher_course_rel_obj.delete()
        
        return Response({"status": "ok"})

class ModuleViewSet(ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleBaseSerializers