#Creador Jorge Alberto Flores Sánchez
#Matricula: 1622167  Grupo: 22
#Fecha de Creación : 18/09/2019

numero=input("Dame un numero del 1 al 9: ")
numero=int(numero)
#La instrucción for ejecuta una instruccion que se repite determinada,
#cantidad de veces (rango)
#El segundo parámetro de range no se incluye en la serie de valores.
#En este caso el rango es del 1 al 10.
for i in range(1,11):
    #i va variando a cada iteración (o ciclo)
    salida="{} x {} = {}"
    print(salida.format(numero,i,i*numero))