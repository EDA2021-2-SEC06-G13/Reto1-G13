"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar artistas cronologicamente en un rango de años")
    print("3- Listar cronologicamente las adquisiciones del museo en un rango de años")
    print("4- Clasificar las obras de un artista de acuerdo a la tecnica")
    print("5- Clasificar las obras por la nacionalidad de su creador")
    print("6- Calcular el costo para transportar todas las obras de un departamento")
    print("7- Proponer una nueva exposicion en el museo")

catalog = None

def initCatalog():
    """
    Inicializa el catalogo 
    """
    return controller.initCatalog()
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog=controller.initCatalog()
        controller.loadData(catalog)




    elif int(inputs[0]) == 2:
        anho_inicial=input("Ingrese el año inicial: ")
        anho_final=input("Ingrese el año final: ")
        r=controller.requerimiento_1(anho_inicial,anho_final,catalog)
        for i in range(1,lt.size(r)):
            res=lt.getElement(r,i)
            print(res)
        
        pass
    elif int(inputs[0]) == 3:
        input("Ingrese el rango de años: ")
        pass
    elif int(inputs[0]) == 4:
        input("Sobre que tecnica desea clasificar al artista:  ")
        pass
    elif int(inputs[0]) == 5:
        input("Sobre que nacionalidad desea clasificar las obras:  ")
        pass
    elif int(inputs[0]) == 6:
        input("Ingrese el departamento origen: ")
        input("Ingrese el departamento destino: ")
        pass
    elif int(inputs[0]) == 7:
        input("Que exposicion desea proponer:  ")
        pass
    else:
        sys.exit(0)
sys.exit(0)
