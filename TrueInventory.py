# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 14:51:55 2021

@author: JimmyLpz


Create
Read
Update
Delete
Show
Queries


"""

def create(b,e):
    b.append(e)
    return b
def read(x):
    return x=="Cocacola"
def update(x):
    #check below cause i really dont found the way to change lambda to a function
    return x
def delete(x):
    quitar=12
    
    return x!=quitar
#extras
def show(x):
    return x
def querys(x):
   
    return x



b=[1,"Cocacola","Bebida Energetica",12,"Cocacola"]


#the other way print(list(map(lambda x:x,b))) and show all
#Show all the list
print("\n\n La lista es: ",list( map(show,b)))
#READ
print("\n\n Encontrar Elementos repetidos de la lista: ",list(filter(read,b)))


#delete ||| quitar=12
result=filter(delete,b)
print("\n\nEliminar 1"," entonces",list(result))

print("\n\n Cambiar 1 por hola ",list(map(lambda x: "hola" if x == 1 else x,b)))
#print("\n\nCambiamos 1 por cocacola",list(filter(update,b)))

#print(update("Cocacola"))
print("\nAgregar Producto un elemento a la lista: bebida Alcoholica",create(b,"bebida Alcoholica"))
print("\nAgregar Producto un elemento a la lista: 9",create(b,9))

contador=lambda x,cont=0: cont,b
#print(list(contador))


