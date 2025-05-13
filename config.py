from dotenv import load_dotenv
import os

load_dotenv()
db_username = os.getenv("DB_USERNAME")
password = os.getenv("PASSWORD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_port = os.getenv("DB_PORT")
DATABASE_URL = f"postgresql://{db_username}:{password}@{db_host}:{db_port}/{db_name}"
