from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.index, name='blog_home'),
                  path('<int:blog_id>/', views.detail, name='blog_detail'),
                  path('create/', views.create_blog, name='create_blog'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
