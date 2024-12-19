from sqlalchemy import Column, String, Float, Integer, ForeignKey, Date, Table, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Business(Base):
    __tablename__ = 'businesses'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(String, nullable=False)
    location = Column(String)
    created_at = Column(Date, server_default='now()')

class Dish(Base):
    __tablename__ = 'dishes'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    business_id = Column(UUID(as_uuid=True), ForeignKey('businesses.id', ondelete='CASCADE'))
    name = Column(String, nullable=False)
    price_usd = Column(Float, nullable=False)
    description = Column(String)
    created_at = Column(Date, server_default='now()')

class Sale(Base):
    __tablename__ = 'sales'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    dish_id = Column(UUID(as_uuid=True), ForeignKey('dishes.id', ondelete='CASCADE'))
    sale_date = Column(Date, nullable=False)
    sale_hour = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    total_sales_usd = Column(Float, nullable=False)
