# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 11:50:55 2021

@author: JimmyLpz

INVENTORY CRUD 

create = x{int{key1,a,key2,b,key3,b,keyn,z}}
def (inventory)



Read = find x from inventory
def(inventario,object){
if(inventario[i]==input()){
   return inventario[i]
}else{
  return 0;
} 

}


Update = modificate x from inventory


Delete eliminate x from inventory


Show = print everything, and the category or the products
def(inventory){
for i in company_profile:
    print("category:  ",i,"\tProducto: ",company_profile[i]);
    or print(company_profile)
}
    
    
Queries= like s read counint the rows and collumns
and sum the number of products and print with a restriction
def(inventory){

for i in company_profile:
    x=company_profile[i]
    a= i+
    
print(x)
print(a)
}

"""
def create(inventory):
    return 0


def read(inventory,n):
    
    return 0


def update(inventory):
    inventory.update(inventory[4])
    return ''


def delete(inventory):
    del inventory[1]
    return ''


def show(inventory):
    
    return ''


def query(inventory):
  
    return ''


inventory={1:{   "name": "Emperador",
                 "Description": "Galletas de Chocolate",
                 "price":"16",
                 "date ": "july 1,2003"},
                 2:{"name": "Emperador",
                 "Description": "Galletas de lmon",
                 "price":"12",
                 "date ": "july 2,2003"},
                 3:{"name": "Emperador",
                 "Description": "Galletas de lmon",
                 "price":"13",
                 "date ": "july 2,2003"},
                  4:{"name": "Emperador",
                 "Description": "Galletas de lmon",
                 "price":"16",
                 "date ": "july 2,2003"},
                  5:{"name": "Emperador",
                 "Description": "Galletas de lmon",
                 "price":"7",
                 "date ": "july 2,2003"}}

"""
 FEEDBACK!!!!!!!!!!!!!!!!!!!!!!!!
 
#print(company_profile["name"])
#print(company_profile.get("share price","Information not available"))
#print(company_profile)

#print("introduzca si existe un proveedor:Proveedor,Producto,Fecha")

#new_information={"Proveedor": input(),
               #  "Producto": input(),
             #    "date": input()}



#company_profile.update(new_information)

#print(company_profile)
 """


print("\n\n List",show(inventory))
print("\n\n Number of Rows and Products",query(inventory))
print("\n\n a element Eliminated",delete(inventory))
print("\n\n How is the actually list",show(inventory))
print("\n\n Number of Rows and Products",query(inventory))
#print("\n\n Add a new row",update(inventory))
print("\n\n How is the actually list",show(inventory))







