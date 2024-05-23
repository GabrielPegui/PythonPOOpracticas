# juego de creacion de personajes y funsion.
from clase_personaje import personaje,crear_personaje

#arreglo donde se almacenaran los personajes
personajes = []

while True:
    #muestra de las opciones para el usuario
    print('Bienvenido a su juego de Personajes')
    #muestra de las opciones
    print('1.Crear Personaje')
    print('2.Funsionar Personajes')
    print('3.mostrar personajes')
    print('4.salir')

    #selecionar uan opcion
    Seleccion = int(input('escriba el numero de la opcion que le interesa: '))
    while Seleccion <= 0 or Seleccion >= 5:
        print('debe elegir una opcion valida para este juego, es decir un numero entre 1 y 4 que son las opciones validas')
        Seleccion = int(input('escriba el numero de la opcion que le interesa'))

    #segun la opcion seleccionada que haremos

    if Seleccion == 1:
        print("Bien a continuacion creara sus personaje poniendole un nombre, un nivel y un poder que desee. suerte !!")
        nombre = input('nombre del personaje a crear: ')
        nivel = int(input('nivel del personaje a crear: '))
        poder = int(input('poder del personaje a crear: '))
        crear_personaje(nombre,nivel,poder,personajes)
        print('Personaje creado exitosamente!!!')
        

    #tener pendiente en la opcion 2 guardar ese personaje fusioando en el arreglo 

    elif Seleccion == 2:
        print('A continuación fusionarás personajes. Ten en cuenta que los personajes a fusionar deben existir. En caso de que no existan, debes crearlos.')

        personaje1_nombre = input('Nombre del personaje 1 a fusionar: ')
        personaje2_nombre = input('Nombre del personaje 2 a fusionar: ')

        # Verificar si ambos personajes existen en la lista
        if personaje1_nombre in [p.nombre for p in personajes] and personaje2_nombre in [p.nombre for p in personajes]:
            # Encuentra los objetos de personaje correspondientes a los nombres
            personaje1_obj = next(p for p in personajes if p.nombre == personaje1_nombre)
            personaje2_obj = next(p for p in personajes if p.nombre == personaje2_nombre)

            # Fusionar personajes
            nuevo_personaje = personaje1_obj + personaje2_obj
            # Agregar el nuevo personaje fusionado a la lista de personajes
            crear_personaje(nuevo_personaje.nombre, nuevo_personaje.nivel, nuevo_personaje.poder, personajes)
            print('Personajes fusionados exitosamente!')
        else:
            print('Al menos uno de los personajes no se encuentra en la lista de personajes.')


        

    elif Seleccion == 3:
        print('A continuacion le mostraremos sus personajes disponibles')
        print('personajes: ')
        if not personajes:
            respuesta = input('aun no tiene personajes! quiere crear uno?')
            if respuesta.lower() == 'si':
                    nombre = input('nombre del personaje a crear: ')
                    nivel = int(input('nivel del personaje a crear: '))
                    poder = int(input('poder del personaje a crear: '))
                    crear_personaje(nombre,nivel,poder,personajes)
                    print('personaje creado, a continuacion su lista')
                    for personaje in personajes:
                     print(personaje)
            else:
                print('bueno no ah querido crear un personaje no teniendo ninguno , se acabo el juego !')
                break

        else:
            for personaje in personajes:
                print(personaje)
            
        



    else:
        print('ah salido del juego de personajes y fuciones , Hasta luego')
        break
    





