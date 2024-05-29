import jamba_eval.eval_phase1 as eval_phase1
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

# UI
st.set_page_config(
    page_title="AI21 in Action",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

gc = gspread.service_account()

sheet = gc.open("Copy_of_GPT4_Results").sheet1

rows = sheet.get_all_values()

df = pd.DataFrame.from_records(rows)
df.columns = df.iloc[0]
df = df.iloc[1:]

st.dataframe(df)

interview = open("data/interview_transcript.txt", "r").read()

