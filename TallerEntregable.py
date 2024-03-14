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
        self.__cedula = int
        self.__genero = ""
        self.__dicpacimplantes = {}

#getter clase paciente
    def get_Nombre(self):
        return self.__nombre
    def get_Cedula(self):
        return self.__cedula
    def get_Genero(self):
        return self.__genero
    def get_dicpacimplantes(self):
        return self.__dicpacimplantes
#getter clase paciente
    def set_Nombre(self,n):
        self.__nombre = n   
    def set_Cedula(self,c):
        self.__cedula = c
    def set_Genero(self,g):
        self.__genero = g

    def agregarimplante(self, id, ob):
        self.get_dicpacimplantes()[id] = ob
        return True

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
        a = self.verificarExistePac()
        if not a:
            self.get_pacientes()[id_] = ob
            return False
        else: 
            return True    
    def agregarImp(self, id_, tipoimp, ob):
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
            return print(f"El implante tipo Implante de  Rodilla con {id_} no se halla en la base de datos")
        else:
            self.get_implantes()["ImplanteRodilla"][id_].set_material(mat)
            self.get_implantes()["ImplanteRodilla"][id_].set_tipoFijacion(tf)
            self.get_implantes()["ImplanteRodilla"][id_].set_tamaño(tam)
            self.get_implantes()["ImplanteRodilla"][id_].set_medResponsable(med)
            self.get_implantes()["ImplanteRodilla"][id_].set_estado(est)
            self.get_implantes()["ImplanteRodilla"][id_].set_fechaRevision(frev)
            self.get_implantes()["ImplanteRodilla"][id_].set_mantenimiento(man)
            return print("Cambios modificados con éxito")
    def editarInfoImplanCa(self, id_, mat, tf, tam, med, est, frev, man, tipoimp=2):
        a = self.verificarExisteImp(tipoimp, id_)
        if a == False:
            return print(f"El implante tipo Implante de Cadera con {id_} no se halla en la base de datos")
        else:
            self.get_implantes()["ImplanteCadera"][id_].set_material(mat)
            self.get_implantes()["ImplanteCadera"][id_].set_tipoFijacion(tf)
            self.get_implantes()["ImplanteCadera"][id_].set_tamaño(tam)
            self.get_implantes()["ImplanteCadera"][id_].set_medResponsable(med)
            self.get_implantes()["ImplanteCadera"][id_].set_estado(est)
            self.get_implantes()["ImplanteCadera"][id_].set_fechaRevision(frev)
            self.get_implantes()["ImplanteCadera"][id_].set_mantenimiento(man)
            return print("Cambios modificados con éxito")
    def editarInfoImplanDe(self, id_, mat, f, sf, med, est, frev, man, tipoimp=3):
        a = self.verificarExisteImp(tipoimp, id_)
        if a == False:
            return print(f"El implante tipo Implante Dental con {id_} no se halla en la base de datos")
        else:
            self.get_implantes()["ImplanteDental"][id_].set_material(mat)
            self.get_implantes()["ImplanteDental"][id_].set_forma(f)
            self.get_implantes()["ImplanteDental"][id_].set_sistFijacion(sf)
            self.get_implantes()["ImplanteDental"][id_].set_medResponsable(med)
            self.get_implantes()["ImplanteDental"][id_].set_estado(est)
            self.get_implantes()["ImplanteDental"][id_].set_fechaRevision(frev)
            self.get_implantes()["ImplanteDental"][id_].set_mantenimiento(man)
            return print("Cambios modificados con éxito")
    def editarInfoStent(self, id_, mat, l, d, med, est, frev, man, tipoimp=4):
        a = self.verificarExisteImp(tipoimp, id_)
        if a == False:
            return print(f"El implante tipo Stent Coronario con {id_} no se halla en la base de datos")
        else:
            self.get_implantes()["StentCoronario"][id_].set_material(mat)
            self.get_implantes()["StentCoronario"][id_].set_longitud(l)
            self.get_implantes()["StentCoronario"][id_].set_diametro(d)
            self.get_implantes()["StentCoronario"][id_].set_medResponsable(med)
            self.get_implantes()["StentCoronario"][id_].set_estado(est)
            self.get_implantes()["StentCoronario"][id_].set_fechaRevision(frev)
            self.get_implantes()["StentCoronario"][id_].set_mantenimiento(man)
            return print("Cambios modificados con éxito")
    def editarInfoMarcapasos(self, id_, ne, fc, fe, med, est, frev, man, tipoimp=5):   
        a = self.verificarExisteImp(tipoimp, id_)
        if a == False:
            return print(f"El implante tipo Marcapasos con {id_} no se halla en la base de datos")
        else:
            self.get_implantes()["Marcapasos"][id_].set_nElectrodos(ne)
            self.get_implantes()["Marcapasos"][id_].set_formConexion(fc)
            self.get_implantes()["Marcapasos"][id_].set_fEstimulacion(fe)
            self.get_implantes()["Marcapasos"][id_].set_medResponsable(med)
            self.get_implantes()["Marcapasos"][id_].set_estado(est)
            self.get_implantes()["Marcapasos"][id_].set_fechaRevision(frev)
            self.get_implantes()["Marcapasos"][id_].set_mantenimiento(man)
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
        dic_rod = self.get_implantes()["ImplanteRodilla"]
        if not dic_rod:
            print("No hay información disponible para los implantes de rodilla.")
        else:
            print("\nImplantes de Rodilla:")
            for implante_id, implante_info in dic_rod.items():
                print(f"Implante ID: {implante_id}")
                print(f"Tipo fijación: {implante_info.get_tipoFijacion()}")
                print(f"Tamaño: {implante_info.get_tamaño()}")
                print(f"Médico responsable: {implante_info.get_medResponsable()}")
                print(f"Estado: {implante_info.get_estado()}")
                print(f"Fecha revisión: {implante_info.get_fechaRevision()}")
                print(f"Mantenimiento: {implante_info.get_mantenimiento()}")
    
        dic_cad = self.get_implantes()["ImplanteCadera"]
        if not dic_cad:
            print("No hay información disponible para los implantes de rodilla.")
        else:
            print("\nImplantes de Cadera:")
            for implante_id, implante_info in dic_cad.items():
                print(f"Implante ID: {implante_id}")
                print(f"Tipo fijación: {implante_info.get_tipoFijacion()}")
                print(f"Tamaño: {implante_info.get_tamaño()}")
                print(f"Médico responsable: {implante_info.get_medResponsable()}")
                print(f"Estado: {implante_info.get_estado()}")
                print(f"Fecha revisión: {implante_info.get_fechaRevision()}")
                print(f"Mantenimiento: {implante_info.get_mantenimiento()}")
        
        dic_den = self.get_implantes()["ImplanteDental"]
        if not dic_dent:
            print("No hay información disponible para los implantes de rodilla.")
        else:
            print("\nImplantes de Dentales:")
            for implante_id, implante_info in dic_den.items():
                print(f"Implante ID: {implante_id}")
                print(f"Material: {implante_info.get_material()}")
                print(f"Forma: {implante_info.get_forma()}")
                print(f"Sistema de fijación: {implante_info.get_sistFijacion()}")
                print(f"Médico responsable: {implante_info.get_medResponsable()}")
                print(f"Estado: {implante_info.get_estado()}")
                print(f"Fecha revisión: {implante_info.get_fechaRevision()}")
                print(f"Mantenimiento: {implante_info.get_mantenimiento()}")
        
        dic_st = self.get_implantes()["StentCoronario"]
        if not dic_st:
            print("No hay información disponible para los implantes de rodilla.")
        else:
            print("\nStent Coronario:")
            for implante_id, implante_info in dic_st.items():
                print(f"Implante ID: {implante_id}")
                print(f"Material: {implante_info.get_material()}")
                print(f"Longitud: {implante_info.get_longitud()}")
                print(f"Diámetro: {implante_info.get_diametro()}")
                print(f"Médico responsable: {implante_info.get_medResponsable()}")
                print(f"Estado: {implante_info.get_estado()}")
                print(f"Fecha revisión: {implante_info.get_fechaRevision()}")
                print(f"Mantenimiento: {implante_info.get_mantenimiento()}")
 
        dic_marc = self.get_implantes()["Marcapasos"]
        if not dic_st:
            print("No hay información disponible para los implantes de rodilla.")
        else:
            print("\nMarcapasos:")
            for implante_id, implante_info in dic_marc.items():
                print(f"Implante ID: {implante_id}")
                print(f"Número de electrodos: {implante_info.get_nElectrodos()}")
                print(f"Forma de conexión: {implante_info.formConexion()}")
                print(f"Forma de estimulación: {implante_info.get_fEstimulacion()}")
                print(f"Médico responsable: {implante_info.get_medResponsable()}")
                print(f"Estado: {implante_info.get_estado()}")
                print(f"Fecha revisión: {implante_info.get_fechaRevision()}")
                print(f"Mantenimiento: {implante_info.get_mantenimiento()}") 

def main():
    servicio_implantes = Sistema()
    while True:
        while True:
            try:
                menu = int(input('''Bienvenido al sistema, ingrese una opción:
                         \n1-Agregar nuevo implante 
                         \n2-Eliminar implante
                         \n3-Crear paciente 
                         \n4-Asignar implante a paciente
                         \n5-Editar información de implante 
                         \n6-Visualizar inventario
                         \n7-Salir del sistema
                         >> '''))
                break
            except ValueError:
                print("Ingrese un valor del menú")
                continue
        if menu == 1: 
            while True:
                while True:
                    try:
                        tipo = int(input('''Ingrese el tipo de implante: 
                                \n1-Implante de rodilla
                                \n2-Implante de cadera
                                \n3-Implante dental
                                \n4-Stent Coronario
                                \n5-Marcapasos
                                \nOtro-Volver
                                >> '''))
                        break
                    except ValueError:
                        print("Ingrese un valor del menú")
                        continue
                while True:
                    try:
                        id_ = int(input("Ingrese la ID:"))
                        break
                    except ValueError:
                        print("Ingrese un dato numérico")
                        continue
                ver = servicio_implantes.verificarExisteImp(tipo, id_)
                if ver:
                    print(f"El implante de {tipo} con ID {id_} ya se encuentra en el sistema")
                    break
                else:
                    if tipo == 1:
                        ob = ImplanteRodilla()
                        mat = input("Ingrese el tipo de material: ")
                        tf = input("Ingrese el tipo de fijación: ")
                        while True:
                            try:
                                tam = float(input("Ingrese el tamaño: "))
                                break
                            except ValueError:
                                print("Ingrese un valor adecuado")
                                continue
                        med = input("Médico responsable: ")
                        frev = input("Fecha de revisión: ")
                        man = input("Mantenimiento: ")
                        est= input("Ingrese el estado del implante: ")
                        ob.set_material(mat)
                        ob.set_tipoFijacion(tf)
                        ob.set_tamaño(tam)
                        ob.set_medResponsable(med)
                        ob.set_fechaRevision(frev)
                        ob.set_mantenimiento(man)
                        ob.set_estado(est)
                        servicio_implantes.agregarImp(id_, tipo, ob)
                    elif tipo == 2:
                        ob = ImplanteCadera()
                        mat = input("Ingrese el tipo de material: ")
                        tf = input("Ingrese el tipo de fijación: ")
                        while True:
                            try:
                                tam = float(input("Ingrese el tamaño: "))
                                break
                            except ValueError:
                                print("Ingrese un valor adecuado")
                                continue
                        med = input("Médico responsable: ")
                        frev = input("Fecha de revisión: ")
                        man = input("Fecha de revisión: ")
                        est = input("Ingrese el estado del implante: ")
                        ob.set_material(mat)
                        ob.set_tipoFijacion(tf)
                        ob.set_tamaño(tam)
                        ob.set_medResponsable(med)
                        ob.set_fechaRevision(frev)
                        ob.set_mantenimiento(man)
                        ob.set_estado(est)
                        servicio_implantes.agregarImp(id_, tipo, ob)
                    elif tipo == 3:
                        ob = ImplanteDental()
                        mat = input("Ingrese el tipo de material: ")
                        f = input("Ingrese la forma del implante: ")
                        sf = input("Ingrese el sistema de fijación: ")
                        med = input("Médico responsable: ")
                        frev = input("Fecha de revisión: ")
                        man = input("Fecha de revisión: ")
                        est = input("Ingrese el estado del implante: ")
                        ob.set_material(mat)
                        ob.set_forma(f)
                        ob.set_sistFijacion(sf)
                        ob.set_medResponsable(med)
                        ob.set_fechaRevision(frev)
                        ob.set_mantenimiento(man)
                        ob.set_estado(est)
                        servicio_implantes.agregarImp(id_, tipo, ob)
                    elif tipo == 4:
                        ob = StentCoronario()
                        mat = input("Ingrese el tipo de material")
                        while True:
                            try:
                                l = float(input("Ingrese la longitud: "))
                                break
                            except ValueError:
                                print("Ingrese un valor adecuado")
                                continue
                        while True:
                            try:
                                d = float(input("Ingrese el diámetro: "))
                                break
                            except ValueError:
                                print("Ingrese un valor adecuado")
                                continue
                        med = input("Médico responsable: ")
                        frev = input("Fecha de revisión: ")
                        man = input("Fecha de revisión: ")
                        est = input("Ingrese el estado del implante: ")
                        ob.set_material(mat)
                        ob.set_longitud(l)
                        ob.set_diametro(d)
                        ob.set_medResponsable(med)
                        ob.set_fechaRevision(frev)
                        ob.set_mantenimiento(man)
                        servicio_implantes.agregarImp(id_, tipo, ob)
                    elif tipo == 5:
                        ob = Marcapasos()
                        while True:
                            try:
                                ne = int(input("Ingrese el número de electrodos: "))
                                break
                            except ValueError:
                                print("Ingrese un valor adecuado")
                                continue
                        
                        fc= input("Ingrese forma de conexión: ")
                        fe= input("Ingrese forma de estimulación: ")
                        med = input("Médico responsable: ")
                        frev = input("Fecha de revisión: ")
                        man = input("Fecha de revisión: ")
                        est = input("Ingrese el estado del implante: ")
                        ob.set_formConexion(fc)
                        ob.set_fEstimulacion(fe)
                        ob.set_nElectrodos(ne)
                        ob.set_medResponsable(med)
                        ob.set_fechaRevision(frev)
                        ob.set_mantenimiento(man)
                        ob.set_estado(est)
                        servicio_implantes.agregarImp(id_, tipo, ob)    
                    else:
                        break
        
        elif menu == 2:
            while True:
                try:
                    id_=int(input("Ingrese la ID del implante"))
                    break
                except ValueError:
                    print("Ingrese un valor adecuado")
                    continue
            while True:
                try:    
                    tipo=int(input('''Ingrese tipo de implante
                        \n1-Implante de rodilla 
                        \n2-Implante de cadera
                        \n3-Implante dental 
                        \n4-Stent coronario 
                        \n5-Marcapasos
                        \nOtro-Salir 
                        >> '''))
                    break
                except ValueError:
                    print("Ingrese un valor adecuado")
                    continue
            if tipo==1:
                tipo="ImplanteRodilla"
                servicio_implantes.eliminarImp(id_,tipo)
            elif tipo==2:
                tipo="ImplanteCadera"
                servicio_implantes.eliminarImp(id_,tipo)
            elif tipo==3:
                tipo="ImplanteDental"
                servicio_implantes.eliminarImp(id_,tipo)
            elif tipo==4:
                tipo="StentCoronario"
                servicio_implantes.eliminarImp(id_,tipo)
            elif tipo==5:
                tipo="Marcapasos"
                servicio_implantes.eliminarImp(id_,tipo)
            else:
                break
        
        elif menu==3:
            while True:
                pac=Paciente()
                while True:
                    try:    
                        id=int(input("Ingrese la cedula del paciente: "))
                        break
                    except ValueError:
                        print("Ingrese un valor adecuado")
                        continue
                if servicio_implantes.verificarExistePac(id):
                    print("El paciente ya se encuentra registrado")
                    break
                else:
                    pac.set_Nombre=input("Ingrese el nombre del paciente: ")
                    pac.set_Cedula=id
                    pac.set_Genero=input("Ingrese el genero del paciente: ")
                    servicio_implantes.agregarPac(id,pac)
                    servicio_implantes.agregarPac(id,pac)
                    break
        
        elif menu == 4:
            while True:
                try:
                    id_pac = int(input('Ingrese la ID del paciente: '))
                    break
                except ValueError:
                    print("Ingrese un valor numérico")
                    continue
            while True:
                try:
                    id_im = int(input('Ingrese la ID del implante disponible en el inventario: '))
                    break
                except ValueError:
                    print("Ingrese un valor numérico")
                    continue
            while True:
                try:
                    tipo = int(input('''Ingrese el tipo de implante: 
                            \n1-Implante de rodilla
                            \n2-Implante de cadera
                            \n3-Implante dental
                            \n4-Stent Coronario
                            \n5-Marcapasos
                            >> '''))
                    break
                except ValueError:
                    print("Ingrese un valor del menú")
                    continue
            if not servicio_implantes.verificarExistePac(id):
                print("El paciente no se encuentra registrado")
                break
            else:
                if tipo == 1:
                    pac = servicio_implantes.get_implantes()[id_pac]
                    ob = servicio_implantes.get_pacientes()[tipo][id_im]
                    pac.get_dicpacimplantes()[id_im] = ob
                    break
                elif tipo == 2:
                    pac = servicio_implantes.get_implantes()[id_pac]
                    ob = servicio_implantes.get_pacientes()[tipo][id_im]
                    pac.get_dicpacimplantes()[id_im] = ob
                    break
                elif tipo == 3:
                    pac = servicio_implantes.get_implantes()[id_pac]
                    ob = servicio_implantes.get_pacientes()[tipo][id_im]
                    pac.get_dicpacimplantes()[id_im] = ob
                    break
                elif tipo == 4:
                    pac = servicio_implantes.get_implantes()[id_pac]
                    ob = servicio_implantes.get_pacientes()[tipo][id_im]
                    pac.get_dicpacimplantes()[id_im] = ob
                    break
                elif tipo == 5:
                    pac = servicio_implantes.get_implantes()[id_pac]
                    ob = servicio_implantes.get_pacientes()[tipo][id_im]
                    pac.get_dicpacimplantes()[id_im] = ob
                    break

        elif menu==5:
            while True:
                try:
                    tipo = int(input('''Ingrese el tipo de implante: 
                                \n1-Implante de rodilla
                                \n2-Implante de cadera
                                \n3-Implante dental
                                \n4-Stent Coronario
                                \n5-Marcapasos
                                \nOtro-Volver
                                >> '''))
                    break
                except ValueError:
                    print("Ingrese un valor numérico")
                    continue
            while True:
                try:
                    id_Implante = int(input('Ingrese la ID del Implante que desea editar: '))
                    break
                except ValueError:
                    print("Ingrese un valor numérico")
                    continue
            if not servicio_implantes.verificarExisteImp(id_Implante):
                print("Este implante no se encuentra en el sistema")
            else:
                if tipo==1:
                    mat = input("Ingrese el tipo de material: ")
                    tf = input("Ingrese el tipo de fijación: ")
                    while True:
                        try:
                            tam = float(input("Ingrese el tamaño: "))
                            break
                        except ValueError:
                            print("Ingrese un valor adecuado")
                            continue
                    med = input("Médico responsable: ")
                    frev = input("Fecha de revisión: ")
                    man = input("Mantenimiento: ")
                    est = input("Ingrese el estado del implante: ")
                    servicio_implantes.editarInfoImplanRo(id_Implante,mat,tf,tam, med, est, frev, man, tipoimp=1)
                elif tipo==2:
                    mat = input("Ingrese el tipo de material: ")
                    tf = input("Ingrese el tipo de fijación: ")
                    while True:
                        try:
                            tam = float(input("Ingrese el tamaño: "))
                            break
                        except ValueError:
                            print("Ingrese un valor adecuado")
                            continue
                    med = input("Médico responsable: ")
                    frev = input("Fecha de revisión: ")
                    man = input("Mantenimiento: ")
                    est = input("Ingrese el estado del implante: ")
                    servicio_implantes.editarInfoImplanCa(id_Implante,mat,tf,tam, med, est, frev, man, tipoimp=2)
                elif tipo==3:
                    mat = input("Ingrese el tipo de material: ")
                    f = input("Ingrese la forma del implante: ")
                    sf = input("Ingrese el sistema de fijación: ")
                    med = input("Médico responsable: ")
                    frev = input("Fecha de revisión: ")
                    man = input("Fecha de revisión: ")
                    est = input("Ingrese el estado del implante: ")
                    servicio_implantes.editarInfoImplanDe(id_Implante, mat, f, sf, med, est, frev, man, tipoimp=3)
                elif tipo==4:
                    mat = input("Ingrese el tipo de material")
                    while True:
                        try:
                            l = float(input("Ingrese la longitud: "))
                            break
                        except ValueError:
                            print("Ingrese un valor adecuado")
                            continue
                    while True:
                        try:
                            d = float(input("Ingrese el diámetro: "))
                            break
                        except ValueError:
                            print("Ingrese un valor adecuado")
                            continue
                    med = input("Médico responsable: ")
                    frev = input("Fecha de revisión: ")
                    man = input("Fecha de revisión: ")
                    est = input("Ingrese el estado del implante: ")
                    servicio_implantes.editarInfoStent(id_Implante, mat, l, d, med, est, frev, man, tipoimp=4)
                elif tipo==5:
                    while True:
                        try:
                            ne = int(input("Ingrese el número de electrodos: "))
                            break
                        except ValueError:
                            print("Ingrese un valor adecuado")
                            continue
                    fc= input("Ingrese forma de conexión: ")
                    fe= input("Ingrese forma de estimulación: ")
                    med = input("Médico responsable: ")
                    frev = input("Fecha de revisión: ")
                    man = input("Fecha de revisión: ")
                    est = input("Ingrese el estado del implante: ")
                    servicio_implantes.editarInfoMarcapasos( id_Implante, ne, fc, fe, med, est, frev, man, tipoimp=5)
        elif menu == 6:
            print(servicio_implantes.verInventarioTotal())
        elif menu ==  7: 
            break
        else:
            continue                                    

main()