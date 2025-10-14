# My Contributions to CHAT Platform

**Kaitlyn Samuelian - Independent Study (Spring 2026)**  
**CU Boulder Aerospace Engineering Department**  
**Advisor: Professor Hodgkinson**

---

## Overview

This document outlines my planned contributions to the CHAT platform as part of my independent study. The project combines software development with educational technology research.

**Note:** This is a living document. Plans may evolve based on what works, what doesn't, and what we learn along the way.

---

## Development Contributions

### 1. Frontend & User Interface

**Student Interface:**
- Modern chat interface with dark/light themes
- Responsive design (mobile, tablet, desktop)
- Accessibility features (keyboard navigation, screen readers)
- Persona selector to choose teaching style
- Chat history and message search
- Reflection submission interface

**Instructor Dashboard:**
- Canvas-style interface design
- Course and assignment overview
- Quick access to prompt editing and analytics
- Student activity monitoring

**Technical Approach:**
- HTML5/CSS3 with modern layout techniques
- JavaScript for interactivity
- Chart.js or Plotly.js for visualizations
- Accessible design following WCAG guidelines

### 2. Prompt Management System

**Core Features:**
- Create, edit, and delete prompts
- Markdown editor with preview
- Version control (automatic backups, rollback capability)
- Tag and organize prompts by course/assignment
- Test prompts before deploying to students
- Search and filter

**Why This Matters:**
Instructors need an easy way to customize AI behavior without being AI experts. This gives them full control over what their AI tutor says and how it teaches.

**Technical Approach:**
- Flask API endpoints for CRUD operations
- File-based storage (markdown with YAML metadata)
- Custom versioning system with timestamps
- Preview mode using actual AI models

### 3. Multi-Persona AI Tutors

**Four Teaching Personalities:**

1. **Socratic Tutor** - Asks guiding questions, never gives direct answers
2. **Visual Tutor** - Emphasizes diagrams, analogies, spatial thinking
3. **Step Solver** - Breaks problems into clear, numbered steps
4. **Explainer** - Provides detailed conceptual explanations

**Implementation:**
- Persona selector UI for students
- Different prompt templates for each persona
- Guardrails that enforce teaching approach (e.g., Socratic mode blocks direct answers)
- Track which persona students choose and use for analytics

**Research Component:**
Compare learning outcomes and student preferences across personas. Do students naturally choose what works best for them, or do they need guidance?

### 4. Analytics & Visualization

**Chat Log Browser:**
- View de-identified student conversations
- Filter by course, assignment, date, persona
- Search within conversations
- Export to CSV/JSON for research

**Metrics Dashboard:**
- Usage trends (chats per day/week, peak times)
- Persona comparison (which are most popular, effective)
- Common questions and topics
- Model usage statistics
- Interactive charts and graphs

**Why This Matters:**
Instructors need to understand how students are using AI. Researchers need data to study AI-enhanced learning.

### 5. Canvas Integration

**Student Features:**
- "Submit Chat Reflection" button in chat interface
- Automatic packaging of chat transcript + student reflection
- Submit directly to Canvas assignment
- Confirmation and tracking

**Instructor Features:**
- Assignment mapping (link Canvas assignments to CHAT prompts)
- View student reflections and chat summaries
- Provide feedback
- AI-generated summaries as private notes

**Technical Approach:**
- Canvas API integration (OAuth2, assignment submission)
- Automated grade passback
- Webhook listeners for enrollment sync

---

## Research Contributions

### Study Design

- Literature review on AI in education and prompt engineering
- Design studies to investigate persona effectiveness
- Plan data collection procedures
- Create surveys and interview protocols
- Obtain IRB approval if required

### Data Collection

**Quantitative:**
- Chat logs with timestamps, personas, models used
- Usage metrics (logins, session duration, message counts)
- Persona selection data
- Assignment performance (if available)

**Qualitative:**
- Student surveys on satisfaction and perceived learning
- Instructor interviews about adoption barriers
- Usability testing observations
- Student reflections on AI interactions

### Analysis

- Statistical analysis of persona effectiveness
- Text analysis of common student questions
- Thematic coding of interviews
- Comparison of learning outcomes across conditions
- Identification of interaction patterns

### Dissemination

- EEF Symposium presentation (15 minutes + Q&A)
- Research poster
- Final report documenting findings
- Potential conference paper or journal article
- Open-source repository with documentation

---

## Skills I'm Developing

### Technical Skills

**Full-Stack Development:**
- Flask backend development
- RESTful API design
- Frontend HTML/CSS/JavaScript
- Database design (Neo4j)
- Docker deployment

**AI Integration:**
- Working with OpenAI API and other AI models
- Prompt engineering for education
- Implementing guardrails and content filtering
- Comparing model performance

**Data & Analytics:**
- Data visualization with Chart.js/Plotly
- Processing and analyzing chat logs
- Statistical analysis
- Creating dashboards

### Research Skills

**Study Design:**
- Formulating research questions
- Mixed-methods research (quantitative + qualitative)
- Educational technology research
- Ethics and FERPA compliance

**Data Analysis:**
- Statistical analysis (comparing groups, correlations)
- Qualitative coding and thematic analysis
- Text mining and pattern identification

**Communication:**
- Academic writing
- Presenting to technical and non-technical audiences
- Creating effective visualizations
- Documentation for different audiences

### Professional Skills

**Project Management:**
- Breaking large projects into tasks
- Managing timeline and scope
- Adapting to challenges
- Self-directed work

**Collaboration:**
- Working with faculty advisor
- Gathering requirements from instructors
- User testing with students
- Engaging educational researchers

---

## Timeline & Milestones

### Weeks 1-3: Prompt Management
- ✅ CRUD interface functional
- ✅ Version control working
- ✅ Preview and testing capability

### Weeks 4-6: Personas
- ✅ Four personas implemented
- ✅ Persona selector UI
- ✅ Guardrails enforcing teaching approaches

### Weeks 7-9: Analytics
- ✅ Chat log browser
- ✅ Metrics dashboard
- ✅ Pilot deployment started

### Weeks 10-12: Canvas Integration
- ✅ Submission workflow
- ✅ Assignment mapping
- ✅ Instructor feedback tools

### Weeks 13-15: Completion
- ✅ Usability testing
- ✅ Data analysis
- ✅ Documentation complete
- ✅ EEF Symposium presentation

---

## Measuring Success

### Development Success
- All core features working and deployed
- Real students using the platform
- Positive usability test results
- Clean, documented code

### Research Success
- 100+ student participants
- 1000+ chat conversations logged
- Clear findings on persona effectiveness
- Insights into student interaction patterns

### Learning Success
- Mastery of full-stack development
- Understanding of educational research methods
- Growth in project management
- Strong portfolio project for future opportunities

---

## Flexibility

This plan is ambitious but flexible. If certain features prove too complex or time-consuming, priorities can shift. The core focus is:

1. **Must-have:** Prompt management + multi-persona system + basic analytics
2. **Should-have:** Canvas integration + comprehensive analytics
3. **Nice-to-have:** Advanced features (RLHF, pseudo-student testing)

The goal is to create something useful and learn a lot, not to perfectly execute an overly rigid plan.

---

## Contact

**Kaitlyn Samuelian**  
Email: kaitlyn.samuelian@colorado.edu  
Advisor: Professor Hodgkinson, CU Boulder Aerospace Engineering

---

*Last Updated: October 2025*
