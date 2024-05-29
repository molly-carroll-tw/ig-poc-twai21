import os
from ai21 import AI21Client
from ai21.models.chat import ChatMessage
from dotenv import load_dotenv
import gspread
import pandas as pd

client = AI21Client(
    api_key=os.environ["AI21_API_KEY"],
)

gc = gspread.service_account()

sheet = gc.open("Copy_of_GPT4_Results").sheet1

rows = sheet.get_all_values()

df = pd.DataFrame.from_records(rows)
df.columns = df.iloc[0]
df = df.iloc[1:]

# phase 1: 

def phase_one():
    pass

if __name__ == '__main__':
    phase_one()