AI Brute Force Attack Detector
Project Overview
This is a Machine Learning-powered cybersecurity tool designed to identify brute force login attempts within network logs. Unlike static security rules, this system uses a Random Forest Classifier to detect behavioral patterns of attackers, making it more resilient against "low and slow" attack vectors.

The application includes an automated PowerPoint generator that creates a project summary presentation every time the app is launched.

🚀 How to Run the Project
1. Prerequisites
Python 3.x: Ensure Python is installed and added to your system PATH.

VS Code: Recommended for the integrated terminal experience.


Libraries: You will need the libraries listed in the requirements.txt file (streamlit, pandas, scikit-learn, python-pptx).

2. Installation
To avoid "File Not Found" errors, ensure your terminal is pointed to the correct project directory:

Open the Project Folder: Open VS Code, go to File > Open Folder, and select the extracted brute force folder.

Open Terminal: Press Ctrl + ` or go to Terminal > New Terminal.

Install Tools: Run the following command to install the necessary dependencies:

PowerShell

pip install -r requirements.txt
3. Launching the App
Streamlit applications must be launched using the Streamlit module. Run the following command in your terminal:

PowerShell

python -m streamlit run app.py
🛠️ Key Features
Machine Learning Logic: Uses a Random Forest Classifier to analyze attempt velocity, failure ratios, and identity scope.

Dynamic Data Analysis: Upload any login log in CSV format and map your specific columns (IP, Attempts, Usernames) via the sidebar.

Visualization: Real-time distribution charts showing the difference between normal traffic and detected threats.

Auto-Presentation: A BruteForce_Presentation.pptx file is automatically generated in the project root folder upon startup.

❓ Troubleshooting
"Streamlit is not recognized": This happens if your Python Scripts folder is not in your Windows PATH. Use python -m streamlit run app.py as a reliable workaround.

"No such file or directory": Always ensure your terminal prompt path (e.g., C:\Users\...\brute force>) matches the folder where app.py is located.