class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre   #atributo
        self.categoria = categoria
        self.precio = precio  #Default: Public,  PROTECTED, PRIVATE

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')


#GETTERS Y SETTERS  - Get=Obtiene un valor, Set=Agrega un valor 

def get_precio (self):
    return self.precio

def set_precio(self, precio):
    self.precio= precio

#Crear una clase hijo de Restaurant

class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, alberca):
        super().__init__(nombre, categoria, precio)
        self.alberca = alberca

    #Reescribir un metodo (Debe llamarse igual)
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Alberca: {self.alberca}')


    #Agregar un metodo que solo exista en hotel
    def get_alberca(self):
        return self.alberca    



hotel = Hotel('Hotel POO', '5 Estrellas', 200, 'Si')
hotel.mostrar_informacion()
alberca = hotel.get_alberca()
print(alberca)
