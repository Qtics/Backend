from rest_framework import serializers
from .models import User
from .models import Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['subsystem', 'assembly','component', 'description','unit_price','qty','min_qty','add_cost','discount']