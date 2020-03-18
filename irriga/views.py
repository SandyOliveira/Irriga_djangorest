from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Usuario
from .serializers import UsuarioSerializer
from  django.shortcuts import  get_object_or_404

class UsuarioView(APIView):
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response({"usuarios": serializer.data})

    def post(self, request):
        usuario = request.data.get('usuario')
        print(usuario)
        serializer = UsuarioSerializer(data=usuario)
        if serializer.is_valid(raise_exception=True):
            usuario_salvo = serializer.save()
        return Response({"success": "Usuario '{}' criado corretamente".format(usuario_salvo.nome)})

    def put(self, request, pk):
        usuario_salvo = get_object_or_404(Usuario.objects.all(), pk=pk)
        data = request.data
        serializer = UsuarioSerializer(instance=usuario_salvo, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            usuario_salvo = serializer.save()
        return Response({"success": "Usuario '{}' atualizado corretamente".format(usuario_salvo.nome)})

    def delete(self, request, pk):
        usuario = get_object_or_404(Usuario.objects.all(), pk=pk)
        usuario.delete()
        return Response({"message": "Usuário com o id `{}` deletado.".format(pk)},status=204)