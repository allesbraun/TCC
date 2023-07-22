import os

from django.shortcuts import render
from rest_framework import viewsets

from data.models import Code
from data.serializer import CodeSerializer


class CodesViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
#     lookup_field = 'pk'

# class FileViewSet():
#     .objects.filter(student_id=self.kwargs['pk'])


# def upload_code(request):
#     if request.method == 'POST' and request.FILES['file']:
#         uploaded_file = request.FILES['file']
#         file_name = uploaded_file.name
#         title = os.path.splitext(file_name)[0]
#         language = 'Java'
#         content = uploaded_file.read().decode('utf-8')

#         code = Code(title=title, language=language, content=content, file=uploaded_file)
#         code.save()

#         return render(request, 'upload_success.html', {'code': code})
#     else:
#         return render(request, 'upload_form.html')
