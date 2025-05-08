from datetime import datetime

class Gasto():
    __patente: str
    __fecha: datetime
    __importe: float
    __descripcion: str

    def __init__(self, patente: str, fecha: datetime, importe: float, descripcion: str):
        self.__patente = patente
        self.__fecha = fecha
        self.__importe = importe
        self.__descripcion = descripcion

    def __str__(self):
        return f"Patente: {self.__patente}, Fecha: {self.__fecha}, Importe: {self.__importe}, Descripcion: {self.__descripcion}"
    

    def getPatente(self):
        return self.__patente
    
    def getFecha(self):
        return self.__fecha
    
    def getImporte(self):
        return self.__importe
    
    def getDescripcion(self):
        return self.__descripcion
    

    # def __lt__(self, otro):
    #     return (self.__fecha, self.__patente) < (otro.__fecha, otro.__patente)

    def __lt__(self, otro):
        if self.__fecha == otro.getFecha():
            return self.__patente < otro.getPatente()
        return self.__fecha < otro.getFecha()