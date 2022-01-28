
class empleados:
    secuen =1
    emplea2 = [{"Codigo":1,"Nombre":"Dan","Cedula":"0914192182","Cargo":1,"Departamento":1,"Sueldo":500.50}]
    def __init__(self,nombre,cedula,codiCargo,codiDepar,sueldo):
        empleados.secuen +=1
        self.codig = empleados.secuen
        self.nombre = nombre
        self.cedula = cedula
        self.cargo = codiCargo
        self.depart= codiDepar
        self.sueldd = sueldo
    def mostrar(self):
        print("{} - {} - {} - {} - {} - {}".format(self.codig,self.nombre,self.cedula,self.cargo,self.depart,self.sueldd))

    # def datos(self):
    #     return[self.codig,self.nombre,self.cedula,self.cargo,self.depart,self.sueldd]
    def registro(self):
        return{"Codigo":self.codig,"Nombre":self.nombre,"Cedula":self.cedula,"Cargo":self.cargo,"Departamento":self.depart,"Sueldo":self.sueldd}