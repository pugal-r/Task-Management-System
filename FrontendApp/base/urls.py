from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('add/',add,name='add'),
    path('completed/',completed,name='completed'),
    path('trash/',trash,name='trash'),
    path('about/',about,name='about'),

    path('update/<int:pk>',update,name='update'),
    path('delete/<int:pk>',delete,name='delete'),


    path('complete/<int:pk>', complete, name='complete'),
    path('completeall/', completeall, name='completeall'),
    path('delete-all-home/',delete_all_home,name='delete_all_home'),


    path('completed-delete/<int:pk>',completed_delete,name='completed_delete'),
    path('completed-delete-all/',completed_delete_all,name='completed_delete_all'),

    path('restore/<int:pk>', restore, name='restore'),
    path('restore-all/',restore_all,name='restore_all'),
    path('delete-forever/<int:pk>',delete_forever,name='delete_forever'),
    path('delete-all-trash/',delete_all_trash,name='delete_all_trash')

]