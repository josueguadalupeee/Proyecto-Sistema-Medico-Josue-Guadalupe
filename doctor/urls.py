"""
URL configuration for doctor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from aplication.core.views.signup import home,signup,tasks,signout,signin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('signup/',signup,name='signup'),
    path('tasks/',tasks,name='tasks'),
    path('logout/',signout,name='logout'),
    path('signin/',signin,name='signin'),
    path('', include('aplication.core.urls',namespace='core')),
    path('', include('aplication.attention.urls', namespace='attention')), 
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # configuracion imagenes