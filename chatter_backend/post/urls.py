from django.urls import path
from . import api

urlpatterns = [
    path('', api.get_post_list, name='get_post_list'),
    path('create/', api.create_post, name='get_post'),
    path('<uuid:id>/', api.create_like_for_post, name="create_like_for_post"),
    path('<uuid:id>/comments/create/', api.create_comment_on_post, name='create_comment_on_post'),
    path('<uuid:id>/comments/', api.get_post_comments_list,
         name='get_post_comments_list'),
    path('<uuid:post_id>/comments/<uuid:comment_id>/', api.create_like_for_comment,
         name='create_like_for_comment'),
    path('by/<uuid:id>/', api.get_profile_post_list, name='get_profile_post_list')
]
