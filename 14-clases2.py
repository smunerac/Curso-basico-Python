class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre   #atributo
        self.categoria = categoria
        self.__precio = precio  #Default: Public,  PROTECTED, PRIVATE

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}')



#Instanciar la clase
restaurant = Restaurant('Pizzeria Mexico', 'Comida Italiana', 50)
restaurant.__precio =80  #No es posible modificarlo, por ser PRIVATE__
restaurant.mostrar_informacion()

restaurant2 = Restaurant('Hamburguesas Python', 'Comida casual', 20)
restaurant2.__precio=40
restaurant2.mostrar_informacion()






