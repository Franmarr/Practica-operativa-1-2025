import numpy as np
from claseMovilidad import Movilidad
import csv

class GestorMovilidades():
    __dimension: int
    __incremento=5
    __cantidad: int
    __arreMovi: np.ndarray


    def __init__(self, dimension, incremento=5):
        self.__arreMovi=np.empty(dimension, dtype=Movilidad)
        self.__cantidad=0
        self.__dimension= dimension


    def agregarMovilidad(self, unaMovilidad):
        if self.__dimension==self.__cantidad:
            self.__dimension+=self.__incremento
            self.__arreMovi.resize(self.__dimension)

        self.__arreMovi[self.__cantidad]=unaMovilidad
        self.__cantidad+=1

        return

    
    def cargarMovilidades(self):
        with open("movilidades.csv", "r") as archMovi:
            reader=csv.reader(archMovi, delimiter=";")
            next(reader)

            for fila in reader:
                unaMovilidad=Movilidad(fila[0], fila[1], float(fila[2]), float(fila[3]), fila[4], fila[5])
                self.agregarMovilidad(unaMovilidad)
                
            # for i in range(self.__cantidad):
            #     print(self.__arreMovi[i])

    
    def buscarPatenteMovi(self, xpate):
        patEncontrada=False
        i=0
        aux=-1
        while i<self.__cantidad and patEncontrada is not True:
            if self.__arreMovi[i].getPatente() == xpate:
                aux=self.__arreMovi[i]#.getPatente()
                patEncontrada=True
            else:
                i+=1

        return aux
    

    def mostrarPatenteMovi(self, patente):
        print(f"Patente: {patente.getPatente()}, Tipo: {patente.getTipo()}, Capacidad Carga: {patente.getCapacidadCarga()}, Imp mensual de patente: {patente.getImpMensual()}, Marca: {patente.getMarca()}, Modelo: {patente.getModelo()}")
        return
