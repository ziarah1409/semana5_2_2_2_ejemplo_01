from sqlalchemy.orm import sessionmaker
# se importa la clase(s) del
# archivo crear_entidades
from crear_entidades import Ciudad
from crear_entidades import Estadio
# se importa el engine
from base_datos import engine

# Se crea una clase llamada Sessión,
# desde el generador de clases de SQLAlchemy
# sessionmaker.
Session = sessionmaker(bind=engine) # Se usa el engine
# Importante, se crea un objeto llamado session
# de tipo Session, que permite: permitir guardar, eliminar,
# actualizar y generar consultas a la base de datos.
session = Session()

# se crea un objetos de tipo Autor
Ciudad1= Ciudad(nombreCiudad="Piñas",pais="Ecuador",poblacion=9876345)
Ciudad2= Ciudad(nombreCiudad="España",pais="Europa",poblacion=3456789)
Ciudad3= Ciudad(nombreCiudad="Loja",pais="Ecuador",poblacion=9876523)
Estadio1= Estadio(nombreEstadio="Banco de Pichincha",direccionEstadio="Guayaquil",capacidad=80000)
Estadio2= Estadio(nombreEstadio="Olimpico Atahualpa",direccionEstadio="Quito",capacidad=90000)
Estadio3= Estadio(nombreEstadio="Olimpico Ibarra",direccionEstadio="Ecuador",capacidad=800000)

# se agrega los objetos de tipo Autor a la sesión
# a la espera de un commit
session.add(Ciudad1)
session.add(Ciudad2)
session.add(Ciudad3)
session.add(Estadio1)
session.add(Estadio2)
session.add(Estadio3)

# se necesita confirmar los cambios que existan en la sessió
# se usar commit
session.commit()
