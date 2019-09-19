#Creador Jorge Alberto Flores Sánchez
#Matricula: 1622167  Grupo: 22
#Fecha de Creación : 18/09/2019


for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    #print sin argumentos es un salto de línea.
    print()
    #Dentro de un for, se pone otro for. (en este caso se le dice anidado)
    for j in range(1,11):
        #Aquí, i es el contenedor de la tabla base.
        #y j el elemento de la tabla.
        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        #Al concluir con el ciclo indicado se ejecuta este codigo,
        #da un salto de linea y finaliza.
        print()