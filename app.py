# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load chemistry Q&A data
qa_data = pd.read_csv('~/Documents/chemistry_chatbot/data/chemistry_question_utf8.csv')

def find_response(question):
    response = "I'm not sure about that chemistry question."
    for _, row in qa_data.iterrows():
        if question.lower() in row['question'].lower():
            response = row['response']
            break
    return response

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_question = data.get("question", "")
    answer = find_response(user_question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
