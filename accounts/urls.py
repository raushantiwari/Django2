from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('login/', views.login, name='login'),
                  path('signup/', views.signup, name='signup'),
                  path('forgot/password/', views.forgot_pass, name='forgot_pass'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
