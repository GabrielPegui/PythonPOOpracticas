class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def info(self):
        print(f'El nombre de esta persona es: {self.nombre} y tiene una edad de: {self.edad}')


class Estudiante(Persona):
    def __init__(self, nombre, edad,grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def Grado(self):
        print(f'el grado de este estudiante es {self.grado}')



Javier = Estudiante('Javier Jimenez','17 años','6to de Secundaria')

Javier.info()
Javier.Grado()


          

