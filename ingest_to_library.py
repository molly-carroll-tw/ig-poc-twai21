import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["AI21_API_KEY"]

url = "https://api.ai21.com/studio/v1/library/files"
headers = {"Authorization": f"Bearer {api_key}"}

files = {"file": open("data/Transcript_Mock_Interview.docx", "rb")}
# data = {
#     "path": "lib_data/interview_data",
# }
    
requests.post(url=url, headers=headers, files=files)

# result: can POST multiple files to the library, but only 1 at a time! (unless I did open() syntax wrong)

# QUESTIONS:
# Are the documents transformed (index calculation, embedding of text) at all when they're opened or used in the request? making REST call via Python SDK
# If so, what happens to them and what model(s) if any are used? Text embedding?