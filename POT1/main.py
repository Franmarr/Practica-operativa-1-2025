from gestorColectivos import GestorColectivos
from gestorTramos import GestorTramos


def menu():
    op = int(input("""
    1. Leer por teclado el DNI de un chofer y emitir un listado con los datos (ciudad
       origen, ciudad destino y km recorridos) de los tramos recorridos por él; al final
       del listado informar la cantidad total de km recorridos.
    2. Mostrar por cada colectivo la cantidad total de km recorridos y el gasto estimado
       en combustible para la cantidad total de km recorridos.
    3. Dada una distancia recorrida, listar los datos (ciudad origen, ciudad destino y
       patente del colectivo) de los tramos en los que los km recorridos superan la
       distancia dada. Regla de negocio: para resolver este último punto, el analista le
       solicita que sobrecargue el operador relacional correspondiente.

    Ingrese una opción: """))

    return op


if __name__ == "__main__":
    dimension=int(input("Ingrese la cantidad de colectivos: "))
    GC=GestorColectivos(dimension,5)
    GT=GestorTramos()

    GC.cargarColectivos()
    GT.cargarTramos()

    op=menu()

    while op!=0:
        if op == 1:
            dni=input("Ingrese DNI de chofer: ")

            patente=GC.buscarChoferDNI(dni)
            if patente != -1:
                GT.listarTramosChofer(patente)
            else:
                print("No se encontro el DNI ingresado.")
        elif op==2:
            GC.listarGastosColectivos(GT)


        op=int(input("Ingrese otra opcion o 0 para terminar: "))