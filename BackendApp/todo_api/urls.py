from django.urls import path
from .views import *

urlpatterns=[
    path('tasks/',tasks,name='tasks'),
    path('task/<int:pk>',task),
    path('completeall/', complete_all, name='completeall'),
    path('delete-all-home/',delete_all_home,name='delete_all_home'),
    path('completed-delete-all/',completed_delete_all),
    path('delete-forever/<int:pk>',delete_forever,name='delete_forever'),
    path('delete-all-trash/',delete_all_trash,name='delete_all_trash'),
    path('restore-all/',restore_all, name='restore_all')
]