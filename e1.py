adf={
    'estados':{ 'a', 'b', 'c', 'd'},
    'alfabeto':{ '0', '1'} ,
    'transiciones': { 
                    'a':{ '0': 'b', '1': 'a'},
                    'b':{ '0': 'b', '1': 'c'},
                    'c':{ '0': 'd', '1': 'c'},
                    'd':{ '0': 'd', '1': 'c'}
    },
    'estado_inicial': 'a',
    'estados_finales': { 'd'}
}
def evaluacion(adf, palabra):
    estado_actual= adf[ 'estado_inicial']
    for simbolo in palabra:
        if simbolo not in adf[ 'alfabeto']:
            print(f"Alguno de los caracteres{ simbolo}, no pertenece al alfabeto")
            return False
        estado_actual= adf[ 'transiciones'][estado_actual][simbolo]
        print(f"{ simbolo} > { estado_actual}")
    return estado_actual in adf[ 'estados_finales']

cadena="1100110"
print(f"Procesando la cadena { cadena}")
resultado=evaluacion(adf, cadena)
print(f"Se acepto?, { resultado}")