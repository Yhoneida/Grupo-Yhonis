def diccionarioo(diccionario, clave):
    valor = diccionario.get(clave, None)
    if valor is not None:
        tipo_dato = type(valor)
        return valor, tipo_dato
    else:
        return "Clave no encontrada en el diccionario."
    


diccionario_jose = {
    'programa': 'ADSO',
    'telefono': 301452689,
    'modalidad': 'virtual',
    'altura': 1.47,
    'casado' : True
}


clave_buscada = input("señor escriba la clave que quiere buscar ")
resultado = diccionarioo(diccionario_jose, clave_buscada)
if resultado == "Clave no encontrada en el diccionario.":
    print(resultado)
else:
    valor, tipo = resultado
    print(f"Valor: {valor}, Tipo de dato: {tipo}")




def dicico (dicc, clave):
    valor = dicc
