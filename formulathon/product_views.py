from .serializer import ProductSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from win11toast import toast
import pandas as pd

@api_view(['GET','POST'])
def product(request, format=None):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)

        # components = Product.component.objects.all().values()  # Fetch all components
        #components = product.component_set.all().values()
        #df = pd.DataFrame(components)
        #if (df[df['qty'] < df['min_qty']]):
        #toast('LOW INVENTORY. PLS RESTOCK', duration = '5')

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return Response(serializer.data, status = status.HTTP_201_CREATED)
            product_data = serializer.data
            response_data = {
                'success': True,
                'details': product_data
            }
            return JsonResponse(response_data, status=201)
        else:
            # You can provide a more specific error message based on the validation errors
            return JsonResponse({'error': 'Invalid user data', 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@api_view(['GET','PUT','DELETE','POST'])
def product_detail(request, id, format=None):

    try:
        products = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        #To check is something is a valid request
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        #Takes object in get
        serializer = ProductSerializer(products)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        products.save()
        serializer = ProductSerializer(products)
        return Response(serializer.data)