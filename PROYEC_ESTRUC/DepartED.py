class depar:
    secuencia = 0
    catengg =[]
    def __init__(self,catteg):
        depar.secuencia +=1
        self.codg = depar.secuencia
        self.descrip = catteg
    def mostrar(self):
        print("{} - {}".format(self.codg,self.descrip))

    def datos(self):
        return [self.codg,self.descrip]
    def registro(self):
        return {"Codigo":self.codg,"Departamento":self.descrip}