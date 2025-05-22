import numpy as np
from claseColectivo import Colectivo
import csv

class GestorColectivos():
    __arreColectivos : np.ndarray
    __dimension: int
    __cantidad: int
    __incremento= 5

    def __init__(self, dimension, incremento=5):
        self.__arreColectivos=np.empty(dimension, dtype=Colectivo)
        self.__dimension=dimension
        self.__cantidad=0


    def agregarColectivo(self, unColectivo):
        if self.__dimension == self.__cantidad:
            self.__dimension+=self.__incremento
            self.__arreColectivos.resize(self.__dimension)

        self.__arreColectivos[self.__cantidad]=unColectivo
        self.__cantidad+=1

        return


    def cargarColectivos(self):
        with open("colectivos.csv", "r") as archColec:
            reader= csv.reader(archColec, delimiter=";")
            next(reader)

            for fila in reader:
                self.agregarColectivo(Colectivo(fila[0], fila[1], fila[2], int(fila[3]), fila[4]))

        for i in range(self.__cantidad):
            print(self.__arreColectivos[i])


    def buscarChoferDNI(self, xdni):
        i:int=0
        dniEncontrado=False
        aux=-1

        while i<self.__cantidad and dniEncontrado is not True:
            if self.__arreColectivos[i].getDNI() == xdni:
                aux=self.__arreColectivos[i].getPatente()
                dniEncontrado=True
            else:
                i+=1

        return aux
    

    def listarGastosColectivos(self, GT):
        for i in range(self.__cantidad):
            GT.mostrarDatos(self.__arreColectivos[i].getPatente(), Colectivo.getConsumo())

        return

    #Mostrar por cada colecƟvo la canƟdad total de km recorridos y el gasto esƟmado 
#   en combusƟble para la canƟdad total de km recorridos. 