def divide_elementos_de_lista(lista, divisor):
    try:
        return [1/divisor for i in lista]
    except ZeroDivisionError as e:
        return lista


lista = list(range(10))
divisor =0

print(divide_elementos_de_lista(lista, divisor))