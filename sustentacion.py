ropa=[]

while True:
    print('1.añadir prenda de ropa a la lista')
    print('2.si desea listar la lista')
    print('3.muestre las prendas registradas')
    print('4.para salir')
    op=(int(input('Elije la opcion que desea')))

    if op == 1:
        prenda=input('ingrese la prenda de ropa que desea añadir ')
        ropa.append(prenda)
        print(ropa)

    if op==2:
        for index, i in enumerate(ropa):
            print(index, i)
    
    if op==3:
        def mostrarPrendas():

            
    if op == 4:
        print('Saliendo...')
        break    