import json
from tkinter import messagebox
import logging
import os

def save_session_data(session_data, filename='session.json'):
    try:
        with open(filename, 'w') as session_file:
            json.dump(session_data, session_file)
        logging.info("Session data saved successfully.")
    except Exception as e:
        logging.error(f"Failed to save session data with error: {str(e)}")
        messagebox.showerror("Error", f"Could not save session data: {str(e)}")


def load_session_data(filename='session.json'):
    try:
        with open(filename, 'r') as session_file:
            session_data = json.load(session_file)
        logging.info("Session data loaded successfully.")
        return session_data
    except FileNotFoundError:
        logging.info("No previous session data found.")
        return None
    except Exception as e:
        logging.error(f"Failed to load session data with error: {str(e)}")
        messagebox.showerror("Error", f"Could not load session data: {str(e)}")
        return None