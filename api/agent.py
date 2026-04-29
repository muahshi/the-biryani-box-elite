import os
from groq import Groq
from flask import Flask, request, jsonify

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route('/api/get-ai-tips', methods=['GET'])
def get_tips():
    user = request.args.get('user', 'Biryani Lover')
    day = request.args.get('day', 'Friday')
    
    prompt = f"Create a short 1-line greeting for {user} for {day} at 'The Biryani Box' cloud kitchen. Suggest a spicy item from menu. Use Hinglish."
    
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192",
    )
    
    return jsonify({"text": chat_completion.choices[0].message.content})

