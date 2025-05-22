class Movilidad():
    __patente: str
    __tipo: str
    __capacidadCarga: float
    __impMensual: float
    __marca: str
    __modelo: str

    def __init__(self, patente: str, tipo: str, capacidadCarga: float, impMensual: float, marca: str, modelo: str):
        self.__patente = patente
        self.__tipo = tipo
        self.__capacidadCarga = capacidadCarga
        self.__impMensual = impMensual
        self.__marca = marca
        self.__modelo = modelo

    def __str__(self):
        return f"Patente: {self.__patente}, Tipo: {self.__tipo}, Capacidad de Carga: {self.__capacidadCarga}, Impuesto Mensual: {self.__impMensual}, Marca: {self.__marca}, Modelo: {self.__modelo}"
    
    def getPatente(self):
        return self.__patente
    
    def getTipo(self):
        return self.__tipo
    
    def getCapacidadCarga(self):
        return self.__capacidadCarga
    
    def getImpMensual(self):
        return self.__impMensual
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
        