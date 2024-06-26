from django.db import models
import uuid
from account.models import User
from django.utils.timesince import timesince


# Create your models here.

class Like(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  created_by = models.ForeignKey(
      User, related_name="likes", on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

class PostAttachment(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  image = models.ImageField(upload_to='post_attachments')
  created_by = models.ForeignKey(
      User, related_name="post_attachments", on_delete=models.CASCADE)


class Comment(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  body = models.TextField(blank=False, null=True)
  created_by = models.ForeignKey(
      User, related_name="comments", on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  likes = models.ManyToManyField(Like, blank=True)
  likes_count = models.IntegerField(default=0)
  
  def created_at_formatted(self):
    return timesince(self.created_at)
  
  def is_liked_by_user(self, user):
    return self.likes.filter(created_by=user).exists()

class Post(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  
  body = models.TextField(blank=True, null=True)
  
  attachments = models.ManyToManyField(PostAttachment, blank=True)
  
  likes = models.ManyToManyField(Like, blank=True)
  likes_count = models.IntegerField(default=0)
  
  comments = models.ManyToManyField(Comment, blank=True)
  comments_count = models.IntegerField(default=0)
  
  created_at = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
  
  def created_at_formatted(self):
    return timesince(self.created_at)
  
  def is_liked_by_user(self, user):
    return self.likes.filter(created_by=user).exists()

  def is_commented_on_by_user(self, user):
    return self.comments.filter(created_by=user).exists()
