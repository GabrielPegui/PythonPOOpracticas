class personaje:
    def __init__(self,nombre,poder,habilidad):
        self.nombre = nombre
        self.poder = poder
        self.habilidad = habilidad

    def __repr__(self):
        return f'Este personaje es: {self.nombre}, su poder es de: {self.poder} y su habilidad es de: {self.habilidad}'
    def __add__(self,otro_personaje):
        nuevo_nombre = input('introdusca el nombre del nuevo personaje a crear:')
        nuevo_poder = round(((self.poder + otro_personaje.poder)/2)**2)
        nuevo_habilidad = round(((self.habilidad + otro_personaje.habilidad)/2)**2)
        return personaje(nuevo_nombre,nuevo_poder,nuevo_habilidad)
    
Goku = personaje('Goku',1000,1500)
Vegeta = personaje('Vegeta',950,1400)


print(Goku)
print(Vegeta)
respuesta = input(f'Desea crear un personaje mas fuerte combinando a {Goku.nombre} y a {Vegeta.nombre} ?')
if respuesta.lower() == 'si':
    nuevopersonaje = Goku + Vegeta
    print(nuevopersonaje) 
else:
    print(f'los personajes actuales son: {Goku} y {Vegeta}')
