import os
from ai21 import AI21Client
from ai21.models.chat import ChatMessage
from dotenv import load_dotenv
import gspread
import pandas as pd
import streamlit as st
from io import StringIO

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

def chat_call(iteration):
    message = ChatMessage(content=iteration, role="user")

    response = client.chat.completions.create(
        messages=message,
        model="jamba-instruct",
        temperature=0
    )

    answer = response.choices[0].message.content

    return answer

def eval_loop(datfr):
    for i in range(len(datfr)):
        i = i+1

        conglomeration = f"""You are an highly trained technical interviewer evaluating Praveen for a software engineering job.
      Do your best to comprehend the interview transcript in the context of computer science and software engineering.
      You should the interview transcript to answer if Praveen meets the criteria.

      <interview transcript>

      """ + interview + f"""

      </interview transcript>

      <criteria>

      """ + datfr['Definition'][i] + f"""

      </criteria>

      Now you generate evaluation results for Praveen based on the evaluation critera with information provided in the interview transcript.
      You shoud not use information what is not included in the interview transcripts.
      Your output should be 'Yes' or 'No', without any other preamble text.
      """
    
    answer = chat_call(conglomeration)

    if answer.lower() == 'yes':
        print('yaayy')
    

# GPT4 simulated evaluation
st.header("gpt4 simulated evaluation")
st.data_editor(imported_df)