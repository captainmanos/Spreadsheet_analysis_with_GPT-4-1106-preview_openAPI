from tkinter import Tk, filedialog, simpledialog, messagebox
from excel_utils import read_excel_files
from session_manager import load_session_data, save_session_data
from gpt_interaction import ask_gpt, batch_process_questions
import logging


def main():
    # Create a root window and hide it for file dialog usage
    root = Tk()
    root.withdraw()

    # Load previous session data if available
    session_data = load_session_data()
    file_paths = session_data.get('file_paths', []) if session_data else []

    # Enable batch file import with error handling
    new_file_paths = filedialog.askopenfilenames(title="Select Excel files",
                                                 filetypes=[("Excel files", "*.xlsx *.xls")])

    if not new_file_paths:
        messagebox.showinfo("Notice", "No Excel files were selected. Continuing with already loaded files.")
        logging.info('No new Excel files were selected, using previously loaded files.')
    else:
        file_paths.extend(new_file_paths)

    if not file_paths:
        messagebox.showinfo("Operation Cancelled", "No Excel files have been loaded.")
        logging.info('Operation cancelled by the user. No Excel files loaded.')
        root.destroy()
        return

    excel_context = read_excel_files(file_paths)
    if excel_context is None:
        messagebox.showwarning("Warning", "No data was read from Excel files, or an error occurred while processing.")
        root.destroy()
        return

    questions = session_data['questions'] if session_data else []
    while True:
        user_question = simpledialog.askstring("GPT-4 Query", "Ask me a question related to the Excel files (or type 'done' to process):")
        if user_question in [None, 'exit', 'quit', 'goodbye']:
            messagebox.showinfo("Goodbye", "Goodbye!")
            break
        elif user_question == 'done':
            if not questions:
                messagebox.showinfo("GPT-4 Query", "No questions submitted for processing.")
            else:
                responses = batch_process_questions(questions, excel_context)
                for response in responses:
                    messagebox.showinfo("GPT-4 Response", response)
            questions.clear()
        else:
            questions.append(user_question)

    save_session_data({'file_paths': file_paths, 'questions': questions})

    root.destroy()

if __name__ == "__main__":
    main()