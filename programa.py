# archivo = open('Texto.txt','r')
# diccionario = {}

# for linea in archivo.readlines():
#     if linea.count('int'):
#         posicion = linea.split(' ').index('int')
#         tipo = linea.split(' ')[posicion]
#         variable = linea.split(' ')[posicion+1]
#         diccionario[variable] = tipo
#     if linea.count('float'):
#         posicion = linea.split(' ').index('float')
#         tipo = linea.split(' ')[posicion]
#         variable = linea.split(' ')[posicion+1]
#         diccionario[variable] = tipo
#     if linea.count('string'): 
#         posicion = linea.split(' ').index('string')
#         tipo = linea.split(' ')[posicion]
#         variable = linea.split(' ')[posicion+1]
#         diccionario[variable] = tipo
# archivo.close()

# print(diccionario)
diccionario = {'Hola':1,'Buenas':2,'tardes':3}
try:
    print(diccionario['coma'])
except KeyError:
    print("Error en el diccionario")


print('Fin')





