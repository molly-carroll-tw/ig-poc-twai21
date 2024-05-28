import os
from ai21 import AI21Client
from ai21.models.chat import ChatMessage
from dotenv import load_dotenv
import gspread
import pandas as pd

load_dotenv()

client = AI21Client(
    api_key=os.environ["AI21_API_KEY"],
)

gc = gspread.service_account()

sheet = gc.open("Copy of GPT4_Results").sheet1

rows = sheet.get_all_values()

df = pd.DataFrame.from_records(rows)

df.columns = df.iloc[0]
df = df.iloc[1:]

interview = open("data/interview_transcript.txt", "r").read()

df['jamba_eval'] = 'NA'
df['jamba_citation'] = 'NA'

criteria = []
message = []

for i in range(len(df)):
  criteria_i = df['Definition'][i+1] + '. Attribute: ' + df['Attribute'][i+1] + '. Category: ' + df['Category'][i+1]


  criteria.append(
      criteria_i
      )

  message.append(f"""Classify the evaluation results for each criteria based on the following interview transcript into 'Yes' or 'No'.
      If there is not enough information in the interview transcript to provide the evaluation results for a criteria, provide output as 'NA'.

      <output>
      Yes
      No
      NA
      </output>

      <interview transcript>

      """ + interview + f"""

      </interview transcript>

      <criteria>

      """ + criteria_i + f"""

      </criteria>

      Now classify the evaluation results for the critera based on the interview transcript.
      The output should be binary, without any other preamble text.
      """
      )

  messages = [
      ChatMessage(content=message[i], role="user"),
  ]

  response = client.chat.completions.create(
      messages=messages,
      model="jamba-instruct",
      temperature=0
  )

  # print(i)
  # print(response.choices[0].message.content)
  # df['jamba_eval'][i] = response.choices[0].message.content

criteria = []
message = []

for i in range(len(df)):
  criteria_i = df['Definition'][i+1] + '. Attribute: ' + df['Attribute'][i+1] + '. Category: ' + df['Category'][i+1]


  criteria.append(
      criteria_i
      )

  message.append(f"""Provide original quote from the interview transcript that is relevant to the evaluate Praveen against each criteria.
      If there is not enough information in the interview transcript to provide the evaluation results for a criteria, provide output as 'NA'.

      <interview transcript>

      """ + interview + f"""

      </interview transcript>

      <criteria>

      """ + criteria_i + f"""

      </criteria>

      Now respond with relevant quote from the interview transcript for the criteria.
      """
      )

  messages = [
      ChatMessage(content=message[i], role="user"),
  ]

  response = client.chat.completions.create(
      messages=messages,
      model="jamba-instruct",
      temperature=0
  )

#   print(i)
#   print(response.choices[0].message.content)
#   df['jamba_citation'][i] = response.choices[0].message.content



        messages_1 = ChatMessage(content=prompt_1_list[i], role="user")

        response_1 = client.chat.completions.create(
            messages=messages_1,
            model="jamba-instruct",
            temperature=0
        )

        answer = response_1.choices[0].message.content
        df['jamba_eval'] = answer

        return df