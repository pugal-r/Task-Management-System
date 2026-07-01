# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import *
# from .serializer import *
# from rest_framework.renderers import JSONRenderer
# from rest_framework.decorators import api_view
# from django.views.decorators.csrf import csrf_exempt
# import io
# from rest_framework.parsers import JSONParser
# from rest_framework.response import Response
# from rest_framework import status

# # Create your views here.

# @api_view(['GET','POST'])
# @csrf_exempt
# def tasks(request):
#     if request.method == 'GET':
#         model_instance=TaskModel.objects.all()
#         ser_py=TaskSerializer(model_instance,many=True)
#         py_data=ser_py.data
#         # json_data=JSONRenderer().render(py_data)
#         # return HttpResponse('Hello api')
#         return Response(py_data)

#     if request.method == 'POST':
#         req_data=request.body
#         stream_data=io.BytesIO(req_data)
#         py_data=JSONParser().parse(stream_data)
#         de_ser=TaskSerializer(data=py_data)
#         if de_ser.is_valid():
#             de_ser.save()
#             # json_data=JSONRenderer().render({'mesg':'Data Created Successfully..!'})
#             # return Response(json_data)
#             return Response(status=status.HTTP_201_CREATED)
        

#     if request.method == 'DELETE':
#         data=TaskModel.objects.all().delete()
#         return Response(status=status.HTTP_410_GONE)
        
# @api_view(['GET','PUT','DELETE'])
# @csrf_exempt
# def task(request,pk):
#     try:
#         model_instance=TaskModel.objects.get(id=pk)
#     except:
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     if request.method == 'GET':

#         ser_py=TaskSerializer(model_instance)
#         py_data=ser_py.data
#         # json_data=JSONRenderer().render(py_data)
#         # return HttpResponse(json_data)
#         return Response(py_data)
    
#     if request.method == 'PUT':
#         # req_data=request.body
#         # stream_data=io.BytesIO(req_data)
#         # py_data=JSONParser().parse(stream_data)
#         de_ser=TaskSerializer(model_instance,data=request.data,partial=True)
#         if de_ser.is_valid():
#             de_ser.save()
#             return Response(status=status.HTTP_202_ACCEPTED)
        
#     if request.method == 'DELETE':
#         model_instance.trash = True
#         model_instance.save()
#     return Response(status=status.HTTP_202_ACCEPTED)



# @api_view(['PUT'])
# @csrf_exempt
# def complete_all(request):
#     TaskModel.objects.filter(completed=False).update(completed=True)

#     return Response(
#         {'message': 'All Tasks Completed'},
#         status=status.HTTP_202_ACCEPTED
#     )


# @api_view(['PUT'])
# @csrf_exempt
# def delete_all_home(request):

#     TaskModel.objects.filter(trash=False).update(trash=True)

#     return Response(
#         {'message':'All Tasks moved to Trash'},
#         status=status.HTTP_202_ACCEPTED
#     )


# @api_view(['PUT'])
# @csrf_exempt
# def completed_delete_all(request):

#     TaskModel.objects.filter(
#         completed=True,
#         trash=False
#     ).update(trash=True)

#     return Response(status=status.HTTP_202_ACCEPTED)



# @api_view(['DELETE'])
# @csrf_exempt
# def delete_forever(request, pk):
#     try:
#         task = TaskModel.objects.get(id=pk)
#     except TaskModel.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     task.delete()

#     return Response(status=status.HTTP_410_GONE)



# @api_view(['DELETE'])
# @csrf_exempt
# def delete_all_trash(request):

#     TaskModel.objects.filter(
#         trash=True
#     ).delete()

#     return Response(status=status.HTTP_410_GONE)



# @api_view(['PUT'])
# @csrf_exempt
# def restore_all(request):

#     TaskModel.objects.filter(
#         trash=True
#     ).update(
#         trash=False,
#         completed=False
#     )

#     return Response(status=status.HTTP_202_ACCEPTED)


from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
@csrf_exempt
def tasks(request):
    user_id = request.query_params.get('user_id')

    if request.method == 'GET':
        if user_id:
            model_instance = TaskModel.objects.filter(user_id=user_id)
        else:
            model_instance = TaskModel.objects.all()
        ser_py = TaskSerializer(model_instance, many=True)
        return Response(ser_py.data)

    if request.method == 'POST':
        de_ser = TaskSerializer(data=request.data)
        if de_ser.is_valid():
            de_ser.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(de_ser.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        TaskModel.objects.all().delete()
        return Response(status=status.HTTP_410_GONE)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def task(request, pk):
    try:
        model_instance = TaskModel.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        ser_py = TaskSerializer(model_instance)
        return Response(ser_py.data)

    if request.method == 'PUT':
        de_ser = TaskSerializer(model_instance, data=request.data, partial=True)
        if de_ser.is_valid():
            de_ser.save()
            return Response(status=status.HTTP_202_ACCEPTED)

    if request.method == 'DELETE':
        model_instance.trash = True
        model_instance.save()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['PUT'])
@csrf_exempt
def complete_all(request):
    user_id = request.query_params.get('user_id')
    TaskModel.objects.filter(user_id=user_id, completed=False).update(completed=True)
    return Response({'message': 'All Tasks Completed'}, status=status.HTTP_202_ACCEPTED)


@api_view(['PUT'])
@csrf_exempt
def delete_all_home(request):
    user_id = request.query_params.get('user_id')
    TaskModel.objects.filter(user_id=user_id, trash=False).update(trash=True)
    return Response({'message': 'All Tasks moved to Trash'}, status=status.HTTP_202_ACCEPTED)


@api_view(['PUT'])
@csrf_exempt
def completed_delete_all(request):
    user_id = request.query_params.get('user_id')
    TaskModel.objects.filter(user_id=user_id, completed=True, trash=False).update(trash=True)
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['DELETE'])
@csrf_exempt
def delete_forever(request, pk):
    try:
        task = TaskModel.objects.get(id=pk)
    except TaskModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    task.delete()
    return Response(status=status.HTTP_410_GONE)


@api_view(['DELETE'])
@csrf_exempt
def delete_all_trash(request):
    user_id = request.query_params.get('user_id')
    TaskModel.objects.filter(user_id=user_id, trash=True).delete()
    return Response(status=status.HTTP_410_GONE)


@api_view(['PUT'])
@csrf_exempt
def restore_all(request):
    user_id = request.query_params.get('user_id')
    TaskModel.objects.filter(user_id=user_id, trash=True).update(trash=False, completed=False)
    return Response(status=status.HTTP_202_ACCEPTED)