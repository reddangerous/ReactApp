from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse 

from EmployeeApp.models import Employee,Department
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer


# Create your views here.
@csrf_exempt
def DepartmentApi(request,id=0):
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
       Department= Department.objects.get(DepartmentId=data['DepartmentId'])
       serializer = DepartmentSerializer(Department, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        Department.objects.get(DepartmentId=id).delete()
        return JsonResponse({'message': 'Department Deleted'}, status=204)
    else:
        return JsonResponse({'message': 'Not Found'}, status=404)