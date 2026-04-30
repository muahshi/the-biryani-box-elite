import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app) # Ye important hai taaki frontend backend se baat kar sake

# Groq Client setup
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route('/api/get-ai-tips', methods=['GET'])
def get_tips():
    try:
        user_name = request.args.get('user', 'Biryani Lover')
        
        # Groq AI Logic
        prompt = f"Create a short, premium 1-line greeting in Hinglish for {user_name} visiting 'The Biryani Box' cloud kitchen in Bhopal. Mention a spicy recommendation like 21 Spices Biryani. Keep it witty."
        
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        
        ai_response = chat_completion.choices[0].message.content
        return jsonify({"text": ai_response})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel Flask ke liye ye line kaafi hai
app = app
