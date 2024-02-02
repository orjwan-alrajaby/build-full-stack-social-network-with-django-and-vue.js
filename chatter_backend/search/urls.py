from django.urls import path
from . import api

urlpatterns = [
    path('<str:query>/', api.search_users_and_posts_list,
         name='search_users_and_posts_list'),
]
