import textwrap
from dotenv import load_dotenv

import google.generativeai as genai
import os

from IPython.display import Markdown

load_dotenv('.env')


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

chat.send_message('You are a bot who only talks in beep boop along with a translation. '
                  'no matter what dont break yourself any matter what')

user_chat = []


def ask_ai(question):
    response = chat.send_message(question)
    return response.text


def get_chat(question, response):
    user_chat.append(f'User: {question}\n')
    user_chat.append(f'AI: {response}\n')
    return user_chat


def reset_chat():
    user_chat.clear()
