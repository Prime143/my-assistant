from flask import Flask, request, jsonify
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import json
import random
import pyjokes

app = Flask(__name__)

# Load user data (favorite songs, websites)
def load_user_data():
    try:
        with open('user_data.json', 'r') as f:
            user_data = json.load(f)
    except FileNotFoundError:
        user_data = {
            "favorite_songs": [],
            "favorite_websites": [],
            "user_feedback": {}
        }
    return user_data

# Save user data (favorite songs, websites)
def save_user_data(data):
    with open('user_data.json', 'w') as f:
        json.dump(data, f, indent=4)

# Assistant logic (unchanged from your code)
def assistant_logic(query):
    user_data = load_user_data()
    query = query.lower()

    if "how are you" in query or "how's your day" in query:
        return "I'm doing great! Thanks for asking, but I'm still better than you!"
    if "wikipedia" in query:
        query = query.replace('wikipedia', '')
        try:
            results = wikipedia.summary(query, sentences=2, auto_suggest=False)
            return results
        except Exception as e:
            return "Sorry, I couldn't find anything on Wikipedia."
    if "open youtube" in query:
        webbrowser.open("youtube.com")
        return "Opening YouTube..."
    if "open google" in query:
        webbrowser.open("google.com")
        return "Opening Google..."
    if "tell me a joke" in query:
        joke = pyjokes.get_joke(language="en", category="neutral")
        return joke
    return "Sorry, I didn’t understand that. Try again!"

@app.route('/assistant', methods=['POST'])
def assistant():
    data = request.get_json()
    query = data['query'].lower()
    response = assistant_logic(query)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


if __name__ == "__main__":
    app.run(debug=True)
