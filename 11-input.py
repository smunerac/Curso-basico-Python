#nombre = input ('Cual es tu nombre ? \r\n' )  #  \r\n = Salto de linea en consola

#print(f' Hola {nombre}')

# Leer datos que seran numeros
edad = input( 'Cual es tu edad? \r\n')

# Convertir edad (String) a int
edad = int(edad)

if edad >= 18:
    print('Ya puedes votar')
else:
    print('Aun no puedes votar')

# Mezclarlo con operadores
numero = input('Agrega un numero y te dire si es par o impar \r\n')
numero = int (numero)

if numero%2 == 0 :
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')

# Reto, Examen de 3 preguntas, SI o NO
calificacion= int(0)

pregunta1 = input( 'Estamos en el año 1998 ? Si o No ? \r\n')
if pregunta1=='No':
    calificacion+=1
elif pregunta1=='Si':
    calificacion=calificacion
else:
    print('Respuesta invalida \r\n')

pregunta2 = input( 'Este es un curso de Python ? Si o No? \r\n')
if pregunta2=='Si':
    calificacion+=1
elif pregunta2== 'No':
    calificacion=calificacion
else:
    print('Respuesta invalida')

pregunta3 = input( 'Estas en un computador ? Si o No ? \r\n')
if pregunta3 == 'Si':
    calificacion+=1
elif pregunta3=='No':
    calificacion=calificacion
else:
    print('Respuesta invalida')

print(f'Tu calificacion es {calificacion} aciertos, de 3 preguntas en total \r\n')


