class Colectivo():
    __patente: str
    __marca: str
    __modelo: str
    __capacidad: int
    __dni: str

    def __init__(self, patente, marca, modelo, capacidad, dni):
        self.__patente=patente
        self.__marca=marca
        self.__modelo=modelo
        self.__capacidad=capacidad
        self.__dni=dni

    def getPatente(self):
        return self.__patente
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getCapacidad(self):
        return self.__capacidad
    
    def getDni(self):
        return self.__dni
    
    def __str__(self):
        return f"Patente: {self.__patente}, Marca: {self.__marca}, Modelo: {self.__modelo}, Capacidad: {self.__capacidad}, DNI: {self.__dni}"