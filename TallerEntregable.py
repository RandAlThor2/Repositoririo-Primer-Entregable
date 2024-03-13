class Implante:
    def __init__(self):
        self.__medResponsable = ""
        self.__estado = ""
        self.__fechaRevision = ""
        self.__mantenimiento = ""

    def get_medResponsable(self):
        return self.__medResponsable
    def get_estado(self):
        return self.__estado
    def get_fechaRevision(self):
        return self.__fechaRevision
    def gset_mantenimiento(self):
        return self.__mantenimiento
    
    def set_medResponsable(self, med):
        self.__medResponsable = med
    def set_estado(self, est):
        self.__estado = est
    def set_fechaRevision(self, frev):
        self.__fechaRevision = frev
    def set_mantenimiento(self, man):
        self.__mantenimiento = man

class ImplanteRodilla:
    def __init__(self, medResponsable, estado, fechaRevision, mantenimiento):
        super().__init__(medResponsable, estado, fechaRevision, mantenimiento)
        self.__material = ""
        self.__tipoFijacion = ""
        self.__tamaño = float

    def get_material(self):
        return self.__material
    def get_tipoFijacion(self):
        return self.__tipoFijacion
    def get_tamaño(self):
        return self.__tamaño
    
    def set_material(self, mat):
        self.__material = mat
    def set_tipoFijacion(self, tf):
        self.__tipoFijacion = tf
    def set_tamaño(self, tam):
        self.__tamaño = tam

class ImplanteCadera:
    def __init__(self, medResponsable, estado, fechaRevision, mantenimiento):
        super().__init__(medResponsable, estado, fechaRevision, mantenimiento)
        self.__material = ""
        self.__tipoFijacion = ""
        self.__tamaño = float

    def get_material(self):
        return self.__material
    def get_tipoFijacion(self):
        return self.__tipoFijacion
    def get_tamaño(self):
        return self.__tamaño
    
    def set_material(self, mat):
        self.__material = mat
    def set_tipoFijacion(self, tf):
        self.__tipoFijacion = tf
    def set_tamaño(self, tam):
        self.__tamaño = tam

class ImplanteDental:
    def __init__(self, medResponsable, estado, fechaRevision, mantenimiento):
        super().__init__(medResponsable, estado, fechaRevision, mantenimiento)
        self.__material = ""
        self.__forma = ""
        self.__sistFijacion = ""

    def get_material(self):
        return self.__material
    def get_forma(self):
        return self.__forma
    def get_sistFijacion(self):
        return self.__sistFijacion
    
    def set_material(self, mat):
        self.__material = mat
    def set_forma(self, f):
        self.__forma = f
    def set_sistFijacion(self, sf):
        self.__sistFijacion = sf

class StentCoronario:
    def __init__(self, medResponsable, estado, fechaRevision, mantenimiento):
        super().__init__(medResponsable, estado, fechaRevision, mantenimiento)
        self.__material = ""
        self.__longitud = float
        self.__diametro = float

    def get_material(self):
        return self.__material
    def get_longitud(self):
        return self.__longitud
    def get_diametro(self):
        return self.__diametro
    
    def set_material(self, mat):
        self.__material = mat
    def set_longitud(self, l):
        self.__longitud = l
    def set_diametro(self, d):
        self.__diametro = d

class Marcapasos:
    def __init__(self, medResponsable, estado, fechaRevision, mantenimiento):
        super().__init__(medResponsable, estado, fechaRevision, mantenimiento)
        self.__nElectrodos = int
        self.__formConexion = ""
        self.__fEstimulacion = ""

    def get_nElectrodos(self):
        return self.__nElectrodos
    def get_formConexion(self):
        return self.__formConexion
    def get_fEstimulacion(self):
        return self.__fEstimulacion
    
    def set_nElectrodos(self, ne):
        self.__nElectrodos = ne
    def set_formConexion(self, fc):
        self.__formConexion = fc
    def set_fEstimulacion(self, fe):
        self.__fEstimulacion = fe

class Paciente:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = int
        self.__genero = ""
        self.__listaimplantes = []
        
    def get_Nombre(self):
        return self.__nombre
    def get_Cedula(self):
        return self.__cedula
    def get_Genero(self):
        return self.__genero
    def get_listaImplantesPac(self):
        return self.__listaimplantes
    
    def set_Nombre(self,n):
        self.__nombre = n   
    def set_Cedula(self,c):
        self.__cedula = c
    def set_Genero(self,g):
        self.__genero = g

    def agregarimplante(self, id, ob):
        self.get_listaImplantesPac()[id].get_listaImplantesPac.append(ob)
        return print("Implante ingresado")

class Sistema:
    def __init__(self):
        self.__pacientes = {}
        self.__implantes = {
            "ImplanteRodilla" : {},
            "ImplanteCadera" : {},
            "ImplanteDental" : {},
            "StentCoronario" : {},
            "Marcapasos" : {}
        }

    def get_implantes(self):
        return self.__implantes
    def get_pacientes(self):
        return self.__pacientes
    
    def verificarExistePac(self, id):
        if id in self.__pacientes:
            return True
        else:
            return False        
    def verificarExisteImp(self, tipoimp, id_):
        if tipoimp == 1:
            if id_ in self.__implantes["ImplanteRodilla"]:
                return True
        elif tipoimp == 2:
            if id_ in self.__implantes["ImplanteCadera"]:
                return True
        elif tipoimp == 3:
            if id_ in self.__implantes["ImplanteDental"]:
                return True
        elif tipoimp == 4:
            if id_ in self.__implantes["StentCoronario"]:
                return True
        elif tipoimp == 5:
            if id_ in self.__implantes["Marcapasos"]:
                return True
        else:
            return False
            
    def agregarPac(self, id_, ob):
        a = self.verificarExiste()
        if a:
            self.get_pacientes()[id_] = ob
            return False
        else: 
            return True    
    def agregarImp(self, id_, tipoimp, ob):
        a = self.verificarExisteImp(tipoimp, id_)
        if a:
            return print(f"El implante tipo {tipoimp} con {id_} ya se halla en la base de datos")
        else:
            if tipoimp == 1:
                self.get_implantes["ImplanteRodilla"][id_] = ob
                return print("Implante de Rodilla ingresado")
            elif tipoimp == 2:
                self.get_implantes["ImplanteCadera"][id_] = ob
                return print("Implante de Cadera ingresado")
            elif tipoimp == 3:
                self.get_implantes["ImplanteDental"][id_] = ob
                return print("Implante Dental ingresado")
            elif tipoimp == 4:
                self.get_implantes["StentCoronario"][id_] = ob
                return print("StentCoronario ingresado")
            elif tipoimp == 5:
                self.get_implantes["Marcapasos"][id_] = ob
                return print("Marcapasos ingresado")
            
    def editarInfoImplanRo(self, id_, mat, tf, tam, med, est, frev, man, tipoimp=1):
        a = self.verificarExisteImp(tipoimp, id_)
        if a == False:
            return print(f"El implante tipo {tipoimp} con {id_} no se halla en la base de datos")
        else:
            self.get_implantes[tipoimp][id_].set_material(mat)
            self.get_implantes[tipoimp][id_].set_tipoFijacion(tf)
            self.get_implantes[tipoimp][id_].set_tamaño(tam)
            self.get_implantes[tipoimp][id_].set_medResponsable(med)
            self.get_implantes[tipoimp][id_].set_estado(est)
            self.get_implantes[tipoimp][id_].set_fechaRevision(frev)
            self.get_implantes[tipoimp][id_].set_mantenimiento(man)
            return print("Cambios modificados con éxito")
    def editarInfoImplanCa(self, id_, mat, tf, tam, med, est, frev, man, tipoimp=2):
        a = self.verificarExisteImp(tipoimp, id_)
        if a == False:
            return print(f"El implante tipo {tipoimp} con {id_} no se halla en la base de datos")
        else:
            self.get_implantes[tipoimp][id_].set_material(mat)
            self.get_implantes[tipoimp][id_].set_tipoFijacion(tf)
            self.get_implantes[tipoimp][id_].set_tamaño(tam)
            self.get_implantes[tipoimp][id_].set_medResponsable(med)
            self.get_implantes[tipoimp][id_].set_estado(est)
            self.get_implantes[tipoimp][id_].set_fechaRevision(frev)
            self.get_implantes[tipoimp][id_].set_mantenimiento(man)
            return print("Cambios modificados con éxito")
    def editarInfoImplanDe(self, id_, mat, f, sf, med, est, frev, man, tipoimp=3):
        a = self.verificarExisteImp(tipoimp, id_)
        if a == False:
            return print(f"El implante tipo {tipoimp} con {id_} no se halla en la base de datos")
        else:
            self.get_implantes[tipoimp][id_].set_material(mat)
            self.get_implantes[tipoimp][id_].set_forma(f)
            self.get_implantes[tipoimp][id_].set_sistFijacion(sf)
            self.get_implantes[tipoimp][id_].set_medResponsable(med)
            self.get_implantes[tipoimp][id_].set_estado(est)
            self.get_implantes[tipoimp][id_].set_fechaRevision(frev)
            self.get_implantes[tipoimp][id_].set_mantenimiento(man)
            return print("Cambios modificados con éxito")
    def editarInfoStent(self, id_, mat, l, d, med, est, frev, man, tipoimp=4):
        a = self.verificarExisteImp(tipoimp, id_)
        if a == False:
            return print(f"El implante tipo {tipoimp} con {id_} no se halla en la base de datos")
        else:
            self.get_implantes[tipoimp][id_].set_material(mat)
            self.get_implantes[tipoimp][id_].set_longitud(l)
            self.get_implantes[tipoimp][id_].set_diametro(d)
            self.get_implantes[tipoimp][id_].set_medResponsable(med)
            self.get_implantes[tipoimp][id_].set_estado(est)
            self.get_implantes[tipoimp][id_].set_fechaRevision(frev)
            self.get_implantes[tipoimp][id_].set_mantenimiento(man)
            return print("Cambios modificados con éxito")
    def editarInfoMarcapasos(self, id_, ne, fc, fe, med, est, frev, man, tipoimp=5):   
        a = self.verificarExisteImp(tipoimp, id_)
        if a == False:
            return print(f"El implante tipo {tipoimp} con {id_} no se halla en la base de datos")
        else:
            self.get_implantes[tipoimp][id_].set_nElectrodos(ne)
            self.get_implantes[tipoimp][id_].set_formConexion(fc)
            self.get_implantes[tipoimp][id_].set_fEstimulacion(fe)
            self.get_implantes[tipoimp][id_].set_medResponsable(med)
            self.get_implantes[tipoimp][id_].set_estado(est)
            self.get_implantes[tipoimp][id_].set_fechaRevision(frev)
            self.get_implantes[tipoimp][id_].set_mantenimiento(man)
            return print("Cambios modificados con éxito")     

    def eliminarImp(self, id_, tipoimp):
        a = self.verificarExisteImp(tipoimp, id_)
        if a == False:
            return print(f"El implante tipo {tipoimp} con {id_} no se halla en la base de datos")
        else: 
            del self.__implantes[tipoimp][id_]
            return print("Artículo eliminado con éxito")

    def verInventarioTotal(self):
        print("\nInformación de Implantes:")
        print("\nImplantes de Rodilla:")
        dic_rod = self.get_implantes()["ImplanteRodilla"]
        for implante_id, implante_info in dic_rod.items():
            print(f"Implante ID: {implante_id}")
            print(f"Tipo fijación: {implante_info.get_tipoFijacion()}")
            print(f"Tamaño: {implante_info.get_tamaño()}")
            print(f"Médico responsable: {implante_info.get_medResponsable()}")
            print(f"Estado: {implante_info.get_estado()}")
            print(f"Fecha revisión: {implante_info.get_fechaRevision()}")
            print(f"Mantenimiento: {implante_info.get_mantenimiento()}")
        
        print("\nImplantes de Rodilla:")
        dic_cad = self.get_implantes()["ImplanteCadera"]
        for implante_id, implante_info in dic_cad.items():
            print(f"Implante ID: {implante_id}")
            print(f"Tipo fijación: {implante_info.get_tipoFijacion()}")
            print(f"Tamaño: {implante_info.get_tamaño()}")
            print(f"Médico responsable: {implante_info.get_medResponsable()}")
            print(f"Estado: {implante_info.get_estado()}")
            print(f"Fecha revisión: {implante_info.get_fechaRevision()}")
            print(f"Mantenimiento: {implante_info.get_mantenimiento()}")
        
        print("\nImplantes de Dentales:")
        dic_den = self.get_implantes()["ImplanteDental"]
        for implante_id, implante_info in dic_den.items():
            print(f"Implante ID: {implante_id}")
            print(f"Material: {implante_info.get_material()}")
            print(f"Forma: {implante_info.get_forma()}")
            print(f"Sistema de fijación: {implante_info.get_sistFijacion()}")
            print(f"Médico responsable: {implante_info.get_medResponsable()}")
            print(f"Estado: {implante_info.get_estado()}")
            print(f"Fecha revisión: {implante_info.get_fechaRevision()}")
            print(f"Mantenimiento: {implante_info.get_mantenimiento()}")
        
        print("\nStent Coronario:")
        dic_st = self.get_implantes()["StentCoronario"]
        for implante_id, implante_info in dic_st.items():
            print(f"Implante ID: {implante_id}")
            print(f"Material: {implante_info.get_material()}")
            print(f"Longitud: {implante_info.get_longitud()}")
            print(f"Diámetro: {implante_info.get_diametro()}")
            print(f"Médico responsable: {implante_info.get_medResponsable()}")
            print(f"Estado: {implante_info.get_estado()}")
            print(f"Fecha revisión: {implante_info.get_fechaRevision()}")
            print(f"Mantenimiento: {implante_info.get_mantenimiento()}")
 
        print("\nStent Coronario:")
        dic_st = self.get_implantes()["StentCoronario"]
        for implante_id, implante_info in dic_st.items():
            print(f"Implante ID: {implante_id}")
            print(f"Número de electrodos: {implante_info.get_nElectrodos()}")
            print(f"Forma de conexión: {implante_info.formConexion()}")
            print(f"Forma de estimulación: {implante_info.get_fEstimulacion()}")
            print(f"Médico responsable: {implante_info.get_medResponsable()}")
            print(f"Estado: {implante_info.get_estado()}")
            print(f"Fecha revisión: {implante_info.get_fechaRevision()}")
            print(f"Mantenimiento: {implante_info.get_mantenimiento()}")

#Creación clase implante
class Implante:
    def __init__(self):
        self.__medResponsable = ""
        self.__estado = ""
        self.__fechaRevision = ""
        self.__mantenimiento = ""

#Getters de la clase implante
    def get_medResponsable(self):
        return self.__medResponsable
    def get_estado(self):
        return self.__estado
    def get_fechaRevision(self):
        return self.__fechaRevision
    def gset_mantenimiento(self):
        return self.__mantenimiento
    
#Setters de la clase implante
    def set_medResponsable(self, med):
        self.__medResponsable = med
    def set_estado(self, est):
        self.__estado = est
    def set_fechaRevision(self, frev):
        self.__fechaRevision = frev
    def set_mantenimiento(self, man):
        self.__mantenimiento = man


#Creación clase ImplanteRodilla
class ImplanteRodilla:
    def __init__(self, medResponsable, estado, fechaRevision, mantenimiento):
        super().__init__(medResponsable, estado, fechaRevision, mantenimiento)
        self.__material = ""
        self.__tipoFijacion = ""
        self.__tamaño = float(0)

#getters clase ImplanteRodilla
    def get_material(self):
        return self.__material
    def get_tipoFijacion(self):
        return self.__tipoFijacion
    def get_tamaño(self):
        return self.__tamaño

#setters clase ImplanteRodilla
    def set_material(self, mat):
        self.__material = mat
    def set_tipoFijacion(self, tf):
        self.__tipoFijacion = tf
    def set_tamaño(self, tam):
        self.__tamaño = tam

#Creación clase ImplanteCadera
class ImplanteCadera:
    def __init__(self, medResponsable, estado, fechaRevision, mantenimiento):
        super().__init__(medResponsable, estado, fechaRevision, mantenimiento)
        self.__material = ""
        self.__tipoFijacion = ""
        self.__tamaño = float

#getters clase ImplanteCadera
    def get_material(self):
        return self.__material
    def get_tipoFijacion(self):
        return self.__tipoFijacion
    def get_tamaño(self):
        return self.__tamaño

#setters clase ImplanteCadera
    def set_material(self, mat):
        self.__material = mat
    def set_tipoFijacion(self, tf):
        self.__tipoFijacion = tf
    def set_tamaño(self, tam):
        self.__tamaño = tam

#creación clase ImplanteDental
class ImplanteDental:
    def __init__(self, medResponsable, estado, fechaRevision, mantenimiento):
        super().__init__(medResponsable, estado, fechaRevision, mantenimiento)
        self.__material = ""
        self.__forma = ""
        self.__sistFijacion = ""

#getters clase ImplanteDental
    def get_material(self):
        return self.__material
    def get_forma(self):
        return self.__forma
    def get_sistFijacion(self):
        return self.__sistFijacion

#setters clase ImplanteDental
    def set_material(self, mat):
        self.__material = mat
    def set_forma(self, f):
        self.__forma = f
    def set_sistFijacion(self, sf):
        self.__sistFijacion = sf

#Creación clase StentCoronario
class StentCoronario:
    def __init__(self, medResponsable, estado, fechaRevision, mantenimiento):
        super().__init__(medResponsable, estado, fechaRevision, mantenimiento)
        self.__material = ""
        self.__longitud = float
        self.__diametro = float

#getters clase StentCoronario
    def get_material(self):
        return self.__material
    def get_longitud(self):
        return self.__longitud
    def get_diametro(self):
        return self.__diametro
    
#setters clase StentCoronario
    def set_material(self, mat):
        self.__material = mat
    def set_longitud(self, l):
        self.__longitud = l
    def set_diametro(self, d):
        self.__diametro = d

#creación clase Marcapasos
class Marcapasos:
    def __init__(self, medResponsable, estado, fechaRevision, mantenimiento):
        super().__init__(medResponsable, estado, fechaRevision, mantenimiento)
        self.__nElectrodos = int
        self.__formConexion = ""
        self.__fEstimulacion = ""

#getters clase Marcapasos
    def get_nElectrodos(self):
        return self.__nElectrodos
    def get_formConexion(self):
        return self.__formConexion
    def get_fEstimulacion(self):
        return self.__fEstimulacion

#setters clase Marcapasos
    def set_nElectrodos(self, ne):
        self.__nElectrodos = ne
    def set_formConexion(self, fc):
        self.__formConexion = fc
    def set_fEstimulacion(self, fe):
        self.__fEstimulacion = fe

#creación clase Paciente
class Paciente:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__listaimplantes = []

#getters clase Paciente     
    def get_Nombre(self):
        return self.__nombre
    def get_Cedula(self):
        return self.__cedula
    def get_Genero(self):
        return self.__genero
    def get_listaImplantesPac(self):
        return self.__listaimplantes

#setters clase Paciente
    def set_Nombre(self,n):
        self.__nombre = n   
    def set_Cedula(self,c):
        self.__cedula = c
    def set_Genero(self,g):
        self.__genero = g

    def agregarimplante(self, id, ob):
        self.get_listaImplantesPac()[id].get_listaImplantesPac.append(ob)
        return print("Implante ingresado")

#creación clase Sistema
#creación clase Sistema
class Sistema:
    def __init__(self):
        self.__pacientes = {}
        self.__implantes = {
            "ImplanteRodilla" : {},
            "ImplanteCadera" : {},
            "ImplanteDental" : {},
            "StentCoronario" : {},
            "Marcapasos" : {}
        }

#getters clase Sistema
    def get_implantes(self):
        return self.__implantes
    def get_pacientes(self):
        return self.__pacientes
    
    def verificarExistePac(self, id):
        if id in self.__pacientes:
            return True
        else:
            return False        
    def verificarExisteImp(self, tipoimp, id_):
        if tipoimp == 1:
            if id_ in self.__implantes["ImplanteRodilla"]:
                return True
        elif tipoimp == 2:
            if id_ in self.__implantes["ImplanteCadera"]:
                return True
        elif tipoimp == 3:
            if id_ in self.__implantes["ImplanteDental"]:
                return True
        elif tipoimp == 4:
            if id_ in self.__implantes["StentCoronario"]:
                return True
        elif tipoimp == 5:
            if id_ in self.__implantes["Marcapasos"]:
                return True
        else:
            return False
            
#setters clase Sistema
    def agregarPac(self, id_, ob):
        a = self.verificarExiste()
        if a:
            self.get_pacientes()[id_] = ob
            return False
        else: 
            return True    
    def agregarImp(self, id_, tipoimp, ob):
        a = self.verificarExisteImp(tipoimp, id_)
        if a:
            return print(f"El implante tipo {tipoimp} con {id_} ya se halla en la base de datos")
        else:
            if tipoimp == 1:
                self.get_implantes["ImplanteRodilla"][id_] = ob
                return print("Implante de Rodilla ingresado")
            elif tipoimp == 2:
                self.get_implantes["ImplanteCadera"][id_] = ob
                return print("Implante de Cadera ingresado")
            elif tipoimp == 3:
                self.get_implantes["ImplanteDental"][id_] = ob
                return print("Implante Dental ingresado")
            elif tipoimp == 4:
                self.get_implantes["StentCoronario"][id_] = ob
                return print("StentCoronario ingresado")
            elif tipoimp == 5:
                self.get_implantes["Marcapasos"][id_] = ob
                return print("Marcapasos ingresado")
            
    def editarInfoImplanRo(self, id_, mat, tf, tam, med, est, frev, man, tipoimp=1):
        a = self.verificarExisteImp(tipoimp, id_)
        if a == False:
            return print(f"El implante tipo {tipoimp} con {id_} no se halla en la base de datos")
        else:
            self.get_implantes()[tipoimp][id_].set_material(mat)
            self.get_implantes()[tipoimp][id_].set_tipoFijacion(tf)
            self.get_implantes()[tipoimp][id_].set_tamaño(tam)
            self.get_implantes()[tipoimp][id_].set_medResponsable(med)
            self.get_implantes()[tipoimp][id_].set_estado(est)
            self.get_implantes()[tipoimp][id_].set_fechaRevision(frev)
            self.get_implantes()[tipoimp][id_].set_mantenimiento(man)
            return print("Cambios modificados con éxito")
    def editarInfoImplanCa(self, id_, mat, tf, tam, med, est, frev, man, tipoimp=2):
        a = self.verificarExisteImp(tipoimp, id_)
        if a == False:
            return print(f"El implante tipo {tipoimp} con {id_} no se halla en la base de datos")
        else:
            self.get_implantes()[tipoimp][id_].set_material(mat)
            self.get_implantes()[tipoimp][id_].set_tipoFijacion(tf)
            self.get_implantes()[tipoimp][id_].set_tamaño(tam)
            self.get_implantes()[tipoimp][id_].set_medResponsable(med)
            self.get_implantes()[tipoimp][id_].set_estado(est)
            self.get_implantes()[tipoimp][id_].set_fechaRevision(frev)
            self.get_implantes()[tipoimp][id_].set_mantenimiento(man)
            return print("Cambios modificados con éxito")
    def editarInfoImplanDe(self, id_, mat, f, sf, med, est, frev, man, tipoimp=3):
        a = self.verificarExisteImp(tipoimp, id_)
        if a == False:
            return print(f"El implante tipo {tipoimp} con {id_} no se halla en la base de datos")
        else:
            self.get_implantes()[tipoimp][id_].set_material(mat)
            self.get_implantes()[tipoimp][id_].set_forma(f)
            self.get_implantes()[tipoimp][id_].set_sistFijacion(sf)
            self.get_implantes()[tipoimp][id_].set_medResponsable(med)
            self.get_implantes()[tipoimp][id_].set_estado(est)
            self.get_implantes()[tipoimp][id_].set_fechaRevision(frev)
            self.get_implantes()[tipoimp][id_].set_mantenimiento(man)
            return print("Cambios modificados con éxito")
    def editarInfoStent(self, id_, mat, l, d, med, est, frev, man, tipoimp=4):
        a = self.verificarExisteImp(tipoimp, id_)
        if a == False:
            return print(f"El implante tipo {tipoimp} con {id_} no se halla en la base de datos")
        else:
            self.get_implantes()[tipoimp][id_].set_material(mat)
            self.get_implantes()[tipoimp][id_].set_longitud(l)
            self.get_implantes()[tipoimp][id_].set_diametro(d)
            self.get_implantes()[tipoimp][id_].set_medResponsable(med)
            self.get_implantes()[tipoimp][id_].set_estado(est)
            self.get_implantes()[tipoimp][id_].set_fechaRevision(frev)
            self.get_implantes()[tipoimp][id_].set_mantenimiento(man)
            return print("Cambios modificados con éxito")
    def editarInfoMarcapasos(self, id_, ne, fc, fe, med, est, frev, man, tipoimp=5):   
        a = self.verificarExisteImp(tipoimp, id_)
        if a == False:
            return print(f"El implante tipo {tipoimp} con {id_} no se halla en la base de datos")
        else:
            self.get_implantes()[tipoimp][id_].set_nElectrodos(ne)
            self.get_implantes()[tipoimp][id_].set_formConexion(fc)
            self.get_implantes()[tipoimp][id_].set_fEstimulacion(fe)
            self.get_implantes()[tipoimp][id_].set_medResponsable(med)
            self.get_implantes()[tipoimp][id_].set_estado(est)
            self.get_implantes()[tipoimp][id_].set_fechaRevision(frev)
            self.get_implantes()[tipoimp][id_].set_mantenimiento(man)
            return print("Cambios modificados con éxito")     

    def eliminarImp(self, id_, tipoimp):
        a = self.verificarExisteImp(tipoimp, id_)
        if a == False:
            return print(f"El implante tipo {tipoimp} con {id_} no se halla en la base de datos")
        else: 
            del self.__implantes[tipoimp][id_]
            return print("Artículo eliminado con éxito")

    def verInventarioTotal(self):
        print("\nInformación de Implantes:")
        print("\nImplantes de Rodilla:")
        dic_rod = self.get_implantes()["ImplanteRodilla"]
        for implante_id, implante_info in dic_rod.items():
            print(f"Implante ID: {implante_id}")
            print(f"Tipo fijación: {implante_info.get_tipoFijacion()}")
            print(f"Tamaño: {implante_info.get_tamaño()}")
            print(f"Médico responsable: {implante_info.get_medResponsable()}")
            print(f"Estado: {implante_info.get_estado()}")
            print(f"Fecha revisión: {implante_info.get_fechaRevision()}")
            print(f"Mantenimiento: {implante_info.get_mantenimiento()}")
        
        print("\nImplantes de Rodilla:")
        dic_cad = self.get_implantes()["ImplanteCadera"]
        for implante_id, implante_info in dic_cad.items():
            print(f"Implante ID: {implante_id}")
            print(f"Tipo fijación: {implante_info.get_tipoFijacion()}")
            print(f"Tamaño: {implante_info.get_tamaño()}")
            print(f"Médico responsable: {implante_info.get_medResponsable()}")
            print(f"Estado: {implante_info.get_estado()}")
            print(f"Fecha revisión: {implante_info.get_fechaRevision()}")
            print(f"Mantenimiento: {implante_info.get_mantenimiento()}")
        
        print("\nImplantes de Dentales:")
        dic_den = self.get_implantes()["ImplanteDental"]
        for implante_id, implante_info in dic_den.items():
            print(f"Implante ID: {implante_id}")
            print(f"Material: {implante_info.get_material()}")
            print(f"Forma: {implante_info.get_forma()}")
            print(f"Sistema de fijación: {implante_info.get_sistFijacion()}")
            print(f"Médico responsable: {implante_info.get_medResponsable()}")
            print(f"Estado: {implante_info.get_estado()}")
            print(f"Fecha revisión: {implante_info.get_fechaRevision()}")
            print(f"Mantenimiento: {implante_info.get_mantenimiento()}")
        
        print("\nStent Coronario:")
        dic_st = self.get_implantes()["StentCoronario"]
        for implante_id, implante_info in dic_st.items():
            print(f"Implante ID: {implante_id}")
            print(f"Material: {implante_info.get_material()}")
            print(f"Longitud: {implante_info.get_longitud()}")
            print(f"Diámetro: {implante_info.get_diametro()}")
            print(f"Médico responsable: {implante_info.get_medResponsable()}")
            print(f"Estado: {implante_info.get_estado()}")
            print(f"Fecha revisión: {implante_info.get_fechaRevision()}")
            print(f"Mantenimiento: {implante_info.get_mantenimiento()}")
 
        print("\nStent Coronario:")
        dic_st = self.get_implantes()["StentCoronario"]
        for implante_id, implante_info in dic_st.items():
            print(f"Implante ID: {implante_id}")
            print(f"Número de electrodos: {implante_info.get_nElectrodos()}")
            print(f"Forma de conexión: {implante_info.formConexion()}")
            print(f"Forma de estimulación: {implante_info.get_fEstimulacion()}")
            print(f"Médico responsable: {implante_info.get_medResponsable()}")
            print(f"Estado: {implante_info.get_estado()}")
            print(f"Fecha revisión: {implante_info.get_fechaRevision()}")
            print(f"Mantenimiento: {implante_info.get_mantenimiento()}")  

    def agregarImaPa():
        dddd


def main():
    servicio_implantes = Sistema()
    while True:
        menu = int(input("Bienvenido al sistema, ingrese una opción:\n 1- Agregar Implante \n2-Eliminar implante \n3-Editar información de implante \n4-Visualizar inventario"))

main()

