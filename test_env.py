import os
from dotenv import load_dotenv
load_dotenv()

print(f"User: {os.getenv('user')}")
print(f"Pass: {os.getenv('password')}")