import openai
from tkinter import messagebox
import logging
import os


openai.api_key = os.getenv('OPENAI_API_KEY')

def ask_gpt(question, context, model="gpt-4-1106-preview"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": context},
                {"role": "user", "content": question}
            ]
        )
        logging.info(f'Requested ChatCompletion for question: {question}')
        return response.choices[0].message['content']
    except openai.error.OpenAIError as e:
        messagebox.showerror("OpenAI Error", str(e))
        logging.error(f'OpenAI Error: {str(e)}')
        return None

def batch_process_questions(questions, excel_context):
    responses = []
    for question in questions:
        response = ask_gpt(question, excel_context)
        responses.append(response if response is not None else "Error occurred during question processing.")
    return responses
