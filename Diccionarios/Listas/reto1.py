instructores=[]

while True:
    print("1.Añadir un instructor")
    print("2.Listar los instructores")
    print("3.Modificar un elemento de la lista")
    print("4.borrar un elemento de la lista")
    print("5.buscar un elemento en la lista")
    print("6.Ordenar la lista de la A a la Z")
    print("7.Salir")
    
    opcion=input("Elija una de las opciones:) ")
    
    if opcion=="1":
        instructor=input("Digite el nombre del instructor que desea agregar: ")
        instructores.append(instructor)
        print(instructores)
    
    if opcion=="2":
        for index, i in enumerate(instructores):
            print(index, i)

    if opcion=="3":
        indice=(int)(input("ingrese la posicion que desea modificar:"))
        instructor=input("Ingrese el instructor que desea modificar:")
        instructores.insert(indice, instructor)
        print(instructores)
        
    if opcion=="4":
        for index, i in enumerate(instructores):
            print(index, i)
        instructor=(int)(input("¿Que instructor desea eliminar de la lista?, elija la posicion:) "))
        del instructores[(instructor)]
        print(instructores)
        
    if opcion=="5":
        instructor=input("¿Que instructor desea buscar en la lista?")
        print("buscando..")
        
        if instructor.lower in instructores:
            print("el instructor " +instructor+ " si existe en la lista")
            
        else:
            print("El instructor no existe en la lista")