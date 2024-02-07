from django.urls import path
from . import api

urlpatterns = [
    path('', api.get_post_list, name='get_post_list'),
    path('create/', api.create_post, name='get_post'),
    path('<uuid:id>/', api.create_like_for_post, name="create_like_for_post"),
    path('by/<uuid:id>/', api.get_profile_post_list, name='get_profile_post_list')
]
