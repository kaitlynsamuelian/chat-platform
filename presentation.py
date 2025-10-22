"""
Presentation Version - Simple Flask chatbot built from math.md file
Initial version: Single math.md knowledge file
Focused on solving math problems and explaining step-by-step reasoning
Simple Q&A format — no personas or adaptive behavior (yet!)
"""
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
import json
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key')

# OpenAI setup
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Data directory
DATA_DIR = Path('chat_data')
DATA_DIR.mkdir(exist_ok=True)

# Load Math Tutor Prompt from math.md file
def load_math_prompt():
    """Load the math tutor prompt from math.md file"""
    math_file = Path('math.md')
    if math_file.exists():
        return math_file.read_text()
    else:
        # Fallback if file doesn't exist
        return "You are a helpful math tutor."

MATH_TUTOR_PROMPT = load_math_prompt()


@app.route('/')
def index():
    """Main chat page"""
    return render_template('presentation.html')


@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    data = request.json
    user_message = data.get('message', '')
    conversation_history = data.get('history', [])
    
    try:
        # Build messages for OpenAI
        messages = []
        
        # Add system prompt
        messages.append({
            'role': 'system',
            'content': MATH_TUTOR_PROMPT
        })
        
        # Add conversation history
        messages.extend(conversation_history)
        
        # Add current message
        messages.append({
            'role': 'user',
            'content': user_message
        })
        
        # Call OpenAI
        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=messages,
            temperature=0.7
        )
        
        ai_response = response.choices[0].message.content
        
        # Save the chat
        save_chat(messages, ai_response)
        
        return jsonify({
            'success': True,
            'response': ai_response
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


def save_chat(messages, ai_response):
    """Save chat to JSON file"""
    timestamp = datetime.now().isoformat()
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    chat_data = {
        'timestamp': timestamp,
        'messages': messages,
        'ai_response': ai_response
    }
    
    # Save to file
    filename = DATA_DIR / f'presentation_chat_{date_str}.json'
    
    # Append to existing file or create new
    if filename.exists():
        with open(filename, 'r') as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = [data]
        data.append(chat_data)
    else:
        data = [chat_data]
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)


if __name__ == '__main__':
    print("🎓 Starting Math Tutor on http://localhost:8001")
    print("   📄 Loading prompt from: math.md")
    print("   🔑 Make sure you have OPENAI_API_KEY in .env file")
    app.run(debug=True, port=8001)

