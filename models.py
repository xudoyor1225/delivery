from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, ForeignKey, Float
from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    ism=Column(String(25),)
    familiya=Column(String(25),)
    username=Column(String(100), unique=True)
    password= Column(Text)
    tel = Column(String(25))
    address = Column(String(200))
    email=Column(String(128), unique=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    zakazlar=relationship("Zakaz", back_populates="user")

class Zakaz(Base):
    __tablename__ = 'zakaz'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='zakaz')
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship('Product', back_populates='zakaz')
    deliver_id = Column(Integer, ForeignKey('delivery.id'))
    delivery = relationship('Delivery', back_populates='zakaz')
    zakaz_vaqti=Column(DateTime)
    yetkazish_vaqti=Column(DateTime)
    holat = (
        ( " JARAYOND" , "jarayonda"),
        (" YOLDA", "yolda"),
        (" YETKAZILDI", "yetkazildi")
    )

    status=Column(ChoiceType(choices=holat) ,default="JARAYOND")
    manzil=Column(String(200))

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    narxi=Column(Float)
    paket=Column(String(50))
    manzil=Column(String(200))
    ogirligi=Column(String(100))
    saqlash_tartibi=Column(String(100))
    zakazlar=relationship("Zakaz", back_populates="product")


class Delivery(Base):
    __tablename__ = 'delivery'
    id = Column(Integer, primary_key=True)
    mashina_turi=Column(String(50))
    narxi=Column(Float)
    zakazlar=relationship("Zakaz", back_populates="delivery")



