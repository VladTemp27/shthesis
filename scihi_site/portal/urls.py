from django.conf.urls import url 
from django.contrib.auth import views as auth_views 
 
from . import views 
 
app_name='loadmap' 
 
urlpatterns = [url('login/$', auth_views.login, name='login'), 
              .....] 