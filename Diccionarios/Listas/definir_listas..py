lista=[1, 2, 3, 4] #declarar una lista

print(lista) #mostrar contenido de una lista
print(lista[0]) #Acceder a un elemento en particular de una lista 
print(lista[-1]) #Se puede acceder al ultimo elemento de una lista
lista[0]=7 #Se puede modificar el elemento de una lista
print(lista[0]) 


#Recorrer listas
for i in lista: #Iterar recorrer una lista 
    print(i)
    
for index, i in enumerate(lista): #si nececitamos un indice que acompañe a cada dato 
    print(index, i)
    

#Iterar 2 listas al mismo tiempo    
lista1=[5, 9, 10]
lista2=["jazz", "rock", "Djent"] 
for i1, i2 in zip (lista1, lista2):
    print(i1, i2)
    
#Longitud de la lista
print(len(lista))