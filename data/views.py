import os

from django.conf import settings
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import \
    APIView  # Certifique-se de importar corretamente a classe APIView

from data.models import Code
from data.serializer import CodeSerializer


class CodesViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer

class JavaFileViewSet(APIView):  # Use a classe APIView ao invés de ViewSet
    def get(self, request, filename=None):  # Use o método 'get' ao invés de 'retrieve'
        # Obter o caminho absoluto completo para a pasta 'java_files'
        java_files_directory = os.path.join(settings.BASE_DIR, 'java_files')

        # Verifica se o arquivo Java existe no diretório 'java_files'
        java_file_path = os.path.join(java_files_directory, filename)
        if os.path.exists(java_file_path):
            # Se o arquivo existir, retorna-o como uma resposta HTTP
            with open(java_file_path, 'rb') as file:
                response = HttpResponse(file)
                response['Content-Type'] = 'application/octet-stream'
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
                return response
        else:
            # Se o arquivo não existir, retorna uma resposta 404
            return Response(status=status.HTTP_404_NOT_FOUND)
