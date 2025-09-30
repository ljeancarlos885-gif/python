suma=0
for i in range (0,10,2):
    print ("dijite un numero" + str(i +1) +" : ")
    numero=int(input())
    suma=suma+numero
    
print ("la sumatoria total es: " + str (suma))
    
suma=0
print("digite la cantidad de numeros para sumar: ")
cantidad=int (input())
for i in range (cantidad):
    print("digite el numnero" + str (i+1)+": ")
    numero=int(input())
    suma=suma+numero
print("la sumatoria total es: "+ str(suma))
    