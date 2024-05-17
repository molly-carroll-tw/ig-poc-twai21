import csv
import os
from dotenv import load_dotenv
from ai21 import AI21Client
from transformers import AutoModelForCausalLM, AutoTokenizer

load_dotenv()

txt_file = open("data/txt_ldc.txt", "r")

def split_file(txt_file):
    for something in txt_file:
        part = something.strip("}")
    return part

criteria_content_list = split_file(txt_file)

full_dict_prep = str(criteria_content_list).split("}{")
query_construction = full_dict_prep[2].partition("'Definition': ")[-1]

client = AI21Client(
    api_key=os.environ["AI21_API_KEY"],
)

results_csv = open('results.csv', 'a')

# TODO: adjust CSV delimiter for output file visibility
def run_evaluation(upload):
    for l in range(0, len(upload)-1):
        extracted_query = upload[l].partition("'Definition': ")[-1]
        category_prefix = upload[l].partition(", 'Definition'")[:1]

        # Use interview transcript file ID vs. label
        response = client.library.search.create(query=extracted_query, labels=["demo1"])
        if (len(response.results) > 0):
            results_csv.write(f"Evaluation: YES | Criteria: {category_prefix} {extracted_query} Source sample: {response.results[0]}")
        else:
            results_csv.write(f"Evaluation: No/Not Found | Criteria: {category_prefix} {extracted_query}")
    results_csv.close()
    

def print_eval(upload):
    for l in range(0, len(upload)-1):
        extracted_query = upload[l].partition("'Definition': ")[-1]
        category_prefix = upload[l].partition(", 'Definition'")[:1]

        # QUESTION: despite the label indication the query still searches all docs in RAG engine - help?
        response = client.library.search.create(query=extracted_query, labels=["demo1"])
        if (len(response.results) > 0):
             print(f"Evaluation: YES | Criteria: {category_prefix} {extracted_query} Source sample: {response.results[0]}")
        else:
             print(f"Evaluation: No/Not Found | Criteria: {category_prefix} {extracted_query}")

# print_eval(full_dict_prep)
run_evaluation(full_dict_prep)