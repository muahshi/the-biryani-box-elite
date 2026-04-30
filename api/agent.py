```python
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

# Flask app initialization
app = Flask(__name__)
CORS(app)

# Groq Client setup
# Note: Ensure GROQ_API_KEY is set in Vercel Environment Variables
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route('/api/get-ai-tips', methods=['GET'])
def get_tips():
    try:
        user_name = request.args.get('user', 'Biryani Lover')
        
        # AI Prompt for Bhopal Cloud Kitchen context
        prompt = (
            f"Create a short, premium 1-line greeting in Hinglish for {user_name} "
            f"visiting 'The Biryani Box' cloud kitchen in Bhopal. "
            f"Mention a spicy recommendation like 21 Spices Biryani or Chicken Tikka. "
            f"Keep it witty and royal."
        )
        
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        
        ai_response = chat_completion.choices[0].message.content
        return jsonify({"text": ai_response})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Required for Vercel to pick up the app
if __name__ == "__main__":
    app.run()

```
