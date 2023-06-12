utiles=['lapiz', 'borrador']

def buscarNombre():
      elemento=input('ingrese el elemento que desea buscar:')
      indice= utiles.index(elemento)
      print('el elemento ' +elemento+ ' esta en la posicion {} de la lista'.format(indice))
      util=input('digite el nuevo util:')
      utiles.insert(indice, util )
      print(utiles)

buscarNombre()
def Borrar():
    for index, i in enumerate(utiles):
        print(index, i)
    util=(int)(input("¿Que articulo desea eliminar de la lista?, elija la posicion:) "))
    confirmacion=input('¿esta seguro que desea eliminar el elemento de la lista?:')
    if confirmacion=='si':
         del utiles[(util)]
    if confirmacion=='no':
         print('transaccion cancelada:)')

    print(utiles) 

