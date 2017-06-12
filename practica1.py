import sys

class Nodo:
	def __init__(self, usuario, password):
		self.usuario=usuario
		self.password=password
		self.siguiente=None
		self.anterior=None

class Lista_Usuarios:
	bandera=False

	def __init__(self):
		self.primero=None
		self.ultimo=None

	def vacia(self):
		if self.primero == None:
			return True
		else:
			return False

	def agregar_usuario(self, usuario, password):
		if self.vacia():
			self.primero=self.ultimo=Nodo(usuario, password)
		else:
			aux=self.ultimo
			self.ultimo=aux.siguiente=Nodo(usuario, password)
			self.ultimo.anterior=aux
		self.__enlazar()
		


	def __enlazar(self):
		self.primero.anterior=self.ultimo
		self.ultimo.siguiente=self.primero

	def inicio_fin(self):
		print "imprimiendo de inicio a fin"
		aux=self.primero 
		while aux:
			print aux.usuario + "-->",
			aux=aux.siguiente
			
			if aux==self.primero:
				print aux.usuario
				break


	def fin_inicio(self):
		print "imprimiendo de fin a inicio"
		aux=self.ultimo
		while aux:
			print aux.usuario + "-->",
			aux=aux.anterior
			if aux==self.ultimo:
				print aux.usuario
				break

	def verificar_usuario(self, usuario, password):
		usuario_activo=0
		aux=self.primero 
		while aux:
			if aux.usuario==usuario and aux.password==password:
				
				return True

			else:
				
				aux=aux.siguiente

			if aux==self.primero:
				
				return False

class cola_operaciones:

	def __init__(self):
		self.cabeza=None
		self.cola=None

	def leer_archivo(self,archivo):
		archivo='"'+archivo+'"'
		try:
			documento=open(archivo,"r")
			for linea in documento.readlines():
				print linea
		except:
			print "archivo no valido"
			menu_sistema()

				


def menu_principal():
	print "Practica 1 \nSeleccione una opcion: \n1. Crear Usuario \n2. Ingresar al sistema \n3. Salir del Programa"
	opcion = raw_input()

	if opcion == "1":	
		
		agregar_usuario()

	elif opcion=="2":
		
		ingresar_sistema()

	elif opcion=="3":

		sys.exit()

	else:
		print "Opcion no valida, ingrese una opcion valida"
		menu_principal()


def agregar_usuario():
	print "ingrese nombre de usuario:"
	nombre= raw_input ()
	print "ingrese contrasena:"
	password= raw_input ()
	lista.agregar_usuario(nombre, password)
	menu_principal()

def ingresar_sistema():
	print "ingrese nombre de usuario:"
	nombre= raw_input ()
	print "ingrese contrasena:"
	password= raw_input ()

	bandera=lista.verificar_usuario(nombre, password)
	if bandera:
		menu_sistema()

	else:
		print "usuario y contrasena no validos"
		menu_principal()

def menu_sistema():
	print "Seleccione una opcion: \n1. Leer Archivo \n2. Resolver Operaciones \n3. Operar la Matriz \n4. Mostrar Usuarios \n5. Mostrar Cola \n6. Cerrar Sesion"
	opcion = raw_input()

	if opcion == "1":
		archivo="C:\Users\Renan\Desktop\prueba.txt"
		cola.leer_archivo(archivo)
		lista.bandera=True
		menu_sistema()

	elif opcion=="2":
		if lista.bandera:
			menu_resolver()
		else:
			print "no se ha cargado ningun archivo"	
			menu_sistema()

	elif opcion=="3":

		if lista.bandera==True:
			menu_matriz()
		else:
			print "no se ha cargado ningun archivo"
			menu_sistema()	

	elif opcion=="4":

		lista.inicio_fin()
		lista.fin_inicio()
		menu_sistema()

	elif opcion=="5":

		menu_sistema()

	elif opcion=="6":

		menu_principal()

	else:
		print "Opcion no valida, ingrese una opcion valida"
		menu_sistema()

def menu_resolver():
	print "Seleccione una opcion: \n1. Operar Siguiente \n2. Regresar"
	opcion = raw_input()

	if opcion == "1":	
		
		menu_resolver()

	elif opcion=="2":
		
		menu_sistema()

	else:
		
		print "Opcion no valida, ingrese una opcion valida"
		menu_resolver()

def menu_matriz():
	print "Seleccione una opcion: \n1. Ingresar Dato \n2. Operar Transpuesta \n3. Mostrar Matriz Original \n4. Mostrar Matriz Transpuesta \n5. Regresar"
	opcion = raw_input()

	if opcion == "1":	
		
		ingresar_dato()
		menu_matriz()

	elif opcion=="2":
		
		menu_matriz()

	elif opcion=="3":

		menu_matriz()

	elif opcion=="4":

		menu_matriz()

	elif opcion=="5":

		menu_sistema()

	else:
		print "Opcion no valida, ingrese una opcion valida"
		menu_matriz()

def ingresar_dato():
	print "Ingresar valor de X:"
	posx = raw_input()
	print "Ingresar valor de Y:"
	posy = raw_input()
	print "Ingresar valor a guardar:"
	valor = raw_input()
bandera=True
lista =Lista_Usuarios()
cola=cola_operaciones()
menu_principal()

