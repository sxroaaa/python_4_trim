jennifer={
    "nombre": "jennifer Fajardo",
    "materia":"Python Basico",
    "telefono": "3242567845",       
}
jonathan={
    "nombre":"Jonathan Espitia",
    "materia":"Base de datos",
    "telefono": "3163748897"
}

instructores2557861={
    "i1": jennifer,
    "i2": jonathan
    
}

while True:
    print("Instructores del SENA ficha 2557861:)")
    print("1.Añadir/Modificar")
    print("2.Buscar")
    print("3.Borrar")
    print("4.Listar")
    print("5.salir")
    
    op=int(input("¿Que opcion desea realizar"))
    
    if op==1:
        instructor=input("Ingrese el nombre del instructor")
        if instructor in instructores2557861:
            print("el instructor ya se encuentra en la lista")
            eleccion=input("1.modificar nombre\n 2.modificar materia\n 3.modificar telefono \n4.terminar")
            if eleccion=="1":
                nombre=input("Digite el nuevo nombre del instructor")
                instructores2557861[instructor]["nombre"]=nombre

            if eleccion=="2":
                materia=input("Digite la nueva materia")
                instructores2557861[instructor]["materia"]=materia

            if eleccion=="3":
                telefono=input("digite el nuevo telefono del instructor")
                instructores2557861[instructor]["telefono"]=telefono

            if eleccion=="4":
                print("Cancelar")
                break
        else:
            instructores2557861[instructor]={}
            nombre=input("Escriba el nombre del instructor")
            instructores2557861[instructor]["nombre"]=nombre
            materia=input("Escriba la materia del instructor")
            instructores2557861[instructor]["materia"]=materia
            telefono=input("digite el numero del instructor")
            instructores2557861[instructor]["telefono"]=telefono

    if op==2:
        instructor=input("Digite el instructor que desea buscar")
        print("Se encontraron los siguientes resultados...")

        for instructor, datos in instructores2557861.item():
            if instructor.startwith(instructor):
                print(f"El nombre del instructor es {instructores2557861[instructor]['nombre']}, la materia que dictan es {instructores2557861[instructor]['materia']} y su telefono {instructores2557861[instructor]['telefono']}")
        else:
            print("No se encontre el instructor...lo sentimos:(")

    if op==3:
        instructor=input("Digite el instructor que desea eliminar")
        if instructor in instructores2557861:
            confirmar=input("¿Esta seguro de eliminar el instructor?:\n1.Si\n2.No")
            if confirmar=="1":
                del instructores2557861[instructor]
            if confirmar=="2":
                print("Operacion cancelada:(")
        else:
            print("No se encontro el instructor")

    if op==4:
        for clave, valor in instructores2557861.items():
         print(clave)
         print(valor)
    if op==5:
        print("Saliendoo..")
        break