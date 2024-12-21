from faker import Faker
from sqlalchemy.orm import Session
from app.db import Base, engine, SessionLocal
from app.models import Business, Dish, Sale
import random
from datetime import datetime, timedelta

# creating faker
fake = Faker()

# creating bd
Base.metadata.create_all(bind=engine)

def clear_database(db: Session):
    # clear db before
    db.query(Sale).delete()
    db.query(Dish).delete()
    db.query(Business).delete()
    db.commit()


def seed_businesses(db: Session, count: int = 5):
    # create fake businesses
    businesses = []
    for _ in range(count):
        business = Business(
            name=fake.company(),
            location=fake.address(),
            created_at=fake.date_this_decade()
        )
        db.add(business)
        businesses.append(business)
    db.commit()
    return businesses


def seed_dishes(db: Session, businesses, count_per_business: int = 10):
    # creating dishes for each buinesses
    dishes = []
    dish_names = [
        "Pasta", "Pizza", "Burger", "Sushi", "Salad",
        "Tacos", "Steak", "Soup", "Sandwich", "Fries"
    ]
    for business in businesses:
        for _ in range(count_per_business):
            dish = Dish(
                business_id=business.id,
                name=random.choice(dish_names),
                price_usd=round(random.uniform(5.0, 50.0), 2),
                description=fake.sentence(nb_words=10),
                created_at=fake.date_this_decade()
            )
            db.add(dish)
            dishes.append(dish)
    db.commit()
    return dishes


def seed_sales(db: Session, dishes, count_per_dish: int = 20):
    # creating fake sales
    sales = []
    for dish in dishes:
        for _ in range(count_per_dish):
            sale_date = fake.date_between(start_date="-1y", end_date="today")
            sale_hour = random.randint(0, 23)
            quantity = random.randint(1, 10)
            total_sales_usd = quantity * dish.price_usd
            sale = Sale(
                dish_id=dish.id,
                sale_date=sale_date,
                sale_hour=sale_hour,
                quantity=quantity,
                total_sales_usd=round(total_sales_usd, 2)
            )
            db.add(sale)
            sales.append(sale)
    db.commit()
    return sales


def run_seeding():
    # filling db
    db = SessionLocal()
    try:
        print("Clearing database...")
        clear_database(db)

        print("Seeding businesses...")
        businesses = seed_businesses(db, count=5)

        print("Seeding dishes...")
        dishes = seed_dishes(db, businesses, count_per_business=10)

        print("Seeding sales...")
        seed_sales(db, dishes, count_per_dish=20)

        print("Database seeding completed!")
    finally:
        db.close()


if __name__ == "__main__":
    run_seeding()
