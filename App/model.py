"""
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


from os import replace
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import insertionsort as ins
assert cf
from datetime import date
from time import time
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

    catalog['artistas'] = lt.newList("ARRAY_LIST")
    catalog["obras"] = lt.newList("ARRAY_LIST")
                            
    return catalog

# Funciones para agregar informacion al catalogo
def addArtist(catalog, artistas):
   
    lt.addLast(catalog['artistas'], artistas)
    
    

def addObras(catalog, obras):
    
    lt.addLast(catalog['obras'], obras)
 
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpfunction(uno,dos):
    if int(uno["BeginDate"])> int(dos["BeginDate"]):
        r=True
    else:
        r=False
    return r
def cmpArtWorkByDateAcquired(uno,dos):
    x=str(uno["DateAcquired"])
    y=str(dos["DateAcquired"])
    if x> y:
        r=True
    else:
        r=False
    return r
def compareobras(obra1,obra2):
    if (lt.getElement(obra2, 1) ==obra1):
        return 0
    return -1
def comparepais(pais1, pais2):
    return (lt.getElement(pais1,2) >lt.getElement(pais2,2))
def comparepaises(pais1, pais2):
    if (lt.getElement(pais2, 1) ==pais1):
        return 0
    return -1

# Funciones de ordenamiento



#Como curador del museo quiero listar cronológicamente los artistas que nacieron en un rango de años.
def artistasCronologicamente(anho_inicio, anho_final,catalog):
    ordenar=sa.sort(catalog["artistas"],cmpfunction)
    lista_1234=lt.newList("ARRAY_LIST")
    for i in range(1,lt.size(ordenar)+1):
        anho=lt.getElement(ordenar,i)
        if int(anho["BeginDate"])>= int(anho_inicio) and int(anho["BeginDate"])<=int(anho_final):
            lt.addLast(lista_1234,anho)
    return lista_1234


def adquisicionCronologicamente(fecha_inicial,fecha_final,catalog):
        ordenar=sa.sort(catalog["obras"],cmpArtWorkByDateAcquired)
        lista=lt.newList("ARAY_LIST")
        for i in range(1,lt.size(ordenar)+1):
            anho=lt.getElement(ordenar,i)
            x=str((anho["DateAcquired"]))
            if x>=(fecha_inicial) and x<=(fecha_final):
                lt.addLast(lista,anho)
        return lista

def clasificarobras(nombreArtista,catalog):
    lista=lt.newList('ARRAY_LIST',
                                    cmpfunction=compareobras)
    
    i =1
    while i <= lt.size(catalog["artistas"]):
        artista = lt.getElement(catalog["artistas"], i)
        if nombreArtista==artista["DisplayName"]:
            iden = artista["ConstituentID"]
            
            j = 1   
            while j <= lt.size(catalog["obras"]):
                obra = lt.getElement(catalog["obras"], i)
                ids = obra["ConstituentID"]
                ids = ids.replace("[", "").replace("]","").replace(" ", "").split(",")
                for id in ids:
                    if id == iden:
                        tecnica = obra["Medium"]
                        if lt.isPresent(lista, tecnica)==0:

                            lista_2 = lt.newList()
                            lt.addLast(lista_2, tecnica)
                            lt.addLast(lista_2, 1)
                            lt.addLast(lista, lista_2)
                    
                        else:
                            tecnicas= lt.getElement(lista,lt.isPresent(lista,tecnica))
                            cantidad=lt.getElement(tecnicas,2)
                            lt.changeInfo(tecnicas,2,cantidad+1)               
                j+=1
        i+=1
    sorted_list = sa.sort(lista, comparepais)
    return lista
    
'''    lista=lt.newList("SINGLE_LINKED")
    lista_artista=lt.newList("SINGLE_LINKED")
    for i in range(1,lt.size(catalog)):
        nombre=lt.getElement(catalog["artistas"])
        if  str(nombre ["DisplayName"])==str(nombreArtista):
            lt.addLast(lista,nombre)
    for i in range(0,lt.size(lista_artista)):
        tecnica=lt.getElement(catalog["obras"])
        r=tecnica ["Medium"]
        lt.addLast(lista_artista,r)'''

def clasificarObrasNacionalidad(catalog):
    lista=lt.newList('ARRAY_LIST',
                                    cmpfunction=comparepaises)
    
    i =1
    while i <= lt.size(catalog["obras"]):
        obra = lt.getElement(catalog["obras"], i)
        ids = obra["ConstituentID"]
        ids = ids.replace("[", "").replace("]","").replace(" ", "").split(",")
        
        for id in ids:
            j = 1
            encontre_artista=False
            
            while j<= lt.size(catalog["artistas"]) and not encontre_artista:
                artista = lt.getElement(catalog["artistas"], j)
                iden= artista["ConstituentID"]
                
                if id == iden:
                    encontre_artista=True
                    nacionalidad = artista["Nationality"]
                    if nacionalidad == "":
                        nacionalidad = "Unknown"
                    if lt.isPresent(lista, nacionalidad)==0:

                        lista_2 = lt.newList()
                        lt.addLast(lista_2, nacionalidad)
                        lt.addLast(lista_2, 1)
                        lt.addLast(lista, lista_2)
                    
                    else:
                        pais= lt.getElement(lista,lt.isPresent(lista,nacionalidad))
                        cantidad=lt.getElement(pais,2)
                        lt.changeInfo(pais,2,cantidad+1)               
                j+=1
        i+=1
    sorted_list = sa.sort(lista, comparepais)
    return sorted_list

        


"""""
def tiempo (catalog, tamaño,tipo_sort):
    sublist=lt.subList(catalog["obras"],1,tamaño)
    inicio=time()
    if tipo_sort=="Shell":
            ordenar=sa.sort(catalog["artistas"],cmpfunction)
            lista=lt.newList("ARAY_LIST")
    if tipo_sort=="Merge":
            ordenar=mg.sort(catalog["artistas"],cmpfunction)
            lista=lt.newList("ARAY_LIST")
    if tipo_sort=="Insertion":
            ordenar=ins.sort(catalog["artistas"],cmpfunction)
            lista=lt.newList("ARAY_LIST")
    if tipo_sort=="Quick Sorts":
            ordenar=qs.sort(catalog["artistas"],cmpfunction)
            lista=lt.newList("ARAY_LIST")
    fin=time()
    tiempo=(fin-inicio)*1000
    return tiempo










#Como curador del museo quiero listar cronológicamente las obras adquiridas por el museo en un rango de fechas.



#Como investigador del museo quiero clasificar las obras de un artista de acuerdo a la técnica (medios) utilizada para su creación.
"""
