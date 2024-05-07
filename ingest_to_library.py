import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["AI21_API_KEY"]

url = "https://api.ai21.com/studio/v1/library/files"
headers = {"Authorization": f"Bearer {api_key}"}


# can only natively post one file at a time; can write custom function to do more programatically
files = {"file": open("data/Transcript_Mock_Interview.docx", "rb")}
# data = {
#     "path": "lib_data/interview_data",
# }

# path is a way to segment data in semantically logical ways - path not reflected in GUI
# labels also achieve this
# can act as guarding/narrowing down what is queried
    
requests.post(url=url, headers=headers, files=files)

# result: can POST multiple files to the library, but only 1 at a time! 

# QUESTIONS:
# Are the documents transformed (index calculation, embedding of text) at all when they're opened or used in the request? making REST call via Python SDK

# when POST request: it indexes docs, chunking, embedding + loading to vector DB in one call
# text embedding model: created by AI21 based on a HF text embedding model -- finding out which (E5? with tweaking by AI21 - retraining/finetuning - may not have access to details on training sets etc.)

# when answering, different endpoint -- that URL will do retrieval from vector DB + LLM generates answer

# for other data types, may need custom build but asking product

# can call the embedding model directly - SDK/request API