
import random
saldo=10000
#metodo lanzar moneda 
def lanzarMoneda():
    nombre=input("ingrese su nombre: ")
    print("Hola " +nombre+ " bienvenido/a al juego de carisellazo:)!")
    moneda=random.randint(1, 2)
    return (moneda, nombre)
    

    

#Metodo jugar
def jugar():
    jugador=(int)(input("elije\n 1.cara\n2.Sello: "))
    apuesta=(int)(input("ingrese el valor que desea apostar: "))

    return (jugador, apuesta)

#Metodo ganar
def ganar(apuesta):
        sal=apuesta*2
        respuesta= print (f"Has ganado, ahora tienes {sal} ")
        return respuesta
    
        
def perder(apuesta):
        sal=apuesta*0
        respuesta= print (f"Has perdidos tienes {sal} ")
        return respuesta


moneda, nombre=lanzarMoneda()
jugador, apuesta=jugar()
if moneda==jugador:
    g=ganar(apuesta)
    

elif moneda!=jugador:
    p=perder(apuesta)
    