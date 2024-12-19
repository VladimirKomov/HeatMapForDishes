import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Loading environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    print("DATABASE_URL is not set.")
else:
    try:
        engine = create_engine(DATABASE_URL)

        # checked connection
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Connection successful:", result.scalar())
    except Exception as e:
        print("Connection failed:", e)
