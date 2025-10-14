# CHAT Platform

**Canvas-linked Human-AI Teaching: An AI-Integrated Learning Platform**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)](https://flask.palletsprojects.com/)

## Table of Contents

- [Overview](#overview)
- [Motivation](#motivation)
- [Technical Architecture](#technical-architecture)
- [Features](#features)
  - [Current Features](#current-features)
  - [Planned Features](#planned-features)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Research Components](#research-components)
- [License](#license)
- [Contact](#contact)

## Overview

CHAT (Canvas-linked Human-AI Teaching) is an AI-integrated learning platform designed to enhance student learning through customizable AI tutors while maintaining FERPA compliance and providing rich analytics for educational research. The platform serves as a bridge between AI-powered educational assistance and traditional learning management systems like Canvas.

**Project Status:** Active Development (Independent Study Project)  
**Institution:** University of Colorado Boulder, Aerospace Engineering Department  
**Advisor:** Professor Hodgkinson

## Motivation

Traditional AI chatbots for education face several critical challenges:

- **Lack of customization:** Generic AI responses don't align with specific pedagogical approaches or assignment requirements
- **Privacy concerns:** Many AI platforms send student data to external servers, violating FERPA compliance
- **Limited instructor control:** Educators have no way to guide AI behavior or enforce teaching methodologies
- **Missing analytics:** No systematic way to understand how students interact with AI tutors or measure effectiveness
- **No integration:** AI tools exist in isolation from existing educational infrastructure

CHAT addresses these challenges by providing:

1. **Customizable AI Personas** - Instructors can create multiple teaching personalities (Socratic, Visual, Step-by-Step, etc.)
2. **Local-First Architecture** - All data stored locally for complete FERPA compliance
3. **Instructor Control** - Full prompt management system with version control and testing capabilities
4. **Rich Analytics** - Comprehensive logging and visualization of student-AI interactions
5. **Canvas Integration** - Seamless submission workflow and grade synchronization
6. **Research Platform** - De-identified data access for educational researchers studying AI-enhanced learning

## Technical Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         Student Interface                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │ Chat UI      │  │ Persona      │  │ Assignment           │  │
│  │ (Dark/Light) │  │ Selector     │  │ Submission           │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Flask Application Server                    │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Authentication Layer (OAuth2 - Tapis/TACC)              │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                   │
│  ┌──────────────────┐  ┌──────────────────┐  ┌─────────────┐  │
│  │ Chat Handler     │  │ Prompt Manager   │  │ Canvas API  │  │
│  │ - Message routing│  │ - CRUD ops       │  │ Integration │  │
│  │ - Guardrails     │  │ - Versioning     │  │             │  │
│  └──────────────────┘  └──────────────────┘  └─────────────┘  │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  AI Model Interface (Multi-Model Support)                │  │
│  │  - GPT-4 / GPT-3.5                                       │  │
│  │  - Llama-3                                               │  │
│  │  - Gemini                                                │  │
│  │  - Local servers (GPT-OSS)                               │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                        Data Storage Layer                        │
│                                                                   │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────────────┐    │
│  │ Neo4j DB     │  │ JSON Logs    │  │ Markdown Prompts   │    │
│  │ - Students   │  │ - Chat       │  │ - Personality      │    │
│  │ - Classes    │  │   transcripts│  │ - Assignment       │    │
│  │ - Enrollment │  │ - Analytics  │  │ - Versioned        │    │
│  └──────────────┘  └──────────────┘  └────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     Instructor Dashboard                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │ Prompt       │  │ Analytics    │  │ Chat Log Browser     │  │
│  │ Editor       │  │ Dashboard    │  │ (De-identified)      │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Research Data Access                          │
│              (De-identified exports for researchers)             │
└─────────────────────────────────────────────────────────────────┘
```

### Technology Stack

- **Backend:** Flask (Python 3.8+)
- **Database:** Neo4j (graph database for student-class relationships)
- **Authentication:** OAuth2 (Tapis/TACC)
- **AI Models:** OpenAI API, Google Gemini, Meta Llama, local model support
- **Frontend:** HTML5, CSS3, JavaScript (vanilla + modern frameworks TBD)
- **Visualization:** Plotly.js / Chart.js
- **Containerization:** Docker
- **LMS Integration:** Canvas API
- **Data Storage:** JSON (chat logs), Markdown (prompts)

## Features

### Current Features

The following features are implemented in the proof-of-concept:

✅ **AI Chat Interface**
- GPT-based Socratic math helper
- Real-time conversation with context awareness
- Customizable system prompts

✅ **Authentication & Authorization**
- OAuth2 authentication via Tapis/TACC
- Secure session management
- User role differentiation (student/instructor)

✅ **Data Persistence**
- Chat logs saved to JSON files
- Neo4j database for student-class relationships
- Local storage for FERPA compliance

✅ **Canvas Integration (Basic)**
- Unique code generation for credit submission
- Student identification and verification

✅ **Deployment**
- Docker containerization
- Flask server architecture
- Production-ready infrastructure

### Planned Features

The following features are under active development as part of the independent study:

#### 🎨 Frontend & User Experience (Phase 1)

- **Modern Chat Interface**
  - Dark/light theme toggle
  - Typing indicators
  - Message persistence and history
  - Responsive design (mobile, tablet, desktop)
  - Accessibility features (WCAG 2.1 AA compliance)

- **Student Dashboard**
  - Assignment list and status
  - Chat history browser
  - Persona selector
  - Progress tracking
  - Reflection submission interface

- **Instructor Dashboard**
  - Canvas-style interface design
  - Course and assignment management
  - Student analytics overview
  - Quick access to prompt editing

#### 📝 Prompt Management System (Phase 2)

- **CRUD Operations**
  - Create new prompts from templates
  - Edit existing prompts with live preview
  - Delete unused prompts (with safety checks)
  - Duplicate prompts for variations

- **Version Control**
  - Automatic backup on every edit
  - Rollback to previous versions
  - View version history and diff
  - Change notes and documentation

- **Organization & Discovery**
  - Tag system (course, assignment, difficulty)
  - Search and filter
  - Folder structure for organization

- **Testing & Preview**
  - Test prompts before publishing to students
  - Preview with different AI models
  - Sample conversation simulator

- **AI-Assisted Prompt Creation**
  - Tutorial system for using ChatGPT to generate prompts
  - Best practices guide
  - Template library

#### 👥 Persona System (Phase 3)

- **Multiple AI Tutor Personalities**
  - **Socratic Tutor:** Asks guiding questions, encourages critical thinking
  - **Visual Tutor:** Emphasizes diagrams, analogies, and visual explanations
  - **Step Solver:** Breaks problems into discrete steps with clear progression
  - **Explainer:** Provides detailed conceptual explanations with examples

- **Persona Configuration**
  - Student persona selector (choose preferred teaching style)
  - Instructor persona assignment (set default per assignment)
  - Persona-specific prompt templates
  - Personality trait customization

- **Guardrails & Middleware**
  - Socratic mode: Blocks direct answers, enforces question-based responses
  - Exam Proctor mode: Restricts hint depth, prevents full solutions
  - Homework Helper mode: Allows more detailed guidance
  - Custom guardrail rules per persona

- **Persona Analytics**
  - Compare effectiveness across different personas
  - Student preference tracking
  - Learning outcome correlation
  - A/B testing framework

#### 📊 Analytics & Visualization (Phase 4)

- **Chat Log Browser**
  - De-identified conversation viewer
  - Filter by course, assignment, date, persona, model
  - Search within conversations
  - Export individual or bulk transcripts

- **Metrics Dashboard**
  - Total chats per day/week/semester
  - Average conversation length
  - Message count distributions
  - Model usage statistics
  - Most common questions/keywords
  - Time-of-day usage patterns

- **Interactive Visualizations**
  - Plotly.js or Chart.js powered charts
  - Heatmaps of activity
  - Trend analysis over time
  - Persona comparison charts

- **Export & Integration**
  - CSV/JSON export for research
  - API for external analytics tools
  - Canvas integration: AI Summary Viewer

#### 🔗 Enhanced Canvas Integration (Phase 5)

- **Student Features**
  - "Submit Chat Reflection" button in chat UI
  - Package chat transcript + reflection
  - Submit directly to Canvas assignments
  - Confirmation and status tracking

- **Instructor Features**
  - Feedback panel for rubric notes
  - AI-generated chat summaries as private notes
  - Grade import/export
  - Assignment mapping (link Canvas assignments to CHAT prompts)

- **Automation**
  - Automatic credit for participation
  - Reflection requirement enforcement
  - Due date synchronization

#### 🧪 Testing & Documentation (Phase 6)

- **Usability Testing**
  - Student testing sessions
  - Instructor feedback collection
  - Iterative design improvements
  - Qualitative feedback analysis

- **Documentation**
  - Developer documentation
  - API reference
  - Instructor user guide
  - Student tutorials
  - Deployment guide

- **Presentation Materials**
  - EEF Symposium presentation
  - Demo videos and walkthroughs
  - UI mockups and designs
  - Research poster

#### 🚀 Advanced Features (Stretch Goals)

- **Pseudo-Student Testing**
  - AI students with different profiles (struggling, advanced, visual learner, etc.)
  - Automated prompt testing before deployment
  - Simulated conversation generation
  - Edge case detection

- **RLHF System (Reinforcement Learning from Human Feedback)**
  - Instructor correction interface
  - "Overseer" AI analyzes corrections
  - Automatic prompt refinement
  - Continuous improvement loop

- **Chat Replay Controls**
  - VCR-style interface (play, pause, step)
  - Slider to navigate through conversation timeline
  - Annotation and commenting
  - Side-by-side comparison

- **C-to-Assembly Visualizer**
  - Interactive tool for Computer Architecture courses
  - Visual representation of code translation
  - Stack and register state visualization
  - Step-by-step execution

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- Docker and Docker Compose
- Neo4j database
- OpenAI API key (or other AI model credentials)
- Canvas API credentials
- Tapis/TACC OAuth2 credentials

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/chat-platform.git
   cd chat-platform
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

   Required environment variables:
   ```
   FLASK_SECRET_KEY=your-secret-key
   OPENAI_API_KEY=your-openai-key
   NEO4J_URI=bolt://localhost:7687
   NEO4J_USER=neo4j
   NEO4J_PASSWORD=your-neo4j-password
   CANVAS_API_URL=https://canvas.colorado.edu
   CANVAS_API_TOKEN=your-canvas-token
   TAPIS_CLIENT_ID=your-tapis-client-id
   TAPIS_CLIENT_SECRET=your-tapis-secret
   ```

5. **Start Neo4j database**
   ```bash
   docker-compose up -d neo4j
   ```

6. **Run database migrations**
   ```bash
   python manage.py db_setup
   ```

7. **Start the Flask development server**
   ```bash
   flask run
   ```

   The application will be available at `http://localhost:5000`

### Docker Deployment

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

2. **Access the application**
   - Web interface: `http://localhost:5000`
   - Neo4j browser: `http://localhost:7474`

### Production Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed production deployment instructions.

## Usage

### For Students

1. **Log in** using your university credentials (Tapis/TACC OAuth2)
2. **Select an assignment** from your dashboard
3. **Choose an AI tutor persona** (Socratic, Visual, Step Solver, or Explainer)
4. **Start chatting** with the AI tutor about your assignment
5. **Submit your reflection** when you're done to receive Canvas credit

### For Instructors

1. **Log in** with instructor credentials
2. **Create or edit prompts** in the Prompt Management interface
3. **Assign personas** to specific assignments
4. **Monitor student interactions** through the Analytics Dashboard
5. **Review chat logs** (de-identified) to understand student struggles
6. **Provide feedback** on student reflections through Canvas integration

### For Researchers

1. **Request data access** from the project administrator
2. **Export de-identified chat logs** in CSV/JSON format
3. **Analyze patterns** in student-AI interactions
4. **Collaborate** with the development team on new features

## Project Structure

```
chat-platform/
├── app/
│   ├── __init__.py           # Flask app initialization
│   ├── auth/                 # Authentication (OAuth2)
│   ├── models/               # Database models
│   ├── routes/               # API endpoints
│   ├── services/             # Business logic
│   │   ├── ai_service.py     # AI model interface
│   │   ├── prompt_service.py # Prompt management
│   │   ├── analytics.py      # Analytics generation
│   │   └── canvas.py         # Canvas API integration
│   ├── static/               # CSS, JS, images
│   ├── templates/            # HTML templates
│   └── utils/                # Helper functions
├── data/
│   ├── chat_logs/            # JSON chat transcripts
│   ├── prompts/              # Markdown prompt files
│   └── backups/              # Version control backups
├── tests/
│   ├── unit/                 # Unit tests
│   ├── integration/          # Integration tests
│   └── e2e/                  # End-to-end tests
├── docs/
│   ├── api/                  # API documentation
│   ├── guides/               # User guides
│   └── research/             # Research papers and notes
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── .env.example              # Environment variables template
├── .gitignore
├── requirements.txt          # Python dependencies
├── PROPOSAL.md               # Independent study proposal
├── CONTRIBUTIONS.md          # Contribution guidelines
├── LICENSE
└── README.md                 # This file
```

## Roadmap

### Spring 2026 Semester (15 weeks)

#### Weeks 1-3: Foundation & Infrastructure
- Define prompt schema and file structure
- Implement CRUD interface for prompt management
- Add preview and testing functionality
- Publish/rollback version control system

#### Weeks 4-6: Persona System
- Implement persona selector UI
- Create persona-specific prompt templates
- Develop guardrail middleware
- Persist persona_id in chat logs

#### Weeks 7-9: Analytics & Visualization
- Build analytics dashboard
- Implement persona comparison charts
- Add export functionality (CSV/JSON)
- Create interactive visualizations

#### Weeks 10-12: Canvas Integration
- Assignment mapping system
- Student submission workflow
- Instructor feedback panel
- AI-generated summaries

#### Weeks 13-15: Testing, Documentation & Presentation
- Usability testing with real students/instructors
- Comprehensive documentation
- EEF Symposium presentation preparation
- Research paper draft

### Future Enhancements (Post-Independent Study)

- **Summer 2026:** RLHF system implementation, pseudo-student testing
- **Fall 2026:** Multi-institution deployment, research paper publication
- **Spring 2027:** Advanced visualizations, C-to-Assembly tool, mobile app

## Contributing

This project is part of an independent study, but we welcome contributions from the broader educational technology community.

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guide for Python code
- Write unit tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR
- Add comments for complex logic
- Maintain FERPA compliance in all features

See [CONTRIBUTIONS.md](CONTRIBUTIONS.md) for detailed contribution information.

## Research Components

This project includes significant research components investigating:

1. **Prompt Engineering for Education**
   - How do different prompt structures affect learning outcomes?
   - What makes an effective Socratic tutoring prompt?

2. **AI Persona Effectiveness**
   - Do students learn better with certain AI personalities?
   - How does persona preference correlate with learning style?

3. **Reinforcement Learning from Human Feedback (RLHF)**
   - Can instructor corrections automatically improve AI prompts?
   - How quickly can an "overseer" AI adapt to teaching preferences?

4. **Educational Data Mining**
   - What patterns emerge in student-AI interactions?
   - Can we predict student struggles before they ask for help?

5. **AI Integration in Traditional LMS**
   - What barriers exist to adopting AI tutors in existing courses?
   - How can AI enhance rather than replace instructor interaction?

### Research Collaboration

We are actively seeking collaboration with educational researchers. If you're interested in accessing de-identified data or collaborating on research questions, please contact:

- **Project Lead:** Kaitlyn Samuelian (kaitlyn.samuelian@colorado.edu)
- **Faculty Advisor:** Professor Hodgkinson (CU Boulder Aerospace Engineering)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Professor Hodgkinson** - Faculty advisor and project sponsor
- **CU Boulder Aerospace Engineering Department** - Institutional support
- **TACC (Texas Advanced Computing Center)** - Authentication infrastructure
- **Students and instructors** participating in usability testing

## Contact

**Project Lead:** Kaitlyn Samuelian  
**Email:** kaitlyn.samuelian@colorado.edu  
**Institution:** University of Colorado Boulder  
**Department:** Aerospace Engineering  

**Project Repository:** https://github.com/yourusername/chat-platform  
**Project Website:** [Coming soon]

---

*This project is part of an independent study course at CU Boulder and is under active development. Features and documentation are continuously evolving.*

