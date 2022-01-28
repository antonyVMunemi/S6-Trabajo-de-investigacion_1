# import os
# os.system("cls")

class MenuPR:
  def __init__(self):
    pass
  def menu(self,opciones,titulo):
    print(titulo)
    for opcion in opciones:
      print(opcion)
    opci = input("Elija opccion[1...{}]: ".format(len(opciones)))
    return opci

# ayuda = MenuPR()
# lista = ["1.) Cargo","2.) Departamento","3.) Empleados","4.) Salir"]
# opcion = ayuda.menu(lista)
# print(opcion)
  