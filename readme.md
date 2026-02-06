🏏 IPL Cricket Data API (Flask)

A RESTful API built using Flask and Pandas that provides IPL match, team, and batsman statistics from real IPL datasets.
This project is designed to help beginners understand backend development, REST APIs, and data handling using Python.

🚀 Features

📅 Fetch IPL match details

🏏 Get team-wise records and statistics

🧍 Retrieve batsman performance data

📦 JSON-based API responses

🧠 Beginner-friendly project structure

🛠 Tech Stack

Python

Flask – REST API framework

Pandas – Data processing & analysis

Git & GitHub



🔗 API Endpoints (Examples)
1️⃣ Home
GET /


Response

{
  "message": "Welcome to IPL Data API"
}

2️⃣ Team Records
GET /team?name=MI


Description
Returns match and performance details for the given IPL team.

3️⃣ Batsman Records
GET /batter?batsman=Virat Kohli


Description
Returns batsman statistics such as:

Matches

Innings

Runs

Strike Rate

🧪 How to Run Locally
Step 1️⃣ Clone the repository
git clone https://github.com/aryan7028/IPL_API.git
cd ipl-cricket-api

Step 2️⃣ Create virtual environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

Step 3️⃣ Install dependencies
pip install -r requirements.txt

Step 4️⃣ Run the Flask app
python app.py



📌 Learning Outcomes

Understanding REST API concepts

Using query parameters in Flask

Handling real-world datasets with Pandas

Structuring backend projects

API input validation and error handling

