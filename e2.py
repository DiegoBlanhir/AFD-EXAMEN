adf={
    'estados':{ '1', '2'},
    'alfabeto':{ 'a', 'b'} ,
    'transiciones': { 
                    '1':{ 'a': '1', 'b': '2'},
                    '2':{ 'a': '2', 'b': '1'}
    },
    'estado_inicial': '1',
    'estados_finales': { '2'}
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

cadena="babb"
print(f"Procesando la cadena { cadena}")
resultado=evaluacion(adf, cadena)
print(f"Se acepto?, { resultado}")