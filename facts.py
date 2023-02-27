from random import randrange
from datetime import date
import os, base64
import json


from __init__ import app, db
from sqlalchemy.exc import IntegrityError




class Facts(db.Model):
   __tablename__ = 'facts'  # table industry is plural, class industry is singular


   # Define the User schema with "vars" from object
   id = db.Column(db.Integer, primary_key=True)
   stock = db.Column(db.String(255), unique=True, nullable=False)
   _industry = db.Column(db.String(255), unique=False, nullable=False)
  
   # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)
   # constructor of a User object, initializes the instance variables within object (self)
   def __init__(self, stock, industry):


       self._industry = industry   # variables with self prefix become part of the object,
       self.stock = stock


   @property
   def industry(self):
       return self._industry
  
   # a setter function, allows industry to be updated after initial object creation
   @industry.setter
   def industry(self, industry):
       self._industry = industry


  


   @property
   def stock(self):
       return self.stock
  
   # a setter function, allows industry to be updated after initial object creation
   @stock.setter
   def stock(self, stock):
       self.stock = stock


   def __str__(self):
       return json.dumps(self.read())


   def create(self):
       try:
           # creates a person object from User(db.Model) class, passes initializers
           db.session.add(self)  # add prepares to persist person object to Users table
           db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
           return self
       except IntegrityError:
           db.session.remove()
           return None


   # CRUD read converts self to dictionary
   # returns dictionary
   def read(self):
       return {
           "id": self.id,
           "industry": self.industry,
           "stock": self.stock,
          
       }


   # CRUD update: updates user industry, knew, phone
   # returns self
   def update(self, industry="", stock=""):
       """only updates values with length"""
       if len(industry) > 0:
           self.industry = industry
       if len(stock) > 0:
           self.stock = stock
       db.session.commit()
       return self


   # CRUD delete: remove self
   # None
   def delete(self):
       db.session.delete(self)
       db.session.commit()
       return None
"""CRUD DONE"""


def initFacts():


   """Builds sample user/note(s) data"""
   with app.app_context():
       """Create database and tables"""
       db.create_all()
       """Tester data for table"""
       u1 = Facts( industry='Creates your technology products, especially your cell phones', stock='Apple', )
       u2 = Facts( industry='Creates computers, laptop software, and other products', stock='Microsoft', )
       u3 = Facts( industry='Creates electric stock', stock='Tesla', )
       u4 = Facts( industry='Creates American stock', stock='Ford', )
       u5 = Facts( industry='Creates movies', stock='Disney', )


       facts = [u1, u2, u3, u4, u5]


       """Builds sample user/note(s) data"""
       for fact in facts:
           try:
               '''add a few 1 to 4 notes per user'''
               fact.create()
           except IntegrityError:
               '''fails with bad or duplicate data'''
               db.session.remove()
               print(f"Records exist, duplicate email, or error:")



