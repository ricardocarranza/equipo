from django.db import models

# Create your models here.

class Usuario(models.Model):
	nombre    = models.CharField(max_length=140)
	apellido  = models.CharField(max_length=140, blank=True)
	puesto    = models.CharField(max_length=140, blank=True)
	direccion = models.TextField(blank=True)
	mail      = models.EmailField(blank=True)
	telefono  = models.IntegerField(max_length=9, blank=True, null=True)
	#fecha    = models.DateField(auto_now=True, blank=True)

	def __unicode__(self):
		return self.nombre

class Estado(models.Model):
	estado    = models.CharField(max_length=75)

	def __unicode__(self):
		return self.estado

class TipoEqui(models.Model):
	tipo    = models.CharField(max_length=75, verbose_name='Tipo de equipo')

	def __unicode__(self):
		return self.tipo

class Procesador(models.Model):
	tipo      = models.CharField(max_length=75, help_text='Ingrese el nombre del modelo de microprocesador')
	modelo    = models.CharField(max_length=75, blank=True)
	velocidad = models.CharField(max_length=75, blank=True)

	def __unicode__(self):
		return '%s %s %s' % (self.tipo, self.modelo, self.velocidad)

class Ram(models.Model):
	marca     = models.CharField(max_length=75, blank=True)
	velocidad = models.CharField(max_length=75, blank=True)
	buz       = models.CharField(max_length=75, blank=True)
	capacidad = models.CharField(max_length=75, blank=True, help_text='Ingrese la capacidad de la memoria (128MB - 4GB)')

	def __unicode__(self):
		return '%s %s %s %s' % (self.marca, self.buz, self.velocidad, self.capacidad)

class Disco(models.Model):
	marca	  = models.CharField(max_length=75)
	capacidad = models.CharField(max_length=75, blank=True)

	def __unicode__(self):
		return '%s %s' %(self.marca, self.capacidad)

class Unidad(models.Model):
	tipo      = models.CharField(max_length=75)
	marca     = models.CharField(max_length=75, blank=True)
	velocidad = models.CharField(max_length=75, blank=True)

	def __unicode__(self):
		return '%s %s %s' % (self.tipo, self.marca, self.velocidad)

class Video(models.Model):
	marca     = models.CharField(max_length=75, blank=True)
	modelo    = models.CharField(max_length=75, blank=True)
	velocidad = models.CharField(max_length=75, blank=True)

	def __unicode__(self):
		return '%s %s %s' % (self.marca, self.modelo, self.velocidad)

class Teclado(models.Model):
	marca     = models.CharField(max_length=75, blank=True)
	puerto    = models.CharField(max_length=75, blank=True)

	def __unicode__(self):
		return '%s %s' % (self.marca, self.puerto)


class Mouse(models.Model):
	marca     = models.CharField(max_length=75, blank=True)
	puerto    = models.CharField(max_length=75, blank=True)

	def __unicode__(self):
		return '%s %s' % (self.marca, self.puerto)

class Red(models.Model):
	marca     = models.CharField(max_length=75, blank=True)
	modelo    = models.CharField(max_length=75, blank=True)
	tipo      = models.CharField(max_length=75, blank=True)

	def __unicode__(self):
		return '%s %s %s' % (self.marca, self.modelo, self.tipo)

class Print(models.Model):
	marca     = models.CharField(max_length=75, blank=True)
	modelo    = models.CharField(max_length=75, blank=True)
	tipo      = models.CharField(max_length=75, blank=True)

	def __unicode__(self):
		return '%s %s %s' % (self.marca, self.modelo, self.tipo)

class Monitor(models.Model):
	marca   = models.CharField(max_length=75, blank=True)
	tipo    = models.CharField(max_length=75, blank=True)
	tamano  = models.CharField(max_length=75, blank=True, verbose_name='Tamanio')

	def __unicode__(self):
		return '%s %s %s' % (self.marca, self.tipo, self.tamano)

class Periferico(models.Model):
	nombre   = models.CharField(max_length=75, blank=True)
	marca    = models.CharField(max_length=75, blank=True)

	def __unicode__(self):
		return '%s %s' % (self.nombre, self.marca)

##########################################################

class Sistema(models.Model):
	nombre    = models.CharField(max_length=75, blank=True)
	version   = models.CharField(max_length=75, blank=True)

	def __unicode__(self):
		return '%s %s' % (self.nombre, self.version)

class Ofimati(models.Model):
	nombre    = models.CharField(max_length=75, blank=True)
	version   = models.CharField(max_length=75, blank=True)

	def __unicode__(self):
		return '%s %s' % (self.nombre, self.version)

class Antiv(models.Model):
	nombre    = models.CharField(max_length=75, blank=True)
	version   = models.CharField(max_length=75, blank=True)

	def __unicode__(self):
		return '%s %s' % (self.nombre, self.version)


class FichaTecnica(models.Model):
	nombre     = models.CharField(max_length=75, verbose_name='PC')
	usuario    = models.ForeignKey(Usuario, null=True, blank=True)
	estado     = models.ForeignKey(Estado)
	#fecha      = models.DateField(auto_now=True, blank=True)
	tipo       = models.ForeignKey(TipoEqui)
	moderboard = models.CharField(max_length=75, verbose_name='Motherboard')
	procesador = models.ForeignKey(Procesador, blank=True)
	memoria    = models.ForeignKey(Ram, null=True)
	disco      = models.ForeignKey(Disco, blank=True, verbose_name='Disco Duro', null=True)
	unidad     = models.ManyToManyField(Unidad, verbose_name='Unidades Opticas')
	video      = models.ForeignKey(Video, null=True)
	teclado    = models.ForeignKey(Teclado, null=True)
	mouse      = models.ForeignKey(Mouse, null=True)
	red        = models.ForeignKey(Red, null=True)
	impresora  = models.ForeignKey(Print, null=True)
	monitor    = models.ForeignKey(Monitor, null=True)
	periferico = models.ManyToManyField(Periferico)




	sistema    = models.ForeignKey(Sistema, null=True, blank=True, verbose_name='Sistema operativo')
	office     = models.ForeignKey(Ofimati, null=True, blank=True, verbose_name='Sistema ofimatico')
	antivirus  = models.ForeignKey(Antiv, null=True, blank=True, verbose_name='Anti-virus')



