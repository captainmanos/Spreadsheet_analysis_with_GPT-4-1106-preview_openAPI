 Excel Data GPT-4 Query Application

 Overview
The Excel Data GPT-4 Query Application is an interactive tool that allows users to import Excel files and ask questions related to the data contained within these files using OpenAI's GPT-4 model. The application uses a graphical user interface built with Tkinter to facilitate user interactions, enabling the selection of Excel files and input of user queries. GPT-4 uses the context provided by the data in the Excel files to generate answers.

 Installation
Before running the application, please ensure you have installed the following required Python packages:

- tkinter: for the GUI components.
- pandas: for handling Excel files.
- openai: for interfacing with the OpenAI API and GPT-4 model.

These packages can be installed via pip using the following commands:
```bash
pip install tk
pip install pandas
pip install openai
```

 Environment Setup
To access the OpenAI API services, you will need an API key from OpenAI. Please obtain one from their website and set it as an environment variable with the name 'OPENAI_API_KEY'.
On UNIX systems, here's how you can set the environment variable temporarily in the terminal:
```bash
export OPENAI_API_KEY='your-key-here'
```

On Windows, you can set the environment variable as follows:
```bash
set OPENAI_API_KEY=your-key-here
```

Ensure that it's correctly set before running the application as it's required for communication with OpenAI's services.

Usage Instructions
1. Launch the application by running the `main` function.
2. Use the file dialog to select one or more Excel files (with extensions .xlsx or .xls).
3. Ask the application questions related to the data in the Excel files using the dialog box that appears.
4. Type 'done' when you finish with your questions to receive the responses from GPT-4, or input 'exit', 'quit', or 'goodbye' to end the application.

 Session Management
The application can save your session, including the Excel files' paths you've loaded and the questions you've asked, and load this data the next time you start the application.

The `session_manager` manages this functionality, utilizing a `session.json` file. Any errors during the session's save or load process are logged for troubleshooting.

 Logging
The application logs its activities and errors to an 'app.log' file. This feature is configured in the `logger_config` section and can assist in diagnosing issues that may arise during operation.

Feel free to reach out if any problems occur or if you have any questions regarding the functionality of the application.
