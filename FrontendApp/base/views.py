# from django.shortcuts import render,redirect
# import requests
# import json

# # Create your views here.
# def home(request):
#     # api='http://127.0.0.1:8000/api/tasks/'
#     # response=requests.get(url=api)
#     # py_data=response.json()
#     # return render(request,"home.html",{'data':py_data})
#     api='http://127.0.0.1:8000/api/tasks/'
#     response=requests.get(url=api)
#     py_data=response.json()

#     pending = [
#         i for i in py_data
#         if not i['completed'] and not i['trash']
#     ]
#     return render(request,"home.html",{'data':pending})

# def add(request):
#     api='http://127.0.0.1:8000/api/tasks/'

#     if request.method == 'POST':
#         title=request.POST['title']
#         desc=request.POST['desc']
#         py_data={
#             'title': title,
#             'desc': desc
#         }
#         json_data=json.dumps(py_data)
#         response=requests.post(url=api,data=json_data)
#         return redirect(home)
#     return render(request,"add.html")

# def completed(request):
#     api='http://127.0.0.1:8000/api/tasks/'
#     response=requests.get(url=api)
#     py_data=response.json()

#     completed_tasks = [
#         i for i in py_data
#         if i['completed'] and not i['trash']
#     ]

#     return render(request,'completed.html',{'data': completed_tasks})


# def trash(request):
#     api='http://127.0.0.1:8000/api/tasks/'
#     response=requests.get(url=api)
#     py_data=response.json()

#     trash_tasks = [
#         i for i in py_data
#         if i['trash']
#     ]
#     return render(request,'trash.html',{'data':trash_tasks})
      
# def about(request):
#     return render(request,"about.html")


# def update(request,pk):
#     api=f'http://127.0.0.1:8000/api/task/{pk}'
#     response=requests.get(url=api).json()

#     if request.method == 'POST':
#         title=request.POST['title']
#         desc=request.POST['desc']

#         py_data={
#             'title':title,
#             'desc':desc
#         }
#         json_data=json.dumps(py_data)
#         response=requests.put(url=api, data=json_data,headers={'Content-Type': 'application/json'})
#         return redirect(home)
#     return render(request,"update.html",{'data':response})


# def delete(request,pk):
#     api=f'http://127.0.0.1:8000/api/task/{pk}'
#     response=requests.delete(url=api)
#     return redirect(home)


# def complete(request, pk):
#     api = f'http://127.0.0.1:8000/api/task/{pk}'

#     py_data = {
#         'completed': True
#     }

#     json_data = json.dumps(py_data)

#     requests.put(url=api,data=json_data,headers={'Content-Type': 'application/json'})

#     return redirect('home')

# def completeall(request):
#     api = 'http://127.0.0.1:8000/api/completeall/'

#     requests.put(url=api)

#     return redirect('home')

# def delete_all_home(request):

#     api='http://127.0.0.1:8000/api/delete-all-home/'

#     requests.put(api)

#     return redirect('home')


# def completed_delete(request, pk):
#     api = f'http://127.0.0.1:8000/api/task/{pk}'

#     py_data = {
#         'trash': True
#     }

#     json_data = json.dumps(py_data)

#     requests.put(
#         url=api,
#         data=json_data,
#         headers={'Content-Type': 'application/json'}
#     )

#     return redirect('completed')

# def completed_delete_all(request):
#     api = 'http://127.0.0.1:8000/api/completed-delete-all/'

#     requests.put(api)

#     return redirect('completed')


# def restore(request, pk):
#     api = f'http://127.0.0.1:8000/api/task/{pk}'

#     py_data = {
#         'trash': False,
#         'completed': False
#     }

#     json_data = json.dumps(py_data)

#     requests.put(url=api,data=json_data,headers={'Content-Type': 'application/json'})
#     return redirect('home')


# def restore_all(request):
#     api = 'http://127.0.0.1:8000/api/restore-all/'

#     requests.put(api)

#     return redirect('home')


# def delete_forever(request, pk):
#     api = f'http://127.0.0.1:8000/api/delete-forever/{pk}'

#     requests.delete(api)

#     return redirect('trash')



# def delete_all_trash(request):
#     api = 'http://127.0.0.1:8000/api/delete-all-trash/'

#     requests.delete(api)

#     return redirect('trash')

# d

from django.shortcuts import render, redirect
import requests
import json

def home(request):
    user_id = request.user.id
    api = f'http://127.0.0.1:8000/api/tasks/?user_id={user_id}'
    response = requests.get(url=api)
    py_data = response.json()

    pending = [
        i for i in py_data
        if not i['completed'] and not i['trash']
    ]
    return render(request, "home.html", {'data': pending})


def add(request):
    api = 'http://127.0.0.1:8000/api/tasks/'

    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        py_data = {
            'title': title,
            'desc': desc,
            'user_id': request.user.id  # ✅ user_id not user
        }
        json_data = json.dumps(py_data)
        response = requests.post(url=api,data=json_data,headers={'Content-Type': 'application/json'})
        return redirect(home)
    return render(request, "add.html")

def completed(request):
    user_id = request.user.id
    api = f'http://127.0.0.1:8000/api/tasks/?user_id={user_id}'
    response = requests.get(url=api)
    py_data = response.json()

    completed_tasks = [
        i for i in py_data
        if i['completed'] and not i['trash']
    ]
    return render(request, 'completed.html', {'data': completed_tasks})


def trash(request):
    user_id = request.user.id
    api = f'http://127.0.0.1:8000/api/tasks/?user_id={user_id}'
    response = requests.get(url=api)
    py_data = response.json()

    trash_tasks = [
        i for i in py_data
        if i['trash']
    ]
    return render(request, 'trash.html', {'data': trash_tasks})


def about(request):
    return render(request, "about.html")


def update(request, pk):
    api = f'http://127.0.0.1:8000/api/task/{pk}'
    response = requests.get(url=api).json()

    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        py_data = {
            'title': title,
            'desc': desc
        }
        json_data = json.dumps(py_data)
        response = requests.put(url=api, data=json_data,
                                headers={'Content-Type': 'application/json'})
        return redirect(home)
    return render(request, "update.html", {'data': response})


def delete(request, pk):
    api = f'http://127.0.0.1:8000/api/task/{pk}'
    requests.delete(url=api)
    return redirect(home)


def complete(request, pk):
    api = f'http://127.0.0.1:8000/api/task/{pk}'
    py_data = {'completed': True}
    requests.put(url=api, data=json.dumps(py_data),
                 headers={'Content-Type': 'application/json'})
    return redirect('home')


def completeall(request):
    user_id = request.user.id
    api = f'http://127.0.0.1:8000/api/completeall/?user_id={user_id}'
    requests.put(url=api)
    return redirect('home')


def delete_all_home(request):
    user_id = request.user.id
    api = f'http://127.0.0.1:8000/api/delete-all-home/?user_id={user_id}'
    requests.put(api)
    return redirect('home')


def completed_delete(request, pk):
    api = f'http://127.0.0.1:8000/api/task/{pk}'
    py_data = {'trash': True}
    requests.put(url=api, data=json.dumps(py_data),
                 headers={'Content-Type': 'application/json'})
    return redirect('completed')


def completed_delete_all(request):
    user_id = request.user.id
    api = f'http://127.0.0.1:8000/api/completed-delete-all/?user_id={user_id}'
    requests.put(api)
    return redirect('completed')


def restore(request, pk):
    api = f'http://127.0.0.1:8000/api/task/{pk}'
    py_data = {'trash': False, 'completed': False}
    requests.put(url=api, data=json.dumps(py_data),
                 headers={'Content-Type': 'application/json'})
    return redirect('home')


def restore_all(request):
    user_id = request.user.id
    api = f'http://127.0.0.1:8000/api/restore-all/?user_id={user_id}'
    requests.put(api)
    return redirect('home')


def delete_forever(request, pk):
    api = f'http://127.0.0.1:8000/api/delete-forever/{pk}'
    requests.delete(api)
    return redirect('trash')


def delete_all_trash(request):
    user_id = request.user.id
    api = f'http://127.0.0.1:8000/api/delete-all-trash/?user_id={user_id}'
    requests.delete(api)
    return redirect('trash')