from documento import Documento

class Comrpobante (Documento):
    def __init__(self,id,fecha,monto):
        super().__init__(id,fecha)
        self.__monto = monto
    @property
    def monto(self):
        return self.__monto
    
    @monto.setter
    def monto(self,monto):
        if monto <0:
            raise Exception ("El monto ingresado no concuerda, este debe ser mayor a '0' ")
        self.__monto
        