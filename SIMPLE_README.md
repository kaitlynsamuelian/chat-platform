# Simple AI Tutor with Custom Prompts

This is the **simple version** - a Flask app with customizable AI tutors and chat saving.

## What You Need

1. Python 3.8+
2. OpenAI API key

## Features

✅ **Custom Prompts** - Teachers can create their own AI tutors!
✅ **Multiple Tutors** - Switch between different teaching styles
✅ **Chat Saving** - All conversations saved locally as JSON
✅ **Simple** - Just drop .md files, no coding needed

## Setup (2 minutes)

1. **Create .env file:**
```bash
echo "OPENAI_API_KEY=sk-your-key-here" > .env
```

2. **Install packages:**
```bash
pip install flask openai python-dotenv
```

3. **Run it:**
```bash
python simple_app.py
```

4. **Open:** http://localhost:5000

That's it! 🎉

## What It Does

- **Custom AI Tutors** - Choose from different teaching personalities
- **Teacher-Customizable** - Add new tutors by dropping .md files in `prompts/` folder
- **Chat Interface** - Clean web interface at `http://localhost:5000`
- **Local Storage** - Saves all chats to `chat_data/` folder as JSON (FERPA compliant)
- **Tracks Usage** - Logs which prompt was used for each conversation

## How to Add Custom Prompts (For Teachers)

1. Create a new `.md` file in the `prompts/` folder
2. Name it something like `calculus_tutor.md` or `physics_helper.md`
3. Write your prompt using this format:

```markdown
# Your Tutor Name

You are a [describe the tutor's role and personality].

Your teaching style:
- [Instruction 1]
- [Instruction 2]
- [Instruction 3]

[Any other guidelines for the AI]
```

4. Save the file and refresh the webpage
5. Your new tutor appears in the dropdown!

### Example Prompts Included:

- **Math Tutor** - Guides students through math problems
- **Socratic Tutor** - Only asks questions, never gives answers
- **Physics Helper** - Specializes in physics with real-world examples

## Files

- `simple_app.py` - The Flask app (just ~100 lines)
- `templates/simple_chat.html` - The chat page
- `chat_data/` - Where chats are saved

## Saved Chats

Chats are saved as JSON in `chat_data/chat_YYYY-MM-DD.json`

Each chat includes:
- Timestamp
- All messages in conversation
- AI responses

---

**Note:** There's also a full-featured version in the `app/` directory with Neo4j, authentication, multiple personas, etc. But this simple version matches what your professor described.

