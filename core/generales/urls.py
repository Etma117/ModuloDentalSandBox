from django.urls import path, include
from .views import home, exit, homePageView, homePageViewChildren, login_redirect, recover_password, set_new_password, templeteDenegado, verify_security_answers


from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    
    path('menu/', home.as_view(), name="home"),
    path('', homePageView.as_view(), name="homePage"),
    path('children/', homePageViewChildren.as_view(), name="homePageViewChildren"),

    
    path('accounts/', include('allauth.urls')),

    path('logout/', exit, name='exit'),
    path('recover-password/', recover_password, name='recover_password'),
    path('verify-security-answers/', verify_security_answers, name='verify_security_answers'),
    path('set-new-password/', set_new_password, name='set_new_password'),
    path('denegado/', templeteDenegado.as_view(), name="denegado"),
    path('login/redirect/', login_redirect, name='login_redirect'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)