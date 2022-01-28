class categ:
    secuencia = 2
    categori = [{"Codigo":1,"Cargo":"Analista"},{"Codigo":2,"Cargo":"Jefe"}]
    def __init__(self,categoria):
        categ.secuencia +=1
        self.codigo = categ.secuencia
        self.descripcion = categoria
    def mostrar(self):
        print("{} - {}".format(self.codigo,self.descripcion))

    def datos(self):
        return [self.codigo,self.descripcion]
    def registro(self):
        return {"Codigo":self.codigo,"Cargo":self.descripcion}    

#listacate = []
#cate = categ("Analista")
#cate.mostrar()
#categ.secuencia = 2
#print(cate.datos())
#cate2 = categ("Jefe")
#cate2.mostrar()
#print(cate2.datos())
# listacate.append(cate.datos())
# listacate.append(cate2.datos())
# cate = categ("Secretaria")
# categ.categori.append(cate.registro())
# cate = categ("consejero")
# categ.categori.append(cate.registro())
# print(categ.categori)
#listacate.append(cate2.registro())
#listacate.append(cate3.registro())
#print(listacate)
