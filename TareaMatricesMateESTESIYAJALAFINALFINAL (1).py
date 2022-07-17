#Codigo para resolver una matriz de n x n con el metodo de Gauss Jordan
#Fernanda Monserrat Galván Romero A00344712
#Luis Paulo Flores Arzate A01275194
#Barbara Nicole Vidal Sandoval A01635233


#Funcion para crear una matriz e ingresar datos
def escibirmatriz():
    
    lineas = (input("Ingrese el numero de Filas:"))
    while(lineas == "" or lineas == "-"):
        print("Ingrese un valor valido \n")
        lineas = (input("Ingrese el numero de Filas:"))
    lineas = int(lineas)

    renglones = (input("Ingrese el numero de Columnas:"))
    while(renglones == "" or renglones == "-"):
        print("Ingrese un valor valido \n")
        renglones = (input("Ingrese el numero de Columnas:"))
    renglones = int(renglones)

    matriz=[]
    for i in range (lineas):
        lista = []
        for j in range (renglones):
            num = (input(f'numero en la posicion [{i+1}, {j+1}]: '))
            while(num == "" or num == "-"):
                print("Ingrese un valor valido \n")
                num = (input(f'numero en la posicion [{i+1}, {j+1}]: '))
            num = int(num)
            lista.append(num)
        matriz.append(lista)   
    return matriz



#Funcion para imprimir la matriz
def showMatrix():
    print('------------------')
    for i in matriz:
        for j in i:
            print(round(j), end="\t")
        print("\n")
#Funcion para crear los pivotes en la matriz  
def pivote(piv):
        if matriz[0][0] == 0:
                matriz2 = matriz[0]
                matriz[0] = matriz[1]
                matriz[1] = matriz2
                showMatrix()

        else:
             for i in range(len(matriz[0])):
                if matriz[piv][piv] != 1:
                    q00 = matriz[piv][piv]
                    if q00 != 0:
                        for j in range(len(matriz[0])):
                            matriz[piv][j] = matriz[piv][j] / q00
#Funcion para hacer los 0 en la matriz
def ceros(r, c):
    for i in range(len(matriz[0])):
        if matriz[r][c] != 0:
            q04 = matriz[r][c]
            print('')
            showMatrix()
            for j in range(len(matriz[0])):
                matriz[r][j] = matriz[r][j] - ((q04) * matriz[c][j])
            


# MAIN
inicio = "1"
while inicio != "0":
    matriz = escibirmatriz()
    showMatrix()
    long = len(matriz)
    for k in range (long):
        solucion = (input(f'Ingrese la variable independiente {k+1}: '))
        while solucion == "" or solucion == "-":
            print("Ingrese un valor valido \n")
            solucion = (input(f'Ingrese la variable independiente {k+1}: '))
        solucion  = int(solucion)
        matriz[k].append(solucion)
    showMatrix()
    linea = len(matriz[0])
    for i in range(long):
        pivote(i)
        for j in range(long):
            if i != j:
                ceros(j, i)

    showMatrix()

    cont = 0
    if matriz[long-2][linea-2] == 0:
        matriz2 = matriz[long-2]
        matriz[long-2] = matriz[long-1]
        matriz[long-1] = matriz2
        showMatrix()
    
    for i in range(len(matriz)):
        casilla = 0
        while casilla < (len(matriz[0])-1):
            if matriz[i][casilla] != 0:
                cont +=1
                casilla = len(matriz[0])-1
            else:
                casilla +=1
    cant = 0

    while cant == 0:
        for i in range (long):
            cant = 0
            for j in range (linea):
                if round(matriz[i][j]) != 0:
                    cant = 1
    if cant == 0:
        cant = 3
    cant2 = 0
    while cant2 == 0:
        for i in range (long):
             cant2 = 0
             if round(matriz[i][linea-1]) !=0:
                for j in range (linea):
                    if round(matriz[i][j]) == 0:
                        cant2 += 1
             if cant2 == 1*linea-1:
                cant2 = -1
            
    if cont < linea-1 and cant != 3 and cant2 != -1:
        print(f'El rango de la matriz es {cont}')
        print("El sistema tiene soluciones infinitas")
        print("Hay mas variables que soluciones")
    elif cont > linea-1:
        print(f'El rango de la matriz es: {cont}')
        print('El vector resultante es:')
        for i in range (linea-1):
            print(f' [x{i}] = [{round((matriz[i][long]),3)}]')
        print(f' [x{(linea-1)}] = 0')
    elif cant == 3:
        print(f'El rango de la matriz es {cont}')
        print("El sistema tiene soluciones infinitas")
        print("Una fila es nula y su variable dependiente es 0")
    elif cant2 == -1:
        print(f'El rango de la matriz es {cont}')
        print("El sistema no tiene solucion")
        print("Una fila es nula y su variable dependiente es diferente 0")                
    else:
        print(f'El rango de la matriz es: {cont}')
        print('El vector resultante es:')
        for i in range (long):
            print(f' [x{i}] = [{round((matriz[i][long]),3)}]')
    inicio = input("Presione cualquier boton para continuar, presione 0 para salir: ")



    