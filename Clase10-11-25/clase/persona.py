import re

class Persona:
    def __init__(self,nombre,apellido,telefono,correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__correo = correo
        
    def getNombre(self):
        return f"{self.__nombre} {self.__apellido} "
    
    def getTelefono (self):
        return f"{self.__telefono}"
    
    def getCorreo (self):
        return self.__correo  
    
    def setCorreo (self,nuevo_correo):
        patron_correo = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        valido =re.match (patron_correo,nuevo_correo)
        if valido:
            self.__correo = nuevo_correo
       

        