# Diferencia entre funciones y metodos

nombre = "pedro"

#Funcion
def mostrar_nombre (nombre):
    print(f"Hola {nombre}")

mostrar_nombre(nombre)    

#Metodo
print(  nombre.upper()   )     #Metodo UPPER==>MAYUSCULAS se le aplica al argumento "nombre"
print(  nombre.title()   )     #Metodo Title==>inicial en mayuscula se le aplia al argumento antes del .

#Retos de practica 
#1
def bienvenida_simple():
    print("Buenos dias, bienvenidos")

bienvenida_simple()
#2
nombre_usuario = "Juana"

def bienvenida(usuario):
    print(f"Buenos dias, bienvenid@ {nombre_usuario}")

bienvenida(nombre_usuario)
#3
actividad = "Conducir"
def ultima_actividad(actividad):
    print(actividad)

ultima_actividad(actividad)
