import csv
from claseGasto import Gasto
from datetime import datetime

class GestorGastos():
    __listaGastos: list

    def __init__(self):
        self.__listaGastos=[]

    
    def agregarGasto(self, unGasto):
        self.__listaGastos.append(unGasto)


    def cargarListaGastos(self):
        with open("gastosAbril2025.csv", "r") as archGastos:
            reader=csv.reader(archGastos, delimiter=";")
            next(reader)

            for fila in reader:
                fecha=datetime.strptime(fila[1], "%Y-%m-%d")
                unGasto=Gasto(fila[0], fecha, fila[2], fila[3])
                self.agregarGasto(unGasto)

        # for gasto in self.__listaGastos:
        #     print(gasto)


    def listarGastos(self, xpatMovi):
        acu=0
        print("-GASTOS-")
        for unGasto in self.__listaGastos:
            if unGasto.getPatente()==xpatMovi.getPatente() and unGasto.getFecha().month==4:
                print(f"Fecha: {unGasto.getFecha()}, Importe: {unGasto.getImporte()}, Descripcion: {unGasto.getDescripcion()}")
                
                acu+=float(unGasto.getImporte())
                print(acu)
        
        print(f"Total de gastos: {acu+xpatMovi.getImpMensual()}")

        return
    

    def obtenerGastoPorFecha(self, xfecha):
        acu=0
        xfechaConvertida= datetime.strptime(xfecha, "%Y-%m-%d").date()
        for unGasto in self.__listaGastos:
            if unGasto.getFecha().date() == xfechaConvertida:
                print(f"Gasto: {unGasto.getImporte()}")
                acu+=float(unGasto.getImporte())

        return acu


    def obtenerGastosOrdenados(self):
        self.__listaGastos.sort()
        # print("ordenado de menor a mayor con sobrecarga")
        # for elem in self.__listaGastos:
        #     print(elem)


    def incisoC(self, xfecha, GM):
        i:int = 0
        fechaConvertida=datetime.strptime(xfecha, "%Y-%m-%d").date()

        for unGasto in self.__listaGastos:
            # print(unGasto)
            if unGasto.getFecha().date() == fechaConvertida:
                GM.mostrarIncisoC(unGasto.getPatente())
                i+=1

        return i


