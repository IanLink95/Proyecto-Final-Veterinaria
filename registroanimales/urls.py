from cgitb import html
from django.urls import path
from registroanimales.views import buscarPublicacion, home,account,comunidad,contacto,servicios,familiaFormulario,resultadosBusqueda,tuMascota,buscar,login_request,signup,profile,mascotaFormulario,PublicacionCreacion,PublicacionDetalle,PublicacionEdicion,PublicacionEliminacion,PublicacionList,resultadosBusquedaPublicacion,agregarAvatar,errorPublicacion
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',home,name='home'),
    path('account/',account,name="account"),
    path('comunidad/',comunidad,name="comunidad"),
    path('contacto/',contacto,name="contacto"),
    path('servicios/',servicios,name="servicios"),
    path('resultadosBusqueda/',resultadosBusqueda,name="resultadosBusqueda"),
    path('familiaFormulario/',familiaFormulario,name='familiaFormulario'),
    path('mascotaFormulario/',mascotaFormulario,name='mascotaFormulario'),
    path('tuMascota/',tuMascota,name='tuMascota'),
    path('buscar/',buscar,name='buscar'),
    path('account/login',login_request,name='login'),
    path('account/signup',signup,name='signup'),
    path('account/logout',LogoutView.as_view(template_name='registroanimales/logout.html'),name='logout'),
    path('account/profile',profile,name="profile"),
    path('publicacion/list',PublicacionList.as_view(),name='List'),
    path('publicacion/<pk>',PublicacionDetalle.as_view(),name='Detail'),
    path('publicacion/nuevo/',PublicacionCreacion.as_view(),name='New'),
    path('publicacion/edicion/<pk>',PublicacionEdicion.as_view(),name='Edit'),
    path('publicacion/borrar/<pk>',PublicacionEliminacion.as_view(),name='Delete'),
    path('buscarPublicacion/',buscarPublicacion,name='buscarPublicacion'),
    path('resultadosBusquedaPublicacion/',resultadosBusquedaPublicacion,name="resultadosBusquedaPublicacion"),
    path('agregarAvatar',agregarAvatar,name="AgregarAvatar"),
    path('errorPublicacion',errorPublicacion,name='errorPublicacion'),

]
