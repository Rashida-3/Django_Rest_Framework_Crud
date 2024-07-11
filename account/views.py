from django.shortcuts import render
from rest_framework .response import Response
from .models import student
from rest_framework.views import APIView
from .serializers import studentserde

# Create your views here.


class StudentAPI(APIView):
    def post(self,request):
        serializer=studentserde(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors)
        return Response({"msg":"created success"})    


    def get(self,request,pk=None):
        id=pk
        if id:
            stu=student.objects.get(id=id)
            serializer=studentserde(stu)
            return Response(serializer.data)
        stu=student.objects.all()
        serializer=studentserde(stu, many=True)
        print(serializer.data)
        return Response(serializer.data)   


    def put(self,request):
        pass
