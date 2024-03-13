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
        self.set_medResponsable(medResponsable)
        self.set_estado(estado)
        self.set_fechaRevision(fechaRevision)
        self.set_mantenimiento(mantenimiento)
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
        self.set_medResponsable(medResponsable)
        self.set_estado(estado)
        self.set_fechaRevision(fechaRevision)
        self.set_mantenimiento(mantenimiento)
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
        self.set_medResponsable(medResponsable)
        self.set_estado(estado)
        self.set_fechaRevision(fechaRevision)
        self.set_mantenimiento(mantenimiento)
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
        self.__forma = fs
    def set_sistFijacion(self, sf):
        self.__sistFijacion = sf

class StentCoronario:
    def __init__(self, medResponsable, estado, fechaRevision, mantenimiento):
        super().__init__(medResponsable, estado, fechaRevision, mantenimiento)
        self.set_medResponsable(medResponsable)
        self.set_estado(estado)
        self.set_fechaRevision(fechaRevision)
        self.set_mantenimiento(mantenimiento)
        self.__material = ""
        self.longitud = float
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

        