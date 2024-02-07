from .models import Post
from rest_framework import serializers
from account.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
  created_by = UserSerializer(read_only=True)
  is_liked = serializers.SerializerMethodField()
  class Meta:
    model = Post
    fields = ('id', 'body', 'created_by', 'created_at_formatted',
              'likes_count', 'is_liked')

  def get_is_liked(self, obj):
   request = self.context.get('request')
   if request and request.user.is_authenticated:
        return obj.is_liked_by_user(request.user)
   return False
