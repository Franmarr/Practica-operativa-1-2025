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
        
        print(f"Total de gastos: {acu+xpatMovi.getImpMensual()}")

        return
    

    def indicarGastoPorFecha(self, xfecha):
        i:int=0
        aux=-1
        fechaEncontrada=False
        fechaConvertida=datetime.strptime(xfecha, "%Y-%m-%d").date()
        while i<len(self.__listaGastos) and fechaEncontrada is not True:
            #print(self.__listaGastos[i])
            if self.__listaGastos[i].getFecha().date()==fechaConvertida:
                aux=self.__listaGastos[i]
                fechaEncontrada=True
            else:
                i+=1

        return aux


    def obtenerGastosOrdenados(self):
        self.__listaGastos.sort()
        print("ordenado de menor a mayor con sobrecarga")
        for elem in self.__listaGastos:
            print(elem)


        # fechaConvertida=datetime.strptime(xfecha, "%Y-%m-%d")
        # acu=0
        # for unGasto in self.__listaGastos:
        #     if unGasto.getFecha()==fechaConvertida:
        #         print(f"Gasto de la fecha indicada: {unGasto.getImporte()}")
        #         acu+=float(unGasto.getImporte())

        # print(f"Total general a pagar: {acu}")

        # return


