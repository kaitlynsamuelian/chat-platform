# CHAT Platform

**Canvas-linked Human-AI Teaching: An AI-Integrated Learning Platform**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)](https://flask.palletsprojects.com/)

## Overview

CHAT (Canvas-linked Human-AI Teaching) is an AI-integrated learning platform that gives instructors control over AI tutor behavior while maintaining student privacy and integrating with Canvas LMS.

**Project Status:** Early Development (Independent Study Project)  
**Institution:** University of Colorado Boulder, Aerospace Engineering Department  
**Advisor:** Professor Hodgkinson

## Why CHAT?

Current AI tutoring tools have significant limitations:
- Generic responses that don't align with instructor teaching methods
- Privacy concerns with student data sent to external servers
- No instructor control over AI behavior
- No integration with existing course infrastructure
- Missing analytics on how students use AI

CHAT addresses these by providing customizable AI tutors, local data storage for FERPA compliance, and seamless Canvas integration.

## Current Features

The proof-of-concept currently has:

- ✅ Flask server with GPT-based chat functionality
- ✅ OAuth2 authentication (Tapis/TACC)
- ✅ Neo4j database for student-class relationships
- ✅ JSON-based chat logging
- ✅ Docker containerization
- ✅ Basic Canvas integration (unique code generation)

## Planned Development

As part of the independent study, the following features are being developed:

### Frontend & User Experience
- Modern, accessible chat interface with dark/light themes
- Student and instructor dashboards
- Responsive design for mobile and desktop

### Prompt Management System
- Interface for instructors to create and edit AI prompts
- Version control with backups and rollback
- Testing and preview before deployment
- Organization with tags and search

### Multi-Persona AI Tutors
- Different teaching styles (Socratic, Visual, Step-by-Step, Explainer)
- Student persona selector
- Guardrails to enforce teaching methodologies
- Analytics comparing persona effectiveness

### Analytics Dashboard
- View de-identified student conversations
- Usage metrics and patterns
- Filter and export chat logs for research
- Interactive visualizations

### Canvas Integration
- Student reflection submission workflow
- Assignment mapping (link Canvas assignments to prompts)
- Instructor feedback interface
- Automatic participation credit

### Research Components
- Studying AI persona effectiveness
- Understanding student interaction patterns
- Investigating prompt engineering for education
- Supporting educational technology research

## Technology Stack

- **Backend:** Flask (Python)
- **Database:** Neo4j (graph database)
- **Authentication:** OAuth2 (Tapis/TACC)
- **AI Models:** OpenAI GPT, with support for multiple models
- **Frontend:** HTML/CSS/JavaScript
- **Deployment:** Docker
- **LMS:** Canvas API integration

## Installation

See [GETTING_STARTED.md](GETTING_STARTED.md) for detailed setup instructions.

**Quick start with Docker:**
```bash
git clone https://github.com/yourusername/chat-platform.git
cd chat-platform
cp .env.example .env
# Edit .env with your API keys
docker-compose up --build
```

## Project Structure

```
chat-platform/
├── app/                    # Flask application
├── data/                   # Chat logs and prompts
├── tests/                  # Test suite
├── docker/                 # Docker configuration
├── README.md              # This file
├── PROPOSAL.md            # Independent study proposal
└── CONTRIBUTIONS.md       # Planned contributions
```

## Research Focus

This project investigates several research questions:

1. How do different AI teaching personalities affect student learning?
2. Do students naturally choose personas that match their learning styles?
3. What patterns emerge in student-AI interactions?
4. What barriers exist to instructor adoption of AI tools?

De-identified data will be available to educational researchers studying AI-enhanced learning.

## Timeline

**Spring 2026 (15 weeks):**
- Weeks 1-3: Prompt management system
- Weeks 4-6: Multi-persona implementation
- Weeks 7-9: Analytics dashboard
- Weeks 10-12: Canvas integration
- Weeks 13-15: Testing, documentation, EEF Symposium presentation

## Contributing

This is an active independent study project. The codebase will evolve significantly as features are developed and tested with real students and instructors.

For questions or collaboration inquiries, contact:
- **Student:** Kaitlyn Samuelian (kaitlyn.samuelian@colorado.edu)
- **Advisor:** Professor Hodgkinson (CU Boulder Aerospace Engineering)

## Acknowledgments

- Professor Hodgkinson - Faculty advisor
- CU Boulder Aerospace Engineering Department
- TACC (Texas Advanced Computing Center) - Authentication infrastructure
- Students and instructors participating in development and testing

---

*This project is part of an independent study at CU Boulder and is under active development.*
