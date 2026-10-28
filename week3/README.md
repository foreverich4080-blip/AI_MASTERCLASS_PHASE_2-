Matatu SACCO AI Assistant

What Is This?

The Matatu SACCO AI Assistant is a small AI-powered program that helps SACCO members get answers to common questions.

Instead of needing to remember a specific command, a member can simply type a question in normal language.

For example:

«Member: What's my balance?»

«Assistant: Your current balance is KSh 12,500.»

The assistant understands different ways of asking the same question.

For example:

- "What's my balance?"
- "How much money do I have?"
- "Tell me how much is in my account."

These can all be understood as asking for the member's balance.

---

How Does It Work?

The program has three main parts:

1. The Member

The member types a question into the program.

What's my balance?

2. The Python Application

The Python program receives the question and sends it to Google's Gemini AI.

It also provides Gemini with the SACCO information that the assistant is allowed to use.

3. Gemini AI

Gemini understands what the member is asking and generates a natural-language answer.

The answer is then displayed back to the member.

The Complete Process

Member asks a question
        ↓
Python receives the question
        ↓
Python sends it to Gemini
        ↓
Gemini understands the question
        ↓
Gemini uses the provided SACCO information
        ↓
Gemini generates an answer
        ↓
The answer is shown to the member

---

What Information Does It Know?

For this demonstration, the assistant has the following SACCO information:

- Member balance: KSh 12,500
- Next meeting: Saturday at 10:00 AM
- Membership fee: KSh 1,000

This information is currently demonstration data.

The program is not connected to a real SACCO database.

---

How To Run It

You don't need to understand the code to run the application, but you do need Python and a Gemini API key.

What You Need

Before starting, you need:

1. A computer
2. Python 3.12 or newer
3. An internet connection
4. A Google Gemini API key

---

Step 1 — Get the Project

Download or clone this project onto your computer.

Open a terminal inside the project folder.

---

Step 2 — Install the Required Components

Run:

pip install google-genai python-dotenv

These components allow the program to communicate with Gemini and securely read the API key.

---

Step 3 — Add Your Gemini API Key

Inside the project folder, create a file called:

.env

Put your Gemini API key inside it:

GEMINI_API_KEY=your_api_key_here

The API key allows the program to communicate with Google's Gemini service.

Important

Never share your API key with other people.

The ".env" file is intentionally excluded from GitHub so that the private key is not uploaded.

---

Step 4 — Start the Assistant

Open the terminal in the folder containing the program and run:

python "DAY1 PRACTICE.py"

The program will ask:

Ask the SACCO assistant:

Type your question.

For example:

What's my balance?

Press Enter.

The program sends the question to Gemini and displays the answer.

---

Examples

Asking about the balance

Ask the SACCO assistant: What's my balance?

SACCO Assistant:
Your current balance is KSh 12,500.

Asking about the meeting

Ask the SACCO assistant: When is the next meeting?

SACCO Assistant:
The next meeting is Saturday at 10:00 AM.

Asking about membership

Ask the SACCO assistant: How much is membership?

SACCO Assistant:
The membership fee is KSh 1,000.

---

What Happens If Gemini Is Temporarily Unavailable?

The program has basic error handling.

If Google's Gemini service temporarily returns an error, the program will automatically try the request again up to 5 times.

Question
   ↓
Try
   ↓
Temporary error?
   ↓
Try again
   ↓
Try again
   ↓
Successful response

If the service remains unavailable, the program tells the user instead of crashing.

---

Important Limitation

This is an educational prototype, not a production SACCO system.

The member information is currently written into the program for demonstration purposes.

A real version would connect to a database:

Real SACCO database
        ↓
Member information
        ↓
Python application
        ↓
AI assistant
        ↓
Member

That would allow the assistant to retrieve the member's actual balance, meeting information, payments, and other authorized information.

---

What This Project Demonstrates

This project demonstrates the basic foundation of an AI-powered application:

- Sending information to an AI through an API
- Receiving an AI-generated response
- Giving the AI specific instructions
- Giving the AI information to work with
- Handling temporary API failures
- Keeping API credentials private
- Monitoring API usage

The important idea is that AI is being used as part of a software application, rather than simply being used through a chat interface.

---

Technology

- Python
- Google Gemini API
- Google GenAI Python SDK
- python-dotenv

Project Status

Educational prototype — completed as part of an AI Developer learning project.

Future versions could add:

- A real database
- Member authentication
- Real-time member balances
- Conversation history
- Web or mobile interface
- AI tool/function calling
- More SACCO services