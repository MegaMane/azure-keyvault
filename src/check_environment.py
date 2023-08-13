import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("api_key")

print(key)