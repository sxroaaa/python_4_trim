fruver={}

while True:
    print("Fruver supermercados Noe")
    print("1.Añadir/Modificar")
    print("2.Buscar")
    print("3.Borrar")
    print("4.Listar")
    print("5.salir")
    
    opcion=int(input("¿Que opcion desea realizar?"))
    
    if opcion==1:
        articulo= input("ingrese el nombre del articulo:")
        if articulo in fruver:
            print("el articulo ya se encuentra registrado:")
            opcion=input(" 1.Modifica el precio del articulo\n 2.Modifica el tipo de articulo\n 3.Terminar\n ")
            if opcion=="1":
                precio=int(input("Dame el nuevo precio del articulo:"))
                fruver[articulo]["precio"]=precio
            if opcion=="2":
                tipo=input("Selecciona el nuevo tipo de articulo 1.Vegetal 2.Fruta:")
                if tipo=="1":
                    variedad="vegetal"
                elif tipo=="2":
                    variedad=="fruta"
                fruver[articulo]["tipo"]= variedad
        else:
            fruver[articulo]={}
            precio=int(input("Dame el precio del articulo:"))
            fruver[articulo]["precio"]=precio
            tipo=int(input("Selecciona el nuevo tipo del articulo 1.Vegetal 2.Fruta:"))
            if tipo==1:
                    variedad="vegetal"
            elif tipo==2:
                    variedad="fruta"
            fruver[articulo]["tipo"]=variedad
            
    elif opcion==2:
        texto=input("Ingrese el articulo a buscar")
        print("Se encontraron los siguientes resultados")
        
        for articulo, datos in fruver.item():
            if articulo.startwith(buscar):
                print("El precio del articulo ingresado es {fruta[articulo]['precio']} y es de tipo {fruver[articulo]['tipo']}")
                print(articulo)
    elif opcion==3:
        articulo=input("ingrese el articulo que desea eliminar del fruver")
        if articulo in fruver:
            confirmacion=int(input("¿Esta seguro que desea eliminar el articulo del fruver?\n 1.Si\n 2.No:"))
            if confirmacion==1:
                del fruver[articulo]
                print(fruver)
                
            if confirmacion==2:
                print("Operacion desertada")
                
        else:
            fruver[articulo]={}
            precio=int(input("Dame el precio del articulo:"))
            fruver[articulo]["precio"]=precio
            tipo=int(input("Selecciona el nuevo tipo del articulo 1.Vegetal 2.Fruta:"))
            if tipo==1:
                    variedad="vegetal"
            elif tipo==2:
                    variedad="fruta"
            fruver[articulo]["tipo"]=variedad
                
    if opcion==4:
       for clave, valor in fruver.items():
        print(clave)
        print(valor)
        
    if opcion==5:
        print("Adios:)")
        break