
def BusquedaBinaria(lista, numero):
    if len(lista)<=0:
        return "numero no encontrado"

    #si la lista si tiene elementos, vamos a buscar el numero que se enuentra a la mitad
    mitad = len(lista) // 2 #guardamos el elemento que se encuentra a la mitad de la lista, lalista se divide en 2, y obtendemos el numero de la mitad

    if mitad==numero:
        return "numero encontrado"
    #luego verificamos si el numero que estamos buscando es mayor o menor al numero de lamitad
    else:
        if numero < mitad:
            #empezamosdesde la posicion 0 hasta la mitad
            return BusquedaBinaria(lista[:len(lista) // 2], numero)
        else:
            return BusquedaBinaria(lista[(len(lista) // 2) + 1:], numero )

Lista1 = [1,2,3,4,5,6,7,8,9,10]
numero = 2
print(BusquedaBinaria(Lista1, numero))



#algoritmo Buble Sort(Burbuja)
Lista = [1,2,3,4,5,6,7,8,9,10]
for n in range(len(Lista) -1,0,-1):
    for i in range(n):
         if Lista[i]>Lista[i+1]:
            x = Lista[i]
            Lista[i]=Lista[i+1]
            Lista[i+1] = x
print(Lista)

#algoritmo de busqueda lineal

def BusquedaLineal(lista, numero):
    for i in range(len(lista)):
        if lista[i]==numero:
            return "numero encontrado"
    return "no se encuentra en la lista"

lista = [1,2,3,4,5,6,7,8,9,10]
buscar = 33
print(BusquedaLineal(lista, buscar))



if __name__=="__main__":
   pass

 
    

        

