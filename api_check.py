from dotenv import load_dotenv
import os

load_dotenv()
api_token = os.environ.get("api_read_key")

print(api_token)