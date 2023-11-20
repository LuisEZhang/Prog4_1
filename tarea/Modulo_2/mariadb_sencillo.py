from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "mysql+pymysql://adminsgc:C0c41n4@localhost/sgc"

engine = create_engine(DB_URL)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

Base.metadata.create_all(engine)

nuevo_usuario = User(name='Petra Petrov', age=30)
session.add(nuevo_usuario)
session.commit()

selected_users = session.query(User).filter_by(name='Petra Petrov').first()
print("Usuario seleccionado: " + selected_users.name + ", "+ str(selected_users.age))

nuevo_usuario.age = 31
session.commit()
print("Usuario actualizado: " + str(nuevo_usuario.age)) 

session.delete(selected_users)
session.commit()
print("Usuario eliminado")

session.close()

