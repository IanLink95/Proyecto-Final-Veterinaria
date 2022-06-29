from asyncio.windows_events import NULL
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.template import loader
from registroanimales.models import Familia,Mascota,Consulta,Publicacion,Avatar
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from registroanimales.forms import FamiliaFormulario,MascotaFormulario,UserRegisterForm,UserEditForm,AvatarFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from datetime import datetime

#1. Secciones principales de la página
def home(request):
    plantilla=loader.get_template('registroanimales/home.html')
    documento=plantilla.render()
    return HttpResponse(documento)

def account(request):
    usuario=request.user.username
    id=request.user.id
    avatares=Avatar.objects.filter(user=id).first()
    return render(request,"registroanimales/account.html",{"usuario":usuario,"ruta":avatares})

def comunidad(request):
    plantilla=loader.get_template('registroanimales/comunidad.html')
    documento=plantilla.render()
    return HttpResponse(documento)

def contacto(request):
    plantilla=loader.get_template('registroanimales/contacto.html')
    documento=plantilla.render()
    return HttpResponse(documento)

def servicios(request):
    plantilla=loader.get_template('registroanimales/servicios.html')
    documento=plantilla.render()
    return HttpResponse(documento)

def tuMascota(request):
    return render(request,'registroanimales/tuMascota.html')

#2. Lo relativo a registrar y ver información de tu mascota.
@login_required
def familiaFormulario(request):
    if request.method == 'POST':
        miFormulario=FamiliaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            usuario = request.user
            familia=Familia(id_familia=informacion["id_familia"],apellido=informacion["apellido"],nombre_responsable=informacion["nombre_responsable"],mail=informacion["mail"],user=usuario)
            familia.save()
            return render(request,'registroanimales/familiaCreada.html') 
    else:
        miFormulario=FamiliaFormulario()
    return render(request,'registroanimales/familiaFormulario.html',{"miFormulario":miFormulario})

@login_required
def mascotaFormulario(request):
    if request.method == 'POST':
        miFormulario=MascotaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            usuario = request.user
            mascota=Mascota(id_mascota=informacion["id_mascota"],nombre=informacion["nombre"],fecha_nacimiento=informacion["fecha_nacimiento"],peso_kg=informacion["peso_kg"],altura_mts=informacion["altura_mts"],user=usuario)
            mascota.save()
            return render(request,'registroanimales/mascotaCreada.html') 
    else:
        miFormulario=MascotaFormulario()
    return render(request,'registroanimales/mascotaFormulario.html',{"miFormulario":miFormulario})

@login_required
def buscar(request):
    if request.GET['id_mascota']:
        a= request.GET['id_mascota']
        mascotas=Mascota.objects.filter(id_mascota=a).filter(user=request.user.id)
        consultas=Consulta.objects.filter(id_mascota=a).filter(user=request.user.id)
        z=len(mascotas)
        def vacio():
            if z == 1 :
                return("")
            else:
                return ("Dicho ID de mascota no está asociado a su usuario. Si cree que es un error, por favor comunicarse con nosotros para corregirlo.")
        return render(request,'registroanimales/resultadosBusqueda.html',{'id_mascota':a,'mascotas':mascotas,'consultas':consultas,'vacio':vacio(),'z':z})
    else:
        respuesta="No se ha ingresado un ID correcto"
    return HttpResponse(respuesta)

@login_required
def resultadosBusqueda(request):
    plantilla=loader.get_template('registroanimales/resultadosBusqueda.html')
    documento=plantilla.render()
    return HttpResponse(documento)

#3. Lo relativo a registrarse, iniciar sesión y modificar información como usuario.
def login_request(request):

    if request.method == "POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            usuario= form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')
            user= authenticate(username=usuario,password=contra)
            id=request.user.id
            avatares=Avatar.objects.filter(user=id)
            avataresprimero=avatares.first()
            if user is not None:
                login(request,user)
                return render(request,"registroanimales/account.html",{"usuario":usuario,"ruta":avataresprimero})
            else:
                return render(request,"registroanimales/account.html",{"mensaje2":"Error, datos incorrectos"})
        else:
            return render(request,"registroanimales/account.html",{"mensaje2":"Error, formulario erróneo"})
    form=AuthenticationForm()
    return render(request,"registroanimales/login.html",{"form":form})

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request,"registroanimales/usuarioCreado.html",{"mensaje":"Su usuario ha sido creado con éxito."})
    else:
        form=UserRegisterForm()
    return render(request,"registroanimales/signup.html",{"form":form})

@login_required
def profile(request):
    usuario=request.user
    if request.method == "POST":
        miFormulario= UserEditForm(request.POST,instance=usuario)
        if miFormulario.is_valid:
            informacion=miFormulario
            usuario.email= informacion['email']
            usuario.password1= informacion['password1']
            usuario.password2= informacion['password2']
            usuario.save()
            return render (request,"registroanimales/informacionUserCambiada.html")
    else:
        miFormulario= UserEditForm()
    return render(request,"registroanimales/profile.html",{"miFormulario":miFormulario,"usuario":usuario})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miFormulario=AvatarFormulario(request.POST,request.FILES)
        if miFormulario.is_valid():
            u= User.objects.get(username=request.user)
            avatar=Avatar(user=u,imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()
            usuario=request.user.username
            id=request.user.id
            avatares=Avatar.objects.filter(user=id).first()
            return render(request,"registroanimales/account.html",{"usuario":usuario,"ruta":avatares})
    else:
        miFormulario=AvatarFormulario()
    return render(request,"registroanimales/agregarAvatar.html",{"miFormulario":miFormulario})

#4. Lo relativo a la comunidad (publicaciones de mascotas en adopción)

class PublicacionList(ListView):
    model=Publicacion
    template_name= 'registroanimales/publicaciones_list.html'

class PublicacionDetalle(DetailView):
    model=Publicacion
    template_name='registroanimales/publicacion_detalle.html'

class PublicacionCreacion(LoginRequiredMixin,CreateView):
    model=Publicacion
    success_url= '/registroanimales/publicacion/list'
    fields= ['tema','publicacion']

    def form_valid(self,form):
        user=User.objects.get(username=self.request.user)
        fecha=datetime.now()
        Publicacion.objects.create(tema=self.request.POST['tema'],publicacion=self.request.POST['publicacion'],autor=user,fecha_publicacion=fecha)
        return redirect(self.success_url)

class PublicacionEdicion(LoginRequiredMixin,UpdateView):
    model=Publicacion
    success_url= '/registroanimales/publicacion/list'
    fields= ['tema','publicacion']

    def form_valid(self,form):
        user=User.objects.get(username=self.request.user)
        if form.instance.autor == user:
            return super().form_valid(form)
        else:
            return redirect('/registroanimales/errorPublicacion')


class PublicacionEliminacion(LoginRequiredMixin,DeleteView):
    model=Publicacion
    success_url= '/registroanimales/publicacion/list'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.autor != self.request.user:
            return redirect('/registroanimales/errorPublicacion')
        return super().post(request, *args, **kwargs)

def errorPublicacion(request):
    plantilla=loader.get_template('registroanimales/errorPublicacion.html')
    documento=plantilla.render()
    return HttpResponse(documento)

def buscarPublicacion(request):
    if request.GET['autor']:
        a= request.GET['autor']
        publicaciones=Publicacion.objects.filter(autor=a)
        avatares=Avatar.objects.filter(user=a)
        def username():
            u=0
            for x in publicaciones:
                u= x.autor
                break;
            return u
        return render(request,'registroanimales/resultadosBusquedaPublicacion.html',{'autor':a,'publicaciones':publicaciones,'username':username(),"url":avatares[0].imagen.url})
    else:
        respuesta="No se ha ingresado un usuario correcto"
    return HttpResponse(respuesta)

def resultadosBusquedaPublicacion(request):
    plantilla=loader.get_template('registroanimales/resultadosBusquedaPublicacion.html')
    documento=plantilla.render()
    return HttpResponse(documento)