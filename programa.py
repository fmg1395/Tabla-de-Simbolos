class errores(Exception):
    def __init__(self,valor):
        self.valor = valor
    def __str__(self):
        return str(self.valor)

class nodo:
    def __init__(self,nombre,tipo,linea,valor):
        self.nombre = nombre
        self.tipo = tipo
        self.linea = linea
        self.valor = valor
    def __init__(self):
        self.nombre = ''
        self.tipo = ''
        self.linea = ''
        self.valor = ''

class Tabla_Simbolos:
    def __init__(self):
        self.variables={}
        self.funciones={}
    def insert_variable(self,nodo):
        self.variables[nodo.nombre]=nodo

    def insert_funcion(self,nodo):
        self.funciones[nodo.nombre]=nodo

    def lookup_variable(self,nombre):
        return self.variables[nombre]
    
    def lookup_funcion(self,nombre):
        return self.funciones[nombre]
    
    def revisar_archivo(self,ruta):
        archivo = open(ruta,'r')
        cuenta_linea = 0
        for n in range(2):

            linea = archivo.readline()
            cuenta_linea+=1
            Nodo = nodo()
            try:
                if linea.count('='):
                    division = linea.split(' ')
                    while '' in division:
                        division.remove('')
                    if(len(division) != 4):
                        Nodo.nombre = division[0]
                        self.lookup_variable(Nodo.nombre)
                    Nodo.tipo = division[0]
                    Nodo.nombre = division[1]
                    Nodo.valor = division[3]
                    Nodo.valor = Nodo.valor[:len(Nodo.valor)-2]
                    Nodo.linea = cuenta_linea
                    self.insert_variable(Nodo)
            except errores as e:
                fail = open("Errores.txt",'w')
                fail.write("Error "+e.__str__()+" en linea "+str(cuenta_linea)+"\n")
                fail.close()
            except KeyError:
                fail = open("Errores.txt",'w')
                fail.write("Error en linea "+str(cuenta_linea)+"\n")
                fail.close()
        archivo.close()
                


# Tablita = Tabla_Simbolos()
# Tablita.revisar_archivo('Texto.txt')

# print(Tablita.lookup_variable('x').valor)


file = open("prueba.txt",'a')
file.write("Primera linea\n")
file.close()


file = open("prueba.txt",'a')
file.write("Segunda linea\n")
file.close()

print('END MAIN')
    
# archivo = open('Texto.txt','r')
# # diccionario = {}

# linea = archivo.readline()

# variable = nodo()

# if linea.count('='):
#     division = linea.split(' ')
#     variable.tipo = division[0]
#     variable.nombre = division[1]
#     variable.valor = division[3]
#     variable.valor = variable.valor[:len(variable.valor)-2]
    
# archivo.close()

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
# diccionario = {'Hola':1,'Buenas':2,'tardes':3}
# try:
#     print(diccionario['coma'])
# except KeyError:
#     print("Error en el diccionario")








