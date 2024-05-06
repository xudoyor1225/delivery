from database import Base, engine
from models import User, Product ,Delivery ,Zakaz

Base.metadata.create_all(engine)