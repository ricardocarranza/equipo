from django.contrib import admin
from models import Usuario, Estado, TipoEqui, Procesador, FichaTecnica, Ram, Disco, Unidad, Video, Teclado, Mouse, Red, Print, Monitor, Periferico, Sistema, Ofimati, Antiv, Compresor, Pdf, Grabador, Navegador, Otro

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

class RedAdmin(admin.ModelAdmin):
	list_display = ('marca', 'modelo', 'tipo')

class PrintAdmin(admin.ModelAdmin):
	list_display = ('marca', 'modelo', 'tipo')

class MonitorAdmin(admin.ModelAdmin):
	list_display = ('marca', 'tipo', 'tamano')

		


class SistemaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'version')





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
admin.site.register(Red, RedAdmin)
admin.site.register(Print, PrintAdmin)
admin.site.register(Monitor, MonitorAdmin)
admin.site.register(Periferico)
admin.site.register(Sistema, SistemaAdmin)
admin.site.register(Ofimati)
admin.site.register(Antiv)
admin.site.register(Compresor)
admin.site.register(Pdf)
admin.site.register(Grabador)
admin.site.register(Navegador)
admin.site.register(Otro)


admin.site.register(FichaTecnica, FichaAdmin)