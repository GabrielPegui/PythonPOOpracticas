from abc import ABC, abstractclassmethod


class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f'Soy {self.nombre} del sexo {self.sexo} y tengo la edad de {self.edad}')



class basketbolista(Persona):
    def __init__(self,nombre,edad,sexo,actividad,estado):
        super().__init__(nombre,edad,sexo,actividad)
        self.estado = estado

    def hacer_actividad(self):
        print(f'mi actividad es la de jugar {self.actividad} y ahora mismo estoy {self.estado}')


class Artista(Persona):
    def __init__(self,nombre,edad,sexo,actividad,estado):
        super().__init__(nombre,edad,sexo,actividad)
        self.estado = estado

    def hacer_actividad(self):
        print(f'mi actividad es la de  {self.actividad} y ahora mismo estoy {self.estado}')


Jesus = basketbolista('Jesus Encarnacion Sanchez','25 años','Masculino','Baloncesto','encestando')
CLariza = Artista('Clariza Mendez Polaca','22 años','Femenino','Cantar','Cantando')

Jesus.presentarse()
Jesus.hacer_actividad()
CLariza.presentarse()
CLariza.hacer_actividad()




        