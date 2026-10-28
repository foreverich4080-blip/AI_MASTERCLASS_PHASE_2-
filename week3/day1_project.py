import os
import time


from dotenv import load_dotenv
from google.genai import types

from WEEK1.day2pp import api_key

load_dotenv()
from google import genai
from google.genai import errors

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("no api_key found, kindly check your .env file and make sure the key is working and updated")
else:
    print("api_key found ")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

question = input("ask the SACCO assistant😊:") # hardcoded question and for a system the questions should be automatic not hardcoded

system_instruction = """You are a helpful and very strict Matatu SACCO assistant.

SACCO information:
1. member balance : KSH 12,500.
2. next meeting : saturday at 10:00 AM.
3. membership fee: KSH 1,000.

answer members question clearly,concisely and best way.
strictly only use the information provided above.
do not invent SACCO information.
if the requested information is not available, say that you don't have the information as per now.
"""


for attempt in range (5):
    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=question,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction
            )

        )
        print()
        print("="*50)
        print()
        print("SACCO ASSISTANT:")
        print("="*50)
        print(response.text)
        print(response.usage_metadata)
        break


    except errors.ServerError as e:
        print(f"Gemini server error.ATTEMPT{e}\n {attempt+1}/3")
        if attempt < 4:
           time.sleep(5)
        else:
            print("gemini is currently unavailable: Kindly try again later")
    except Exception as e:
        print(f"Unexpected error{e}")







