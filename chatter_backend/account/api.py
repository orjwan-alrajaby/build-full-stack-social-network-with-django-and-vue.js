from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SignupForm

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
  data = request.data
  
  form = SignupForm({
    'email': data.get('email'),
    'name': data.get('name'),
    'password1': data.get('password1'),
    'password2': data.get('password2'),
  })
  
  if form.is_valid():
    form.save()
    
    # send verification email sometime.
    
    return JsonResponse({
      'message': 'user created successfully.',
      'status': status.HTTP_201_CREATED
    })
  else:    
    if len(form.errors.keys()) > 0:
      return JsonResponse({
        'message': "Bad request. User data is not valid.",
        'status': status.HTTP_400_BAD_REQUEST,
        'errors': form.errors
      })
    return  JsonResponse({'message':'Unexpected error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





# 
# {
#     "message": "something went wrong.",
#     "status": 400,
#     "errors": {
#         "email": [
#             "Enter a valid email address."
#         ],
#         "password2": [
#             "The two password fields didn\u2019t match."
#         ]
#     }
# }
