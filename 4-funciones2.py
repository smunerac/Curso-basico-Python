nombre = "Santiago"

#Funcion con parametros de entrada, y parametro "puesto", con valor por defecto
def informacion(nombre , puesto="desempleado"):  
    print(f" Soy {nombre} y soy {puesto}")
#Parametros entre {}, para ser impreso SU VALOR
#(f) inicial para leer datos DENTRO de las "" de la funcion print


informacion(nombre , "programador")
informacion("Juan" , "diseñador")
informacion("Pedro" )
