baul=["anillos", "mangas"]

while True:
    print("1.Añadir un articulo al baul")
    print("2.Listar articulos del baul de forma ascendente")
    print("3.Borrar el ultimo elemento de la lista")
    print("4.borrar un articulo del baul")
    print("5.Salir")
    
    op=input("Escoja una de las opciones: ")
    
    if op=="1":
        Articulo=input("¿Que articulo desea agregar a la lista?")
        baul.append(Articulo)
        print(baul)
        
    if op=="2":
        baul.sort()
        print(baul)
        
    if op=="3":
        baul.pop()
        print(baul)
    
    if op=="4":
        for index, i in enumerate(baul):
            print(index, i)
        Articulo=(int)(input("¿Que articulo desea eliminar de la lista?, elija la posicion:) "))
        del baul[(Articulo)]
        print(baul)
        
    if op=="5":
        print("Saliendo...")
        break
    