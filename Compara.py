#Creador Jorge Alberto Flores Sánchez
#Matricula: 1622167  Grupo: 22
#Fecha de Creación : 18/09/2019

numero1=input("Numero 1:")
numero2=input("Numero 2:")
salida= "Numeros proporcionados: {} y {}. {}."
if(numero1==numero2):
    #Si los numeros son iguales se ejecuta este if.
    print(salida.format(numero1,numero2,"Los numeros son iguales"))
else:
    #Si los numeros no son iguales entra al if anidado,
    #(un if dentro de otro if), esto si los numeros son diferentes
    if numero1>numero2:
        #Indica si el primer numero es mayor
        print(salida.format(numero1, numero2,"El mayo es el primero"))
    else:
        #De lo contrario el segundo es mayor
        print(salida.format(numero1,numero2,"El mayor es el segundo"))