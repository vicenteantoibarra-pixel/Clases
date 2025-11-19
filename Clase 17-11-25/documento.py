
class Documento:
    def __init__(self, fecha, id):
        self.__id = id
        self.__fecha = fecha

    @property
    def id (self):
        return self.__id
    
    @id.setter
    def id (self, id):
        if id  <0:
            raise Exception ("El ID debe ser mayor a '0' ")
        self.__id = id 
        
    @property
    def fecha (self):
        return self.__fecha
    
    @fecha.setter
    def fecha (self, fecha):
        if fecha  <0:
            raise Exception ("La Fecha debe ser mayor a '0' ")
        self.__fecha = fecha 
    

    
    