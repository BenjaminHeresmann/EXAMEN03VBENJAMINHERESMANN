import funciones as fn

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos = {}

while True:
    try:
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de1 sueldos")
        print("5. Salir del programa")

        opcionMenu = int(input("Digite opcion (1-5): "))

        if opcionMenu == 1:
            sueldos = fn.asignarSueldos(trabajadores,sueldos)

        elif opcionMenu == 2:
            fn.clasificarSueldos(sueldos)

        elif opcionMenu == 3:
            fn.verEstadisticas(sueldos,trabajadores)

        elif opcionMenu == 4:
            fn.reporteSueldos(sueldos)

        elif opcionMenu == 5:
            print("Finalizando programa...")
            print("Desarrollado por Benjamin Heresmann")
            print("RUT 19.617.779-5")
            break

        else: 
            print("Por favor digite opcion valida")
    except:
        print("Por favor digite opcion valida")
