from django.contrib import admin
from .models import User
from .models import Product

# The dot refers to the same directory - in .models
admin.site.register(User)
admin.site.register(Product)
