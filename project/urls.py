"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from conoce_lugares.views import ( index, PostDetalle, PostListar, PostCrear, PostBorrar, PostActualizar, UserSignUp, UserLogin, UserLogout, MensajeDetalle, MensajeListar, MensajeCrear, MensajeBorrar,
                               UserActualizar, AvatarActualizar)
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conoce-lugares/', index, name="conoce-lugares-index"),
    path('conoce-lugares/<int:pk>/detalle/', PostDetalle.as_view(), name="conoce-lugares-detalle"),
    path('conoce-lugares/listar/', PostListar.as_view(), name="conoce-lugares-listar"),
    path('conoce-lugares/crear/', staff_member_required(PostCrear.as_view()), name="conoce-lugares-crear"),
    path('conoce-lugares/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="conoce-lugares-borrar"),
    path('conoce-lugares/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="conoce-lugares-actualizar"),
    path('conoce-lugares/signup/', UserSignUp.as_view(), name ="conoce-lugares-signup"),
    path('conoce-lugares/login/', UserLogin.as_view(), name= "conoce-lugares-login"),
    path('conoce-lugares/logout/', UserLogout.as_view(), name="conoce-lugares-logout"),
    path('conoce-lugares/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="conoce-lugares-mensajes-detalle"),
    path('conoce-lugares/mensajes/listar/', MensajeListar.as_view(), name="conoce-lugares-mensajes-listar"),
    path('conoce-lugares/mensajes/crear/', MensajeCrear.as_view(), name="conoce-lugares-mensajes-crear"),
    path('conoce-lugares/mensajes/<int:pk>/borrar/', MensajeBorrar.as_view(), name="conoce-lugares-mensajes-borrar"),
    path('conoce-lugares/about', TemplateView.as_view(template_name='conoce_lugares/about.html'), name="conoce-lugares-about"),
    path('conoce-lugares/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="conoce-lugares-users-actualizar"),
    path('conoce-lugares/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="conoce-lugares-avatars-actualizar"),
    ]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)