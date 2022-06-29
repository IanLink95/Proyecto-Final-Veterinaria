from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import about,pages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',about,name="about"),
    path('pages/',pages,name="pages"),
    path('registroanimales/',include('registroanimales.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
