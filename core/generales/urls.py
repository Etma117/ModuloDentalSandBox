from django.urls import path, include
from .views import home, exit, recover_password, set_new_password, verify_security_answers


from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', home.as_view(), name="home"),

    path('logout/', exit, name='exit'),
    path('recover-password/', recover_password, name='recover_password'),
    path('verify-security-answers/', verify_security_answers, name='verify_security_answers'),
    path('set-new-password/', set_new_password, name='set_new_password'),

   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)