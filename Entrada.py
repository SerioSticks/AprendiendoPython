#Creador Jorge Alberto Flores Sánchez
#Matricula: 1622167  Grupo: 22
#Fecha de Creación : 18/09/2019

entrada=input()
print(type(entrada))
#La variable booleana tiene como fin verificar si el dato ingresado,
#es o no un digito, y si no encuentra tampoco un punto decimal en, 
#lo capturado, indicara que se trata de un numero con decimales.
#En este caso float es para decir. Si find retorna -1 quiere decir,
#que el digito ingresado no se encontro.Y es verdadero solo si esEntero
#es un numero entero.
esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if (esEntero):
    #Si la condición se cumple entonces es  verdadera (True)
    print("Dato entero.¡Muy bien!")
else:
    #Esto se ejecuta si la condición es falsa (false)
    print("Dato no es entero. Intentar nuevamente.")
    