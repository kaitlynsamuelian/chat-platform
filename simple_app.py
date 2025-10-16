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

# Prompts directory
PROMPT_DIR = Path('prompts')
PROMPT_DIR.mkdir(exist_ok=True)


def get_available_prompts():
    """Load all available prompts from prompts/ directory and subdirectories"""
    prompts = {}
    # Search recursively for all .md files
    for file in PROMPT_DIR.rglob('*.md'):
        prompt_id = file.stem  # filename without extension
        prompt_content = file.read_text()
        # Extract title from first line if it's a markdown header
        first_line = prompt_content.split('\n')[0]
        if first_line.startswith('#'):
            title = first_line.lstrip('#').strip()
        else:
            title = prompt_id.replace('_', ' ').title()
        
        prompts[prompt_id] = {
            'id': prompt_id,
            'title': title,
            'content': prompt_content
        }
    return prompts


@app.route('/')
def index():
    """Main chat page"""
    return render_template('simple_chat.html')


@app.route('/api/prompts')
def list_prompts():
    """API endpoint to get available prompts organized by subject"""
    prompts = get_available_prompts()
    
    # Organize by subject
    by_subject = {
        'Math': [],
        'Biology': [],
        'Physics': [],
        'General': []
    }
    
    for prompt_id, prompt_data in prompts.items():
        title = prompt_data['title']
        if '- Math' in title:
            by_subject['Math'].append({'id': prompt_id, 'title': title})
        elif '- Biology' in title:
            by_subject['Biology'].append({'id': prompt_id, 'title': title})
        elif '- Physics' in title:
            by_subject['Physics'].append({'id': prompt_id, 'title': title})
        else:
            by_subject['General'].append({'id': prompt_id, 'title': title})
    
    return jsonify({
        'by_subject': by_subject,
        'all_prompts': [
            {'id': p['id'], 'title': p['title']} 
            for p in prompts.values()
        ]
    })


@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    data = request.json
    user_message = data.get('message', '')
    conversation_history = data.get('history', [])
    prompt_id = data.get('prompt_id', 'math_tutor')  # Default to math_tutor
    
    try:
        # Load the selected prompt
        prompts = get_available_prompts()
        if prompt_id not in prompts:
            prompt_id = 'math_tutor'  # Fallback
        
        system_prompt = prompts[prompt_id]['content'] if prompts else 'You are a helpful AI tutor.'
        
        # Build messages for OpenAI
        messages = []
        
        # Add system prompt from file
        messages.append({
            'role': 'system',
            'content': system_prompt
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
        
        # Save the chat with prompt info
        save_chat(messages, ai_response, prompt_id)
        
        return jsonify({
            'success': True,
            'response': ai_response
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


def save_chat(messages, ai_response, prompt_id='unknown'):
    """Save chat to JSON file"""
    timestamp = datetime.now().isoformat()
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    chat_data = {
        'timestamp': timestamp,
        'prompt_used': prompt_id,
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

