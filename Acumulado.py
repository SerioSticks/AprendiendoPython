#Creador Jorge Alberto Flores Sánchez
#Matricula: 1622167  Grupo: 22
#Fecha de Creación : 18/09/2019

#Se declaran las variables con las que trabajara el algoritmo
acumulado=int(0)
numero=str("")
#Al crear un While true practicamente se crea un ciclo infinito,
#que no se romperá hasta utilizar la instrucción break
while True:
    numero=input("Dame un numero entero: ")
    if numero=="":
        #si no se ingresa ningun numero,se informa y termina el ciclo.
        print("Vacio. Salida del programa.")
        break
    else:
        #Si se proporciona un valor entonces entra el while
        #como acumulado=acumulado + numero y se realiza el calculo
        #usando la suma incluyente (+=)
        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))

        #Lo que hace es ir sumando todos los numeros y terminará,
        #hasta que se de un enter vacio sin numero.