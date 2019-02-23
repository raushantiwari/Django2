from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='bloghome'),
    # path('all/', views.top_five, name='blogtop_five'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
