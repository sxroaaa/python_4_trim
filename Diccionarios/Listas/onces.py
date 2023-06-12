onces=["hamburguesa", "sandwich", "pizza"]

#añadir elementos
onces.append("gaseosa")


#agregar varios elementos
onces.extend(["Malteada", "perro caliente"])

#insertar elementos en una posicion especifica
onces.insert(2, "empanadas")

#borrar un elemento de una lista
onces.remove("Malteada")


#Borrar un elemento de una posicion especifica de la lista
del onces[0]

#borrar el ultimo elemento de una lista
onces.pop()

#limpiar la lista
#onces.clear()

##Ordenar elementos de una lista

#ordenar ascendentemente una lista 
onces.sort();

print(onces)

#ordenar descendentemente una lista
#onces.reverse();
onces.sort(reverse=True)
print(onces)

#devolver en que posicion esta un elemento de la lista
print(onces.index("empanadas"))