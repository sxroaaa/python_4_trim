instructores=[]

def añadirInstructor():
    instructor=input("ingrese el nombre del instructor que desea añadir:):")
    instructores.append(instructor)

def listarInstructores():
    for index, i in enumerate(instructores):
        print(index, i)

def modificarInstrutor():
    instructor=input("Digite el instructor que desea modificar en la lista ")
    posicion=(int)(input("ingrese la posicion que desea modificar"))
    instructores.insert(posicion, instructor)
    print(instructores)

def borrarInstructor():
    for index, i in enumerate(instructores):
            print(index, i)
    instructor=(int)(input("¿Que instructor desea eliminar de la lista?, elija la posicion:) "))
    del instructores[(instructor)]
    print(instructores)

def buscarInstructor():
        instructor=input("¿Que instructor desea buscar en la lista?")
        print("buscando..")
        
        if instructor.lower in instructores:
            print("el instructor " +instructor+ " si existe en la lista")
            
        else:
            print("El instructor no existe en la lista")

def ordenarLista():
     instructores.sort
     print(instructores)




while True:
    print("1.Añadir un instructor")
    print("2.Listar los instructores")
    print("3.Modificar un elemento de la lista")
    print("4.borrar un elemento de la lista")
    print("5.buscar un elemento en la lista")
    print("6.Ordenar la lista de la A a la Z")
    print("7.Salir")

    eleccion=(int)(input("elija una de las opciones:)"))

    if eleccion==1:
         añadirInstructor()

    if eleccion==2:
         listarInstructores()

    if eleccion==3:
         modificarInstrutor()

    if eleccion==4:
         borrarInstructor()

    if eleccion==5:
         buscarInstructor()

    if eleccion==6:
         ordenarLista()

    if eleccion==7:
         print("Saliendo:)....")
         break