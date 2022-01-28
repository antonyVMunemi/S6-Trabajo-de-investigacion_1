
from CargosED import categ
from DepartED import depar


class validacion:

    def valid_Cargo(codIG):
        carg = 0
        for posi in range(0,len(categ.categori)):
            cargod = categ.categori[posi]
            if cargod["Codigo"] == codIG:
                carg = cargod["Cargo"]
                break
        return carg

    def valid_Depart(deppart):
        dep = 0
        for pos in range(0,len(depar.catengg)):
            depard = depar.catengg[pos]
            if depard["Codigo"] == deppart:
                dep = depard["Departamento"]
                break
        return dep

    def valid_Sueldo(sueldo):
        try:
            sueldo=float(sueldo)
            return True
        except ValueError:
            return False