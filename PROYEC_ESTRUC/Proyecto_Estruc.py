from ayudas import MenuPR
from CargosED import categ
from DepartED import depar
from EmpleaED import empleados
from validaciones import validacion
import os

menupr = MenuPR()
lista = ["1.) Cargo","2.) Departamento","3.) Empleados","4.) Salir"]
opcion =""
while opcion != "4":
  os.system("cls")
  opcion= menupr.menu(lista,"MENÚ FICHA PRINCIPAL")
  if opcion == "1":
    opci1 = ""
    while opci1 != "3":
      os.system("cls")
      opci1 = menupr.menu(["1.) Ingreso","2.) Consulta","3.) Salir"],"MANTENIMIENTO DE CARGOS")
      os.system("cls")
      if opci1 == "1":
        while True:
          os.system("cls")
          print("*"*10,"Ingreso de cargos","*"*10)
          name = input("Nombre de cargos: ")
          if len(name)>=1 and len(name)<=20:
            break
          else:
            input("Cargo invalido, precione una tecla para volver a ingresar el cargo...")    
        art = categ(name)
        cargg = art.registro()
        categ.categori.append(cargg)
        input("datos ingresados satisfactoriamente,precione una tecla para continuar:")
      elif opci1 == "2":
        print("*"*15,"LISTADO DE CARGOS","*"*15)
        print("Codigo"," "*7,"Cargo")
        for art in categ.categori:
          codg = art["Codigo"]
          carg = art["Cargo"]
          print(" "*2,codg," "*8,carg)
        input("Precione una tecla para continuar...")
      
  elif opcion == "2":
    opci2 =""
    while opci2 != "3":
      os.system("cls")
      opci2 = menupr.menu(["1.) Ingreso","2.) Consulta","3.) Salir"],"MANTENIMIENTO DE DEPARTAMENTOS")
      os.system("cls")
      if opci2 == "1":
        while True:
          os.system("cls")
          print("*"*10,"Ingreso de departamentos","*"*10)
          namedp = input("Nombre del departamento: ")
          if len(namedp)>=5 and len(namedp)<=20:
            break
          else:
            input("Departamento invalido, precione una tecla para volver a ingresar el departamento...")  
        dep = depar(namedp)
        deppar = dep.registro()
        depar.catengg.append(deppar)
        input ("Datos agregados correctamente,Precione una tecla para continuar...")
      elif opci2 == "2":
        print("*"*15,"LISTADO DE DEPARTAMENTOS","*"*15)
        print("Codigo"," "*7,"Departamento")
        for dep in depar.catengg:
          coddg = dep["Codigo"]
          departs = dep["Departamento"]
          print(" "*2,coddg," "*10,departs)
        input("Pecione una tecla para continuar...")

  elif opcion == "3":
    opci3 =""
    while opci3 != "3":
      os.system("cls")
      opci3 = menupr.menu(["1.) Ingreso","2.) Consulta","3.) Salir"],"MANTENIMIENTO DE EMPLEADOS")
      os.system("cls")
      if opci3 == "1":
        while True:
          os.system("cls")
          print("*"*10,"Ingreso de Empleados","*"*10)
          nombre = input("Ingrese nombre: ")
          if len(nombre)>=3 and len(nombre)<=20:
            break
          else:
            input("ERROR, precione una tecla para volver a ingresar...")
        while True:
          os.system("cls")
          print("*"*10,"Ingreso de Empleados","*"*10)
          cedula = input("Ingrese cedula: ")
          if any ([c.isalpha() for c in cedula]):
            print("El ingreso debe ser solo de digitos")       
          else:
            if len(cedula)== 10:
              break
            else:
              input("Cedula invalida, precione una tecla para volver a ingresar...")
        while True:
          os.system("cls")
          print("*"*10,"Ingreso de Empleados","*"*10)
          cargo=int(input("Ingrese codigo del cargo: "))
          ca=validacion.valid_Cargo(cargo)
          if cargo ==ca:
            input("no existe el cargo, presione una tecla para volver a ingresar...")
          else:
            break
        while True:
          os.system("cls")
          print("*"*10,"Ingreso de Empleados","*"*10)
          departa = int(input("Ingrese codigo del departamento: "))
          depr = validacion.valid_Depart(departa)
          if departa == depr:
            input("no existe el departamento, presione una tecla para volver a ingresar...")
          else:
            break   
        while True:
          os.system("cls")
          print("*"*10,"Ingreso de Empleados","*"*10)
          sueldo = float(input("Ingrese el sueldo: "))
          sield= validacion.valid_Sueldo(sueldo)
          if sueldo ==sield:
            input("debe ingresar el sueldo en valor decimal, precione una tecla para volver a ingrsar...")
          else:
            break    
        emple = empleados(nombre,cedula,cargo,departa,sueldo)
        emp = emple.registro()
        empleados.emplea2.append(emp)
        input("Datos ingresados correctamente, presiones una tecla para continuar...")

      elif opci3 == "2":
        print("*"*20,"LISTADO DE EMPLEADOS","*"*20)
        print("Codigo"," "*5,"Nombre"," "*7,"Cedula"," "*6,"Cargo"," "*6,"Departamento"," "*6,"Sueldo")
        for emple in empleados.emplea2:
          codIG = emple["Codigo"]
          nombree = emple["Nombre"]
          cedul = emple["Cedula"]
          car = emple["Cargo"]
          car = validacion.valid_Cargo(car) 
          depa = emple["Departamento"]
          depa =validacion.valid_Depart(depa)
          suel = emple["Sueldo"]
          print(" "*2,codIG," "*7,nombree," "*(11-len(nombree)),cedul," "*(13-len(cedul)),car," "*(14-len(car)),depa," "*9,suel)
        input("Precione una tecla para continuar...")
        