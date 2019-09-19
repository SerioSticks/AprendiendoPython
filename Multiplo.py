#Creador Jorge Alberto Flores Sánchez
#Matricula: 1622167  Grupo: 22
#Fecha de Creación : 18/09/2019

#Se captura un numero y se almacena una vez convertido a int
numero=int(input("Dame un numero entero:"))
#Se almacenan en valores de tipo booleano los residuos de la operacion.
#Esto quiere decir que si el residuo es 0 entonces es múltiplo.
esMultiplicado3=((numero%3)==0)
esMultiplicado5=((numero%5)==0)
esMultiplicado7=((numero%7)==0)
#Usar el operador and resuelve por cierto si todas las condiciones,
#son ciertas.En el caso de or se da por cierta al menos si una lo es,
#Los parentecis dividen las condiciones esto quiere decir que la
#comparación con and es una y con or es independiente de esta.
if((esMultiplicado3 and esMultiplicado5) or esMultiplicado7):
    print("Correcto.")
else:
    print("Incorrecto.")
#Esta condicion evalua solo si es multiplo de 3 y 5 o 7 , en cualquiera
# de estos casos sera verdadera , de lo contrario sera falsa.