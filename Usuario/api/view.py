from rest_framework.views import APIView
from .serializers import UsuarioSerializer
from Usuario.models import Usuario
from rest_framework.response import Response

class UsuarioAPIView(APIView):
    
    def get(self,request):
        usuarios = Usuario.objects.all()
        usuarios_serializer = UsuarioSerializer(usuarios, many = True)
        return Response(usuarios_serializer.data)