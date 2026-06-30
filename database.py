from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
# import os

load_dotenv()
DATABASE_URL="postgresql://postgres:Thasmag97@localhost:5432/fastapi_todo"

# DATABASE_URL=os.getenv("DATABASE_URL")
# DATABASE_URL=os.getenv()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base()

#------------------------------------------------------------------------------

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from dotenv import load_dotenv
# import os

# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")

# if DATABASE_URL is None:
#     raise ValueError("DATABASE_URL is not found. Check your .env file.")

# engine = create_engine(DATABASE_URL)

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )

# Base = declarative_base()