class Persona:
    def __init__(self,nombre,apellido,telefono):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
    
    def getNombre(self):
        return f"{self.__nombre} {self.__apellido} "
    
    def getTelefono (self):
        return f"{self.__telefono}"
    
    
    

        