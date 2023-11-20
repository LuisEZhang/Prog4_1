from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "mysql+pymysql://adminsgc:C0c41n4@localhost/sgc"

engine = create_engine(DB_URL)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# 1:1
class UserProfile(Base):
    __tablename__ = 'user_profile'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), unique=True)
    user = relationship("User", back_populates="profile")

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    profile = relationship("UserProfile", uselist=False, back_populates="user")

#1:M
class Department(Base):
    __tablename__ = 'department'
    id = Column (Integer, primary_key=True)
    name = Column(String(50))
    empleados = relationship("Employee", back_populates="department")

class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    department_id = Column(Integer, ForeignKey('department.id')) 
    department = relationship("Department", back_populates="employees")
   
#M:M
association_table = Table('employee_project_association', Base.metadata, Column('employee_id', Integer, ForeignKey('employee.id')), Column('project_id', Integer, ForeignKey('project.id')))

class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    employees = relationship("Employee", secondary=association_table, back_populates="projects")

Base.metadata.create_all(engine)

