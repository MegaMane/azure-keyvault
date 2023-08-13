import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("test_key")

print(os.environ["test_key"])

print(key)