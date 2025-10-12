##Project Overview
This project is a simple tool that lets you talk to a database using everyday language instead of code.

What it does: It takes a question you type (like, "How many students have over 90 marks?") and automatically turns it into a technical database command (SQL query).

How it works: It uses the smart Google Gemini Pro model to create the command, runs it against a local SQLite database, and shows you the final answer right away.

##Why This Project Was Built
We created this project to make getting data from a database much faster and easier for everyone.

No SQL Needed: You don't have to learn complicated SQL code to pull reports or find specific data. Just ask in English!

Quick Answers: Data analysts and business users can get the information they need instantly, without waiting for a developer to write a query for them.

Showcase AI Power: It’s a great example of how large AI models (LLMs) can handle complex tasks like translating human language into working computer code.

##Technologies Used
Google Gemini Pro: This is the core brain. It reads your question and writes the correct SQL code.

Python / Streamlit: This is the app's foundation. Streamlit creates the simple web screen where you type your question and see the results.

SQLite3 Database: This is the data storage. It's where all the student records (names, marks, class) are saved and queried.

python-dotenv: Used to securely load your Google API key from a private .env file.

##How This Project Is Useful
For People Who Need Data (Managers, Analysts)

Self-Service: You can get data yourself without asking technical teams for help.

Focus on Insights: Spend less time writing code and more time analyzing the results.

For Developers

Learning AI Integration: It shows you the best way to connect a Google LLM to a real-world database application.

Foundation for Bigger Tools: This code can be used as a starting point for building more powerful internal tools.
