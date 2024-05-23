class Animal:
    def comer(self):
        print('Estoy Comiendo')

class Mamifero(Animal):
    def Amamantar(self):
        print('Estoy Amamantando')
    def comer(self):
        print('Estoy Comiendo 2')


class Ave(Animal):
    def Volar(self):
        print('Estoy Volando')

class Murcielago(Ave,Mamifero):
    pass


jorfi = Murcielago()

jorfi.comer()
jorfi.Amamantar()
jorfi.Volar()

Animal.comer(jorfi)