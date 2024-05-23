class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def Estudiar(self,horasdeestudio):
            print(f'el estudiante {self.nombre} esta estudiando por {horasdeestudio} horas')

        
nombre = input('por favor introdusca su nombre: ')
edad = input('ahora introdusca su edad : ')
grado = input('y por ultimo su grado : ')
            



Estudiante1 = Estudiante(nombre,edad,grado)

print(f"DATOS DEl ESRUDIANTE: \n Nombre : {Estudiante1.nombre} \n Edad : {Estudiante1.edad} \nGrado : {Estudiante1.grado} \n")



while True:
     
     estudiar = input()

     if estudiar.lower() == 'estudiar':
          Estudiante1.Estudiar(7)
      





        