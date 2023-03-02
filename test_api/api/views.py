from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class User(APIView):
    @csrf_exempt
    def get(self, request):
        user = UserModel.objects.all()
        serializer = UserSerializer(user, many = True)
        data = serializer.data
        response = {"status": "success", "data": data}
        return Response(response)