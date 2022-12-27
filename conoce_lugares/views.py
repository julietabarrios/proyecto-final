from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from conoce_lugares.models import Post, Mensaje
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from conoce_lugares.forms import UsuarioForm
from conoce_lugares.models import Avatar
from django.contrib.auth.admin import User

def index(request):
    posts = Post.objects.order_by("-id").all()
    return render(request, "conoce_lugares/index.html", {"posts": posts})

class PostDetalle(DetailView):
    model = Post

class PostListar(ListView):
    model = Post  

class PostCrear(LoginRequiredMixin,CreateView):
    model = Post
    success_url = reverse_lazy("conoce-lugares-listar")
    fields = '__all__'


class PostBorrar(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy("conoce-lugares-listar")

class PostActualizar(LoginRequiredMixin,UpdateView):
    model = Post
    success_url = reverse_lazy("conoce-lugares-listar")
    fields = "__all__"

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('conoce-lugares-listar')

class UserLogin(LoginView):
    next_page = reverse_lazy('conoce-lugares-listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('conoce-lugares-listar')  
    
class MensajeDetalle(DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje  

class MensajeCrear(SuccessMessageMixin, CreateView):
    model = Mensaje
    success_url = reverse_lazy("conoce-lugares-mensajes-crear")
    fields = ['nombre', 'email', 'texto']
    success_message = "Mensaje de contacto enviado!!"

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("conoce-lugares-mensajes-listar")

class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('conoce-lugares-listar')

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('conoce-lugares-listar')
