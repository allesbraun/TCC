
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from rest_framework import routers

from data.views import CodesViewSet

router = routers.DefaultRouter()
router.register('codes', CodesViewSet, basename='Codes')

urlpatterns = [
    # path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    # path('general-control/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    # path('codes/', CodesViewSet.as_view({'get': 'list'}), name='code-list'),
    # path('codes/<int:pk>/', CodesViewSet.as_view()),
    #re_path(r'^java_files/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]