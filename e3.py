adf={
    'estados':{ 'a', 'b', 'c'},
    'alfabeto':{ '0', '1'} ,
    'transiciones': { 
                    'a':{ '0': 'a', '1': 'b'},
                    'b':{ '0': 'a', '1': 'c'},
                    'c':{ '0': 'c', '1': 'c'}
    },
    'estado_inicial': 'a',
    'estados_finales': { 'a', 'b'}
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

cadena="110010"
print(f"Procesando la cadena { cadena}")
resultado=evaluacion(adf, cadena)
print(f"Se acepto?, { resultado}")