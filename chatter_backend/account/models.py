from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone

# Create your models here.

# The class CustomUserManager is not a model itself, but it serves as a manager for a custom user model. 
# In Django, a model manager is a class that provides methods for creating, querying, and managing instances of a model. 
# While a model represents the data structure and behavior of a database table, the manager facilitates interactions with the model instances.
class CustomUserManager(UserManager):
    def _create_user(self, name, email, password, **extra_fields):
        if not email:
            raise ValueError("No valid email address has been provided.")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, email, password, **extra_fields)

    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(name, email, password, **extra_fields)
      

# above code's explanation

# This code defines a custom user manager class, `CustomUserManager`, which is a subclass of Django's built-in `UserManager`. The purpose of creating a custom user manager is to provide methods for creating and managing user instances in a way that suits the specific requirements of the application.

# In Django, the `UserManager` class provides a set of methods for creating and managing user instances. By creating a custom user manager, you can extend or override these methods to include additional functionality or customize the behavior.

# Let's break down the code:

# ```python
# class CustomUserManager(UserManager):
#     def _create_user(self, name, email, password, **extra_fields):
#         if not email:
#             raise ValueError("No valid email address has been provided.")

#         email = self.normalize_email(email)
#         user = self.model(email=email, name=name, **extra_fields)
#         user.set_password(password)
#         user.save(using=self.db)

#         return user
# ```

# Here, a new method `_create_user` is defined. This method is responsible for creating a new user instance. It takes the user's `name`, `email`, `password`, and any additional `extra_fields` as parameters. If no valid email is provided, it raises a `ValueError`.

# The email is normalized using `self.normalize_email(email)`, which ensures that the email is in a standardized format. Then, a new user instance is created using the `self.model` attribute, which is a reference to the user model associated with this manager. The `set_password` method is called to hash and set the user's password. Finally, the user is saved to the database using `user.save(using=self.db)`.

# Two more methods are defined in the `CustomUserManager`:

# ```python
#     def create_user(self, name=None, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(name, email, password, **extra_fields)

#     def create_superuser(self, name=None, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self._create_user(name, email, password, **extra_fields)
# ```

# These methods provide a convenient way to create regular users (`create_user`) and superusers (`create_superuser`). They call the `_create_user` method with appropriate default values for `is_staff` and `is_superuser`.

# In summary, the `CustomUserManager` is designed to be used with a custom user model that inherits from `AbstractBaseUser` and `PermissionsMixin`. It provides custom methods for creating users and superusers, allowing you to extend or customize the user creation process in your Django application.

# =======================================================
# =======================================================
# =======================================================
# =======================================================
    
class User(AbstractBaseUser, PermissionsMixin):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  
  email = models.EmailField(unique=True)
  
  name = models.CharField(max_length=255, blank=True, null=True, default='')
  
  avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
  
  friends = models.ManyToManyField('self')
  
  friends_count = models.IntegerField(default=0)
  
  posts_count = models.IntegerField(default=0)
  
  is_active = models.BooleanField(default=True)
  
  is_superuser = models.BooleanField(default=False)
  
  is_staff = models.BooleanField(default=False)
  
  date_joined = models.DateTimeField(default=timezone.now)
  
  last_login = models.DateTimeField(blank=True, null=True)
  
  objects = CustomUserManager()
  
  USERNAME_FIELD = 'email'
  EMAIL_FIELD = 'email'
  REQUIRED_FIELDS = []
  
   # @property
  def is_friend_of_user(self, requesting_user):
      return self.friends.filter(id=requesting_user.id).exists()
  
  def has_sent_friend_request_to(self, target_user):
      return self.created_friendshiprequests.filter(created_for=target_user, status=FriendshipRequest.SENT).exists()
  
  def has_received_friend_request_from(self, requesting_user):
      return self.received_friendshiprequests.filter(created_by=requesting_user, status=FriendshipRequest.SENT).exists()
  
# above code's explanation 

# This code defines a custom user model named `User` in Django. Let's break down the code:

# ```python
# class User(AbstractBaseUser, PermissionsMixin):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=255, blank=True, default='')
#     avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(default=timezone.now)
#     last_login = models.DateTimeField(blank=True, null=True)
#     objects = CustomUserManager()
#     USERNAME_FIELD = 'email'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = []
# ```

# Here's a breakdown of each part:

# 1. **Inheritance:**
#    - `User` class inherits from both `AbstractBaseUser` and `PermissionsMixin`. `AbstractBaseUser` is a Django class that provides the core implementation of a user model with hashed passwords. `PermissionsMixin` is for handling permissions and groups.

# 2. **Fields:**
#    - `id`: A UUIDField acting as the primary key for the model.
#    - `email`: An EmailField for storing the user's email. It is marked as unique, ensuring that each email is associated with only one user.
#    - `name`: A CharField for the user's name with a maximum length of 255 characters. It's optional (`blank=True`) and has a default value of an empty string.
#    - `avatar`: An ImageField for storing the user's avatar. It is optional (`blank=True`) and can be null (`null=True`).
#    - `is_active`: A BooleanField indicating whether the user is active or not. It has a default value of `True`.
#    - `is_superuser`: A BooleanField indicating whether the user has superuser privileges. It has a default value of `False`.
#    - `is_staff`: A BooleanField indicating whether the user can access the admin site. It has a default value of `False`.
#    - `date_joined`: A DateTimeField storing the date and time when the user was created. It has a default value of the current time.
#    - `last_login`: A DateTimeField indicating the last time the user logged in. It's optional (`blank=True`) and can be null (`null=True`).

# 3. **Custom Manager:**
#    - `objects = CustomUserManager()`: This associates a custom manager (`CustomUserManager`) with the `User` model. This manager provides methods for creating and managing user instances.

# 4. **Username and Email Fields:**
#    - `USERNAME_FIELD = 'email'`: Specifies that the email field will be used as the unique identifier for authentication instead of the default username.
#    - `EMAIL_FIELD = 'email'`: Indicates the field that represents the email address.
#    - `REQUIRED_FIELDS = []`: Specifies any additional fields required when creating a user via the `createsuperuser` management command. In this case, there are no additional required fields.

# In summary, this `User` model is a custom implementation with additional fields like name, avatar, and custom manager (`CustomUserManager`). It also sets the email as the unique identifier for authentication. This model can be used in place of the default Django user model in your application.     

# =======================================================
# =======================================================
# =======================================================
# =======================================================

class FriendshipRequest(models.Model):
    SENT = 'sent'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    
    STATUS_CHOICES = (
        (SENT, 'Sent'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected')
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_for = models.ForeignKey(User,  related_name="received_friendshiprequests", on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,  related_name="created_friendshiprequests", on_delete=models.CASCADE)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=SENT)
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
  