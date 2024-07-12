import random
import statistics
import csv

def asignarSueldos(trabajadores,sueldos):
    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000)
        sueldos[trabajador] = sueldo
        
    print(sueldos)
    print("Sueldos asignados exitosamente")

    return sueldos

def clasificarSueldos(sueldos):
    menor_800 = {}
    entre_800_2m = {}
    mayor_2m = {}

    for trabajador,sueldo in sueldos.items():
        if sueldo < 800000:
            menor_800[trabajador] = sueldo
        elif sueldo <= 2000000:
            entre_800_2m[trabajador] = sueldo
        else:
            mayor_2m[trabajador] = sueldo

    print("Sueldos menores a $800.000 Total: ", len(menor_800))
    print("")
    print("Nombre trabajador - Sueldo")
    for trabajador,sueldo in menor_800.items():
        print(trabajador,"$",sueldo)
    print("")

    print("Sueldos entre $800.000 y $2.000.000 Total: ", len(entre_800_2m))
    print("")
    print("Nombre trabajador - Sueldo")
    for trabajador,sueldo in entre_800_2m.items():
        print(trabajador,"$",sueldo)
    print("")

    print("Sueldos mayores a $2.000.000 Total: ", len(mayor_2m))
    print("")
    print("Nombre trabajador - Sueldo")
    for trabajador,sueldo in mayor_2m.items():
        print(trabajador,"$",sueldo)
    print("")

def verEstadisticas(sueldos,trabajadores):
    max_sueldo = 0
    min_sueldo = 999999999999
    suma_sueldos = 0
    promedio_sueldos = 0

    for trabajador,sueldo in sueldos.items():
        if sueldo > max_sueldo:
            max_sueldo = sueldo

    for trabajador,sueldo in sueldos.items():
        if sueldo < min_sueldo:
            min_sueldo = sueldo

    for trabajador,sueldo in sueldos.items():
        suma_sueldos = suma_sueldos + sueldo
    promedio_sueldos = suma_sueldos / len(trabajadores)

    print("El sueldo mas alto es: ",max_sueldo)
    print("El sueldo mas bajo es: ",min_sueldo)
    print("El promedio de sueldos es: ",promedio_sueldos)

def reporteSueldos(sueldos):
    reporte = {}
    for trabajador,sueldo in sueldos.items():
        descSalud = sueldo * 0.07
        descAFP = sueldo * 0.12
        sueldoLiquido = sueldo - descSalud - descAFP
        print("Trabajador: ",trabajador,"Sueldo Base: ",sueldo,"Descuento Salud: ",descAFP,"Sueldo Liquido: ",sueldoLiquido)

        
    with open("reporteSueldos","w",newline="") as archivo:
        escritor = csv.writer(archivo,delimiter=",")
        escritor.writerow(["Trabajador","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Liquido"])
        for trabajador,sueldo in sueldos.items():
            escritor.writerow([trabajador,sueldo])




