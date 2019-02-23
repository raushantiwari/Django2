from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.index, name='blog_home'),
                  path('<int:blog_id>/', views.detail, name='blog_detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
