from .models import User, FriendshipRequest
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
  is_friend_of_user = serializers.SerializerMethodField()
  has_sent_friend_request_to = serializers.SerializerMethodField()
  has_received_friend_request_from = serializers.SerializerMethodField()

  class Meta:
    model = User
    fields = ('id', 'name', 'email', 'friends_count',
              'is_friend_of_user', 'has_sent_friend_request_to', 'has_received_friend_request_from',)

  def get_is_friend_of_user(self, obj):
      request = self.context.get('request')
      if request and request.user.is_authenticated:
          return obj.is_friend_of_user(request.user)
      return False
    
  def get_has_sent_friend_request_to(self, obj):
      request = self.context.get('request')
      if request and request.user.is_authenticated:
          return request.user.has_sent_friend_request_to(obj)
      return False

  def get_has_received_friend_request_from(self, obj):
      request = self.context.get('request')
      if request and request.user.is_authenticated:
          return request.user.has_received_friend_request_from(obj)
      return False

class FriendshipRequestSerializer(serializers.ModelSerializer):
  created_by = UserSerializer(read_only=True)
  created_for = UserSerializer(read_only=True)
  class Meta:
    model = FriendshipRequest
    fields = ('id', 'created_by', 'created_for',)