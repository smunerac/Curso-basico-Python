#Revisar si una condicion es mayor a 
balance = 500

if balance > 0:
    print('Puedes pagar')
else:
    print('No tienes saldo')


#Likes
likes=200
if likes >=200:
    print('Exelente, 200 likes')
else:
    print('Casi llegas a los 200')

# if con texto
lenguaje = 'Python'    
if lenguaje== 'Python':
    print('Excelente desicion')

#Negacion de un 'if'
if not lenguaje=='Python':
    print('Exelente desicion')

#Evaluar un Booleano
usuario_autenticado = True

if usuario_autenticado:  #Si la comparacion es True, no se requiere escribir necesariamente
    print('Acceso al sistema')
else:
    print('Debes iniciar sesion')

#Evaluar un elemento de una lista
lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript', 'PHP']
if 'PHP' in lenguajes:
    print('PHP Si existe')
else:
    print('No, no esta en la lista')

#if anidados
usuario_autenticado= True
usuario_admin = True

if usuario_autenticado:
    if usuario_admin:
        print('ACCESO TOTAL')
    else:
        print('Acceso al sistema')
    
else:
    print('Debes iniciar sesion')







