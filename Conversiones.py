#Creador Jorge Alberto Flores Sánchez
#Matricula: 1622167  Grupo: 22
#Fecha de Creación : 18/09/2019

#Primeramente declaramos nuestra variable
#del tipo string (str), con una cadena de digitos.
numero= "1234"
#Despues se va a mostrar el tipo de dato que es la variable
#numero. Usando la salida de Type()
print (type(numero))
# En este paso se va a convertir la cadena a entero.
numero=int(numero)
#Se va a mostrar el cambio de tipo, aunque siga siendo la misma
#variable (numero)
print(type(numero))
#Se declara un str con fin de sustituir (posiciones de la variable
# donde iran los valores proporcionados usando el format)
salida="El numero utilizado es {}"
#Finalmente se muestra el resultado.La sustitucion funciana,
#de tal maneta que donde este {} se coloque el valor de numero.
print(salida.format(numero))
