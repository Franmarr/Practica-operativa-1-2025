import csv
from claseTramo import Tramo

class GestorTramos():
    __listaTramos: list

    def __init__(self):
        self.__listaTramos=[]


    def agregarTramo(self, unTramo):
        self.__listaTramos.append(unTramo)


    def cargarTramos(self):
        with open("tramos.csv","r") as archTramos:
            reader=csv.reader(archTramos, delimiter=";")
            next(reader)

            for fila in reader:
                self.agregarTramo(Tramo(fila[0], fila[1], float(fila[2]), fila[3]))


        for elem in self.__listaTramos:
            print(elem)

        return


    def listarTramosChofer(self, xpatente):
        for unTramo in self.__listaTramos:
            if unTramo.getPatente() == xpatente:
                print(f"Ciudad Origen: {unTramo.getCiudadOrigen()}, Ciudad Destino: {unTramo.getCiudadDestino()}, KM recorridos: {unTramo.getDistancia()}")

        return