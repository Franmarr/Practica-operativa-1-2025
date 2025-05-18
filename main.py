from gestorMovilidades import GestorMovilidades
from gestorGastos import GestorGastos

def menu():
    op=int(input("""
                1-Leer por teclado la patente de una movilidad, si no existe, emitir un mensaje de error, si
                existe listar los gastos que ha tenido en el mes de abril, indicando el total de gastos.
                2-Dada una fecha, indicar los gastos que se produjeron ese día, indicando el total general a
                pagar.
                3-Dada una fecha, indicar para cada movilidad, patente, marca, modelo y total a pagar. Para
                resolver este punto, debe ordenar el Gestor de Gastos de menor a mayor, por fecha y
                patente, debiendo sobrecargar el operador correspondiente en la clase Gasto.
                Ingrese la opcion que desea realizar: """))
    
    return op


if __name__ == "__main__":
    GM=GestorMovilidades(5, 5)
    GM.cargarMovilidades()

    GG=GestorGastos()
    GG.cargarListaGastos()
    opcion=menu()
    while opcion != 0:
        if opcion==1:
            patente=input("Ingrese patente a buscar: ") #puede ser por teclado: AG400IC
            patEncontrada=GM.buscarPatenteMovi(patente)

            if patEncontrada != -1:
                GM.mostrarPatenteMovi(patEncontrada)
                GG.listarGastos(patEncontrada)

            else:
                print("No se encontro patente")
        
        elif opcion==2:
            fecha=input("Ingrese una fecha en formato Y-M-D: ") #aqui tiene que escribir por teclado una fecha como: 2025-03-21
            aux=GG.obtenerGastoPorFecha(fecha)

            if aux != 0:
                print(f"Gasto total para la fecha: {aux}")
            else:
                print("No hubo gastos para la fecha indicada")

        elif opcion == 3:
            GG.obtenerGastosOrdenados()
            fecha1=input("Ingrese una fecha en formato Y-M-D: ")
            #GG.obtenerGastoPorFecha(fecha1)

            GG.mostrarIncisoC(fecha1, GM)

            
        opcion=int(input("Ingrese otra opcion: "))
