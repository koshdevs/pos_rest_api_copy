from django.urls import path 
from pos_users.pos_api.views import api_registration_view 

app_name = 'pos_users'

urlpatterns = [
    path('register/',api_registration_view,name='registration'),
]
