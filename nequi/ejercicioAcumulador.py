presupuesto= 100000

print ('opcion 1: pagar transporte\n opcion 2: Gadstar onces a la profesora\n opcion 3: Ganar dinero')

for i in range(1, 6):
    opcion=(int(input('escoje una opcion:')))
    if opcion==1:
        presupuesto= presupuesto-6000
        print(f'usted eligio pagar el transporte, ahora su presupuesto es de {presupuesto}')

    if opcion==2:
        presupuesto=presupuesto-10000
        print(f'usted eligio pagar las onces de la profesora, ahora su presupuesto es de {presupuesto}')
        
    if opcion==3:
        presupuesto= presupuesto + 5000
        print(f'usted eligio ganar mas dinero, ahora su presupuesto es de {presupuesto}')  
        
    else:
        print('esa opcion no esta disponible')  