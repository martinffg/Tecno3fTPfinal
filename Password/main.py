import secrets, string, sys, os


# Función principal
def main():

    password = ""

    diccionario = {
        "letras": string.ascii_letters,  # cadena del alfabeto en mayusculas y minusculas
        "numeros": string.digits,  # cadena de numeros del 0 al 9
        "caracteres": string.punctuation,  # cadena de caracteres especiales
    }

    # declaro constantes del proyecto
    MAX_OPCION = (
        4  # variable que registra el máximo número de opción disponible en el menú.
    )

    MAX_PASSWORD_LENGTH = 10

    # declaracion de variables globales
    opcionSalida = "0"  # variable que setea el número de opción "Salir" en el "Menú Principal". Se debe setear como String obligatoriamente.
    opcionStr = ""  # variable que guarda la opción elegida como un String.
    opcion = -1  # Variable que guarda la opción elegida como un Integer.
    salir = False
    # Fin declaracion de variables globales

    ##### Funciones para el manejo del Menú #####

    def mostrarPasswordObtenida(passwd):
        print("=" * 80)
        print(f"\tSe genero su nueva password: {passwd}")
        print("=" * 80)
        input("Presione una tecla para continuar. ")

    def getPasswordSoloLetras():
        cadena = ""
        for posicion in range(MAX_PASSWORD_LENGTH - 1):
            cadena += secrets.choice(diccionario["letras"])
        return cadena

    # password.join(secrets.choice(tipo)) con ese comando podemos asignar a un strig que tome valores aleatorios de una lista (tipo)que le enviemos,

    def getPasswordSoloNumeros():
        cadena = ""
        for posicion in range(MAX_PASSWORD_LENGTH - 1):
            cadena += secrets.choice(diccionario["numeros"])
        return cadena

    def getPasswordLetrasNumeros():
        cadena = ""
        for posicion in range(MAX_PASSWORD_LENGTH - 1):
            cadena += secrets.choice(diccionario["letras"] + diccionario["numeros"])
        return cadena

    def getPasswordLetrasNumerosCaracteres():
        cadena = ""
        for posicion in range(MAX_PASSWORD_LENGTH - 1):
            cadena += secrets.choice(
                diccionario["letras"]
                + diccionario["numeros"]
                + diccionario["caracteres"]
            )
        return cadena

    def salida():
        eleccion = input("Confirma que desea salir? presione 'y' para salir: ")
        if eleccion == "y":
            sys.exit()

    def mostrarOpcionesMenu():
        cadena = "_" * 30
        print("\t-" + cadena + "W E L C O M E" + cadena + "-")
        print(f"\t\t\t\tGenerador de Contraseñas V0.1")
        print("\t*>>" + cadena + " ( * o * ) " + cadena + "<<*")
        print("\nSeleccione una de las siguientes opciones:\n\n")
        print("\t>> 1. Generar contraseña solo de Letras.")
        print("\t>> 2. Generar contraseña solo de Números.")
        print("\t>> 3. Generar contraseña Letras y Números.")
        print("\t>> 4. Generar contraseña Letras , Números y Caracteres.")
        print("\t>> 0. Salir.\n")

    def ingresarOpcionValida(opcionStr):
        opcionAValidar = 0
        if opcionStr.isdigit():
            # si el caracter ingresado es numérico entonces valida que sea un valor dentro de las opciones disponibles, sino itera hasta conseguir un número dentro del rango de las opciones del Menú.
            opcionAValidar = int(opcionStr)
            while (
                opcionAValidar < 0 or opcionAValidar > MAX_OPCION
            ):  # valida que se ingrese una opción válida
                print("error, ingrese opción válida")
                opcionStr = input(f"(0-{MAX_OPCION}) >\t")
                if opcionStr.isdigit():
                    opcionAValidar = int(opcionStr)
        else:
            opcionAValidar = (
                -1
            )  # valor de opción inválida en caso que el caracter ingresado no sea numérico.
        return opcionAValidar

    def procesarOpcionElegida(opcionElegida):
        if opcionElegida == int(opcionSalida):
            passwd = ""
            salida()
        elif opcionElegida == 1:
            passwd = getPasswordSoloLetras()
        elif opcionElegida == 2:
            passwd = getPasswordSoloNumeros()
        elif opcionElegida == 3:
            passwd = getPasswordLetrasNumeros()
        elif opcionElegida == 4:
            passwd = getPasswordLetrasNumerosCaracteres()
        else:
            print(f"Opción no válida - Ingrese un número del 0 al {MAX_OPCION}")
        return passwd

    # loop del programa principal
    while salir == False:
        # os.system("clear")  # en windows comentar esta linea
        os.system("cls")  # en windows DESCOMENTAR esta linea
        mostrarOpcionesMenu()
        opcionStr = input(f"\t>> Escriba la opcion seleccionada: ")
        opcion = ingresarOpcionValida(opcionStr)
        if opcion >= 0 and opcion <= int(MAX_OPCION):
            password = procesarOpcionElegida(opcion)
            mostrarPasswordObtenida(password)
        else:
            print(f"Opción no válida - Ingrese un número del 0 al {MAX_OPCION}")
            input("Presione una tecla para continuar. ")

    # Fin Función principal


if __name__ == "__main__":
    main()
