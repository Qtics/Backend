from formulathon.sign_up_views import sign_up
from formulathon.login_views import login
from django.contrib import admin
from django.urls import path
from formulathon import sign_up_views
from formulathon import login_views
from formulathon import product_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', sign_up_views.sign_up),
    path('login/', login_views.login, name='login'),
    path('products/',product_views.product),

]
