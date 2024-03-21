from .serializer import UserSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User

@api_view(['GET','POST'])
def sign_up(request, format=None):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return Response(serializer.data, status = status.HTTP_201_CREATED)
            user_data = serializer.data
            response_data = {
                'success': True,
                'details': user_data
            }
            return JsonResponse(response_data, status=201)
        else:
            # You can provide a more specific error message based on the validation errors
            return JsonResponse({'error': 'Invalid user data', 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


