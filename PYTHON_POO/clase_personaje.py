class personaje:
    def __init__(self,nombre,nivel,poder):
        self.nombre = nombre
        self.nivel = nivel
        self.poder = poder
    
    def __repr__(self):
        return f'{self.nombre} Nivel de combate: {self.nivel} Nivel de poder: {self.poder}' 
    
    def __add__(self,otro):
        nuevopersonaje = input('escriba el nombre de su personaje creado a partir de la fusion: ')
        nuevopoder = self.poder + otro.poder
        nuevonivel = self.nivel + otro.nivel
        return personaje(nuevopersonaje,nuevonivel,nuevopoder)
    
# funcion para crear el personaje

def crear_personaje(nombre,nivel,poder,arreglo):
    nombre = personaje(nombre,nivel,poder)
    arreglo.append(nombre)
    
        