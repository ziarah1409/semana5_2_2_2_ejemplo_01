from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
# se importa el engine
from base_datos import engine

# se crea la clase llamada Base que permite definir las clases bajo las
# características de SQLAlchemy
Base = declarative_base()

# Se crea la una entidad llamada Autor, que hereda
# de Base
class Ciudad (Base):
    __tablename__ = 'Ciudad' # El nombre de la entidad en sqlite
    # Se definen los atributos
    id = Column(Integer, primary_key=True) # este atributo es entero y
                                        # se lo considera como llave
                                        # primaria
    nombreCiudad = Column(String) # atributo de tipo String
    poblacion = Column(Integer)
    pais = Column(String)
    def __str__(self):
        return "%s %s %s " % (self.nombreCiudad, self.poblacion, self.pais)
    

class Estadio (Base):
    __tablename__ = 'Estadio' # El nombre de la entidad en sqlite
    # Se definen los atributos
    id = Column(Integer, primary_key=True) # este atributo es entero y
                                        # se lo considera como llave
                                        # primaria
    nombreEstadio = Column(String) # atributo de tipo String
    direccionEstadio = Column(String)
    capacidad = Column(Integer)
    def __str__(self):
        return "%s %s %s" % (self.nombreEstadio, self.direccionEstadio, self.capacidad)
  

# Sentencia que permite crear o migrar las clases en Python al
# gestor de base de datos, expresado en el engine.
Base.metadata.create_all(engine)
