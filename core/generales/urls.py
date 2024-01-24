from django.urls import path, include
from .views import home, exit


from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', home.as_view(), name="home"),

    path('logout/', exit, name='exit'),

   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)