#Creador Jorge Alberto Flores Sánchez
#Matricula: 1622167  Grupo: 22
#Fecha de Creación : 18/09/2019

#En python existen muchas librerias para facilitar la programación,
#a estas se les denomina modulos (module).
#Para usar un modulo debe importarse y para esto se utiliza la,
#instrucción import
import random
#Definimos nuestra variables, que en esta ocasion sera de tipo,
#flotante (float) y le asignamos un valor.
numero1=float(10.5)

#En python las funciones son instrucciones que hacen una tarea,
#específica, como una unidad de ejecución.
#Se declaran con def.Y todo el codigo identado a la derecha de la ,
#definicion forma parte de la misma función.
def miFuncion():
    #El numero aleatorio se convierte a float, este es generado por
    #random.randrange() (este solo esta disponible si se importa,
    # el modulo random)
    numero2=float(random.randrange(1,10))
    #Se utilizan sustituciones para mostrar resultados.
    mensaje="La suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))

#Se ejecuta la función definida en el código.
miFuncion()