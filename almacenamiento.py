def maximizar(As, D):
    sortedList= sorted(As,key=lambda tup:tup[1])# se ordena para escoger facilmente siempre el menor 
    pesoActual=0
    index=0
    dispositivo=[]
    while(pesoActual<=D) and (index<len(sortedList)):
        if((pesoActual+sortedList[index][1])<= D):# revisa si queda espacio  
            dispositivo.append(sortedList[index])# lo inserta en el dispositivo
            pesoActual=pesoActual+sortedList[index][1]#
            index=index+1
        else:
            return dispositivo
