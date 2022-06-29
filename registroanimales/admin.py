from django.contrib import admin
from registroanimales.models import Tipoanimal,Raza,Familia,Mascota,Consulta,Publicacion,Avatar
from django.contrib.auth import get_user_model

admin.site.register(Tipoanimal)
admin.site.register(Raza)
admin.site.register(Familia)
admin.site.register(Mascota)
admin.site.register(Consulta)
admin.site.register(Publicacion)
admin.site.register(Avatar)

#class PublicacionAdmin(admin.ModelAdmin):
#    def get_queryset(self,request):
#        qs=super(PublicacionAdmin,self).get_queryset(request)
#        if request.user.is_superuser:
#            return qs
#        return qs.filter(author=request.user)
#    def formfield_for_foreignkey(self, db_field, request, **kwargs):
#        if db_field.name=='autor':
#            kwargs['queryset']=get_user_model().objects.filter(username=request.user.username)
#        return super(PublicacionAdmin,self).formfield_for_foreignkey(db_field, request, **kwargs)

#admin.site.register(Publicacion,PublicacionAdmin)
