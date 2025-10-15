"""
Simple Flask chatbot app - mimics custom GPT with chat saving
Just needs .env with OPENAI_API_KEY
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

# OpenAI setup (new API v1.0+)
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Data directory
DATA_DIR = Path('chat_data')
DATA_DIR.mkdir(exist_ok=True)


@app.route('/')
def index():
    """Main chat page"""
    return render_template('simple_chat.html')


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
            'content': 'You are a helpful AI tutor for math problems. Guide students without giving direct answers.'
        })
        
        # Add conversation history
        messages.extend(conversation_history)
        
        # Add current message
        messages.append({
            'role': 'user',
            'content': user_message
        })
        
        # Call OpenAI (new API v1.0+)
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
    filename = DATA_DIR / f'chat_{date_str}.json'
    
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
    print("🚀 Starting simple chatbot on http://localhost:5000")
    print("   Make sure you have OPENAI_API_KEY in .env file")
    app.run(debug=True, port=5000)

