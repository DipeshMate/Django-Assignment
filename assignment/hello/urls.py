from django.urls import path
from .views import *

urlpatterns = [
    path('hello/',hello),
    path('new_users/',new_users, name='new_users'),
    path('users/',users,name='users'),
    path('users/<int:id>/',findUser,name='findUser'),
    path('users/delete/<int:id>/',deleteUser,name='deleteUser'),
    path('editUser/<int:id>',editUser,name='editUser'),
    path('userNotFound/',notFound,)
]
