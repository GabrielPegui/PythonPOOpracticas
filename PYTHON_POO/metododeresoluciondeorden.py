class A:
    def hablar(self):
        print('hola desde A')

class B:
    def hablar(self):
        print('hola desde B')

class C(A):
     def hablar(self):
        print('hola desde C')

class D(B):
    def hablar(self):
        print('hola desde D')

class E(D):
    def hablar(self):
        print('hola desde E')

llamadadeletras = E()


A.hablar(llamadadeletras)