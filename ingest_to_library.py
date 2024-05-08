import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["AI21_API_KEY"]

url = "https://api.ai21.com/studio/v1/library/files"
headers = {"Authorization": f"Bearer {api_key}"}

files = {"file": open("data/Transcript_Mock_Interview.docx", "rb")}
    
requests.post(url=url, headers=headers, files=files)

