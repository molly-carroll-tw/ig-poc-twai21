import os
from ai21 import AI21Client
from ai21.models.chat import ChatMessage
from dotenv import load_dotenv
import gspread
import pandas as pd
import streamlit as st

load_dotenv()

client = AI21Client(
    api_key=os.environ["AI21_API_KEY"],
)

gc = gspread.service_account()

sheet = gc.open("Copy of GPT4_Results").sheet1

rows = sheet.get_all_values()

imported_df = pd.DataFrame.from_records(rows)

# UI
st.set_page_config(
    page_title="AI21 in Action",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

interview = open("data/interview_transcript.txt", "r").read() 
# local RAG data corpus

#creating columns name
imported_df.columns = imported_df.iloc[0]
imported_df = imported_df.iloc[1:]

messages = [
  ChatMessage(
    role="user",
    content=f"""You are an interviewer evaluating Praveen for a software engineering job.
    Please comprehend the interview transcript in the context of computer science and software engineering.
    Use the interview transcript to answer if Praveen meets the criteria.

    <interview transcript>

    """ + interview + f"""

    </interview transcript>
    """
  )
]