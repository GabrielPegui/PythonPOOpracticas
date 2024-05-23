class Persona:
    def __init__(self,nombre,apellido):
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,newnombre):
        self._nombre = newnombre
        
    @nombre.deleter
    def nombre(self):
        del self._nombre
    


Persona1 = Persona('Gabriel','Peguero')


print(Persona1.nombre)


Persona1.nombre = 'Felipe'

print(Persona1.nombre) 

""" del Persona1.nombre
 """

Persona1.nombre = 'elrembo'
print(Persona1.nombre)





