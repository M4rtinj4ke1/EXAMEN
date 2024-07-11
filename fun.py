import os,time,csv,random
sueldo = []
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández",
                "MiguelSánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
def sueldos_a ():
    for x in trabajadores:
        sueldos = random.randint (300000,2500000)
        trabajador = print("Trabajador",x,":",sueldos)
        sueldo.append(sueldos)
        sueldo.append(trabajador)
def clasificar ():
    pass
def estadísticas():
    sueldos = random.randint (300000,2500000)
    if sueldos >= 800000:
        print ("Sueldo mas alto es:",sueldo)
    
    if sueldos <= 800000:
        print ("Sueldo mas bajo:",sueldo)
def reporte ():
    with open ("archivo.csv","x", newline="") as file:
        escritor = csv.writer(file)
        escritor.writerow(trabajadores)
        escritor.writerow(sueldo)
    
    print("ARCHIVO CREADO CON EXITO")
def Salir():
    print ("Finalizando programa.")
    time.sleep(1)
    os.system("cls")
    print ("Finalizando programa..")
    time.sleep(1)
    os.system("cls")
    print ("Finalizando programa...")
    time.sleep(1)
    os.system("cls")
    print("Desarrollado por Martin Jaque")
    print("21.913.464-9")
    exit()