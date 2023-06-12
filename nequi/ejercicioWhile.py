print('opcion 1: pagar transporte\n opcion 2: pagar onces a la profesora\n opcion 3: ganar plata')

eleccion='si'
presupuesto=100000
contador1=0
contador2=0
contador3=0
while eleccion=='si':
    opcion=(int(input('Escoja una de las opciones:')))
    
    if opcion==1:
        presupuesto=presupuesto-6000
        print(f'usted eligio pagar el transporte, su presupuesto ahora es de {presupuesto} ')
        contador1 += 1
        

    if opcion==2:
        presupuesto=presupuesto-10000
        print(f'usted eligio pagar las onces de la profesora, su presupuesto ahora es de {presupuesto}')
        contador2 +=1
        
    if opcion==3:
        presupuesto=presupuesto+5000
        print(f'usted eligio ganar mas, ahora su presupuesto es de {presupuesto}')
        contador3 += 1
        
    print('¿desea elegir otra opcion?')
    eleccion=input('elija si o no:')     
     
print(f'la cantidad de veces que eligio la opcion 1 fue de {contador1} y la opcion 2 fue de {contador2} y la opcion 3 fue de {contador3}')

