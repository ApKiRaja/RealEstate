import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env file

TOKEN = os.getenv("TELEGRAM_TOKEN")
RAZORPAY_KEY = os.getenv("RAZORPAY_KEY")
RAZORPAY_SECRET = os.getenv("RAZORPAY_SECRET")
DATABASE_URL = os.getenv("DATABASE_URL")  # Auto-provided by Railway
