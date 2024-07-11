from fun import *

while True:
    os.system("cls")
    print("""
          ----MENU----
    [1] Asignar sueldos aleatorios
    [2] Clasificar sueldos
    [3] Ver estadísticas.
    [4] Reporte de sueldos
    [5] Salir del programa""")
    opc = input("Ingrese una opcion > ")
    os.system("cls")
    if opc == "1":
        sueldos_a ()
    elif opc == "2":
        clasificar ()
    elif opc == "3":
        estadísticas()
    elif opc == "4":
        reporte ()
    elif opc == "5":
        Salir()
    else:
        print ("ERROR OPCION INCORRECTA")
    time.sleep(4)