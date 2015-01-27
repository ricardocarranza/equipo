from django.contrib import admin
from models import Usuario, Estado, TipoEqui, Procesador, FichaTecnica, Ram, Disco, Unidad, Video, Teclado, Mouse

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellido', 'puesto', 'mail', 'telefono',)

class ProcesadorAdmin(admin.ModelAdmin):
	list_display = ('tipo', 'modelo', 'velocidad')

class RamAdmin(admin.ModelAdmin):
	list_display = ('marca', 'velocidad', 'buz', 'capacidad')

class DiscoAdmin(admin.ModelAdmin):
	list_display = ('marca', 'capacidad')

class UnidadAdmin(admin.ModelAdmin):
	list_display = ('tipo', 'marca', 'velocidad')

class VideoAdmin(admin.ModelAdmin):
	list_display = ('marca', 'modelo', 'velocidad')





class FichaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'usuario', 'estado')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Estado)
admin.site.register(TipoEqui)
admin.site.register(Procesador, ProcesadorAdmin)
admin.site.register(Ram, RamAdmin)
admin.site.register(Disco, DiscoAdmin)
admin.site.register(Unidad, UnidadAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Teclado)
admin.site.register(Mouse)





admin.site.register(FichaTecnica, FichaAdmin)