num=(int(input('digite un numero entre 1 o 10')))

if num<1 or num>10:
    print("lo lamentamos, esta operacion no puede ser posible:(")
    
    
else:
    for i in range(1, 11):
        multi= num*i
        print(f'{num} x {i} = {multi}')