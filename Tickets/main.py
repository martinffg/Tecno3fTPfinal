import pickle, sys, os, random


# Función principal
def main():

    tickets = []
    # declaracion de variables globales
    opcionSalida = (
        "3"  # variable que setea el número de opción "Salir" en el "Menú Principal".
    )
    opcionStr = ""  # variable que guarda la opción elegida como un String.
    opcion = 0  # Variable que guarda la opción elegida como un Integer.
    salir = False
    # Fin declaracion de variables globales

    ##### Funciones para el manejo del Menú #####

    def mostrarTicketEnPantalla(nombre, sector, asunto, mensaje, numero):
        print("=" * 60)
        print("\t\tSe genero el Ticket\t")
        print("=" * 60)
        print(f"\tSu nombre: {nombre}\tN°Ticket: {numero}\t")
        print(f"\tSector: {sector}")
        print(f"\tSector: {asunto}\n")
        print(f"\tMensaje: {mensaje}\n")
        print(f"\t\tRecordar su numero de Ticket\n")

    def altaTicket():
        salirAlta = False
        # comienza loop de carga de tickets
        while salirAlta == False:
            ticket = {}
            print(f"\nIngrese los datos para Generar un nuevo Ticket")
            ticket["nombre"] = input("Ingrese su Nombre: ")
            ticket["sector"] = input("Ingrese su Sector: ")
            ticket["asunto"] = input("Ingrese Asunto: ")
            ticket["mensaje"] = input("Ingrese un Mensaje: ")
            ticket["numero"] = random.randrange(1000, 9999)
            tickets.append(
                ticket
            )  # Guardo el ticket en memoria para la lectura posterior en caso de ser más de uno y evitar el acceso a disco.
            guardar = (
                "ticket" + str(ticket["numero"]) + ".txt"
            )  # defino el nombre del ticket a persistir en disco
            # persisto a disco el ticket cargado
            with open(guardar, "wb") as f:
                pickle.dump(ticket, f)
            # Lo imprimo por pantalla
            mostrarTicketEnPantalla(
                ticket["nombre"],
                ticket["sector"],
                ticket["asunto"],
                ticket["mensaje"],
                ticket["numero"],
            )
            # valido si desea cargar otro ticket, la opción invalida equivale a querer continuar.
            opcionContinuar = input(f"Desea generar un nuevo Ticket) (s/n):")
            if opcionContinuar == "n":
                salirAlta = True
            elif opcionContinuar == "y":
                salirAlta = False
            else:
                print(f"Opcion Invalida. Continuaremos con la carga.")
        # fin loop carga de tickets

    def isTicketEnMemoria(numeroTicket):
        enMemoria = False
        posicion = 0
        while enMemoria == False and posicion < len(tickets):
            if tickets[posicion]["numero"] == numeroTicket:
                enMemoria = True
            posicion += 1
        return enMemoria

    def getInformacionTicket(numeroTicket):
        ticket = {}
        posicion = 0
        encontrado = False
        if isTicketEnMemoria(numeroTicket):
            while posicion < len(tickets) and encontrado == False:
                if tickets[posicion]["numero"] == numeroTicket:
                    encontrado = True
                posicion += 1
        else:
            print(f"El N°Ticket {numeroTicket} es inexistente.")
        return ticket

    def leerTicket():
        salirLectura = False
        while salirLectura == False:
            numeroTicket = input("Ingrese N°Ticket: ")
            abrir = "ticket" + numeroTicket + ".txt"
            ruta = abrir
            # valido que exista el archivo físico
            if os.path.isfile(ruta):
                with open(abrir, "rb") as f:
                    ticket = pickle.load(f)
                # Lo imprimo por pantalla
                mostrarTicketEnPantalla(
                    ticket["nombre"],
                    ticket["sector"],
                    ticket["asunto"],
                    ticket["mensaje"],
                    ticket["numero"],
                )
            elif isTicketEnMemoria(numeroTicket):
                ticket = getInformacionTicket(numeroTicket)
                if ticket["numero"] == numeroTicket:
                    # Lo imprimo por pantalla
                    mostrarTicketEnPantalla(
                        ticket["nombre"],
                        ticket["sector"],
                        ticket["asunto"],
                        ticket["mensaje"],
                        ticket["numero"],
                    )
            else:
                print(f"El N°Ticket {numeroTicket} es inexistente.")
            # valido si desea leer otro ticket, la opción invalida equivale a querer continuar.
            opcionContinuar = input(f"Desea leer otro Ticket) (s/n):")
            if opcionContinuar == "n":
                salirLectura = True
            else:
                salirLectura = False

    def salida():
        eleccion = input("Confirma que desea salir? presione 'y' para salir: ")
        if eleccion == "y":
            sys.exit()

    def mostrarOpcionesMenu():
        print("\nHola bienvenido al sistema de Tickets\n\n")
        print("1. Generar un Nuevo Ticket")
        print("2. Leer un Ticket")
        print("3. Salir")

    def ingresarOpcionValida(opcionStr, opcionSalida):
        opcion = 0
        if opcionStr.isdigit():
            # si el caracter ingresado es numérico entonces valida que sea un valor dentro de las opciones disponibles, sino itera hasta conseguir un número dentro del rango de las opciones del Menú.
            opcion = int(opcionStr)
            while opcion < 1 or opcion > int(
                opcionSalida
            ):  # valida que se ingrese una opción válida
                print("error, ingrese opción válida")
                opcionStr = input(f"(1-{opcionSalida}) >\t")
                if opcionStr.isdigit():
                    opcion = int(opcionStr)
        else:
            opcion = (
                -1
            )  # valor de opción inválida en caso que el caracter ingresado no sea numérico.
        return opcion

    def procesarOpcionElegida(opcion, opcionSalida):
        if opcion == 1:
            altaTicket()
        elif opcion == 2:
            leerTicket()
        elif opcion == int(opcionSalida):
            salida()
        else:
            print(f"Opción no válida - Ingrese un número del 1 al {opcionSalida}")

    # loop del programa principal
    while salir == False:
        # os.system("clear")  # en windows comentar esta linea
        os.system("cls")  # en windows DESCOMENTAR esta linea
        mostrarOpcionesMenu()
        opcionStr = input(f"Seleccione: ")
        opcion = ingresarOpcionValida(opcionStr, opcionSalida)
        if opcion > 0 and opcion <= int(opcionSalida):
            procesarOpcionElegida(opcion, opcionSalida)
        else:
            print(f"Opción no válida - Ingrese un número del 1 al {opcionSalida}")

    # Fin Función principal


if __name__ == "__main__":
    main()
