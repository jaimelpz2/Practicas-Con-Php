# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 23:34:28 2021

@author: JimmyLpz
"""

li=0

while li <5:
    print(li)
    #li=li+1
    li +=1
    #if li ==3 :
        #break
else:
    print("el bucle while ha terminado")
    
    
    print("ahora veremos el bucle for")

for li in 1,0,7:
    print(li)
    
   
    #un bucle para un conjunto es decir un arreglo algo asi1
for nombre in "juan","luis","carlos":
    print(nombre)
    
    #luego vamos a interrumpir un ciclo for
    
    
for li in 1,0,2,8:
    print(li)   
    if li==2:
        pass #se puede omitir la identacion con este comando
else:
    print("el bucle ha llegado hasta el final")
    pass


una_tupla=(1,2,3.0,4+0j,"5")
una_tupla


una_lista=[1,2,3.0,4+0j,"5"]
una_lista

una_tupla == una_lista


for elemento in una_tupla:
    print(elemento)

1 in una_tupla #compara si estos datos se encuentran en tal estructura
2 in una_lista # y lanza un true o false pero no funciona aqui tal cual

una_tupla[0] # muestra el primer valor de la tupla
una_lista[-1] # muestra el ultimo valor de la lista
# el -1 indica que empezara contando desde atras 
una_lista[0:3]#solo cuenta los numeros desde el 0 hasta el 3 

lista_anidada=[[1,2],[3,4]]
lista_anidada