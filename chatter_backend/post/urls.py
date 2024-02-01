from django.urls import path
from . import api

urlpatterns = [
    path('', api.get_post_list, name='get_post_list'),
    path('create/', api.create_post, name='get_post')
]
