from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.decorators import api_view 

from pos_users.pos_api.serializers import RegistrationSerializer 

@api_view(['POST',])
def api_registration_view(request):

    if request.method == 'POST':

        serializer = RegistrationSerializer(data=request.data)

        data = {}
        if serializer.is_valid():

            user = serializer.save()
            data["success"] = "User registered successfully"
            data["email"] = user.email 
            data["username"] = user.username 

        else: 

            data = serializer.errors

        return Response(data)