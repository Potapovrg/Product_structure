from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    
    children = relationship("ProductStructure", back_populates="parent")

class Component(Base):
    __tablename__ = 'components'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Float)
    unit_of_measure = Column(String)

class ProductStructure(Base):
    __tablename__ = 'product_structure'

    id = Column(Integer, primary_key=True)
    parent_product_id = Column(Integer, ForeignKey('products.id'))
    child_id = Column(Integer)
    child_type = Column(String)
    quantity = Column(Float)

    parent = relationship("Product", back_populates="children")