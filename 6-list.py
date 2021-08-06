lenguajes = ["Python", "Kotlin", "Java", "JavaScript"]
print(lenguajes)

#Los arrays (lists) comienzan en la posicion 0
print(lenguajes[0])   #Python

lenguajes.sort() #Ordena alfabeticamente los elementos 
print(lenguajes)

# Acceder a un elemento dentro de un texto
aprendiendo = f"Estoy aprendiendo {lenguajes[3]}"
print(aprendiendo)

#Modificar valores de un arreglo, o list
lenguajes[2] = "PHP"
print(lenguajes) 

#Agregar elementos a un arreglo o list
lenguajes.append("Ruby")
print(lenguajes)

#Eliminar de un arreglo o list
del lenguajes[1]
print(lenguajes)

#Eliminar de un arreglo o list
lenguajes.pop()  #Elimina el ultimo elemento (del final del arreglo)
print(lenguajes)

#Eliminar una posicion en particular con "pop"
lenguajes.pop(0)
print(lenguajes)

#Eliminar por el "Nombre del dato" 
lenguajes.remove("PHP")
print(lenguajes)


