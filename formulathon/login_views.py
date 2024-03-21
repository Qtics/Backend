from .models import User
from .serializer import UserSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def login(request, format=None):
    if request.method == 'POST':
        # Retrieve username and password from the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Perform user authentication (You can use Django's built-in authentication or your own method)
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Invalid username or password'}, status=400)

        # You can generate and return a token for authenticated users if you are implementing token-based authentication.

        user_data = UserSerializer(user).data
        response_data = {
            'success': True,
            'details': user_data
        }
        return JsonResponse(response_data, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
