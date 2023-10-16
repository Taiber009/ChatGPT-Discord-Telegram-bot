import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")


def chatgpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[ {"role": "user","content":prompt}])
        # print(response)
        return str(response['choices'][0]['message']['content'])
    except Exception as e:
        return str(e)
