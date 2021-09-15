﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """
    Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
    los mismos.
    """
    catalog = {'artistas': None,
               'obras': None}

    catalog['artistas'] = lt.newList()
    catalog['obras'] = lt.newList('SINGLE_LINKED')
                                
    

    return catalog

# Funciones para agregar informacion al catalogo
def addArtist(catalog, artistas):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['artistas'], artistas)
    
    

def addObras(catalog, obras):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['obras'], obras)
 
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def cmpfunction(uno,dos):
    if int(uno["BeginDate"])> int(dos["BeginDate"]):
        r=True
    else:
        r=False
    return r

#Como curador del museo quiero listar cronológicamente los artistas que nacieron en un rango de años.
def artistasCronologicamente(anho_inicio, anho_final,catalog):
    ordenar=sa.sort(catalog["artistas"],cmpfunction)
    lista=lt.newList("ARAY_LIST")
    for i in range(1,lt.size(lista)):
        anho=lt.getElement(catalog["artistas"],i)
        print(anho)
        if anho ["BeginDate"]>= anho_inicio and anho["BeginDate"]<=anho_final:
            lt.addLast(lista,anho)
    return lista








#Como curador del museo quiero listar cronológicamente las obras adquiridas por el museo en un rango de fechas.



#Como investigador del museo quiero clasificar las obras de un artista de acuerdo a la técnica (medios) utilizada para su creación.
