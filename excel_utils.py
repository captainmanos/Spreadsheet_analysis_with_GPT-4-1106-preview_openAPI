import pandas as pd
from tkinter import messagebox
import logging

def read_excel_files(file_paths):
    data_frames = []
    for file_path in file_paths:
        try:
            df = pd.read_excel(file_path)
            data_frames.append(df)
            logging.info(f'Successfully read {file_path}')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read {file_path} with error: {str(e)}")
            logging.error(f"Failed to read {file_path} with error: {str(e)}")
            continue

    if data_frames:
        excel_data_as_text = "\n".join([df.to_csv(index=False, sep='\t') for df in data_frames])
        return excel_data_as_text
    return None