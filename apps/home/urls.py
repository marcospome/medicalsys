from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.IndexView.as_view()),
    path('informacion', views.InfoView.as_view()),
    path('especialidades', views.especialiadadListView.as_view()),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'),name='Login'),


]

if settings.DEBUG:
    from django.conf.urls.static import static
        #le decimos que accediendo a la URLPATTERNS si alguien quiere entrar a ver al fichero de turno, que lo pueda ver
        #importamos desde settings los archivos statics, le pasamos el docu root, donde debe ir abuscarlos
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)