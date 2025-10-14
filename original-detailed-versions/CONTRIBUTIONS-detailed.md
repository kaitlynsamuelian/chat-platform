# Project Contributions

## Kaitlyn Samuelian - Independent Study Developer & Researcher

This document outlines my specific contributions to the CHAT platform as part of my 3-credit independent study with Professor Hodgkinson at CU Boulder's Aerospace Engineering Department.

---

## Table of Contents

- [Overview](#overview)
- [Development Contributions](#development-contributions)
- [Research Contributions](#research-contributions)
- [Technical Skills Developed](#technical-skills-developed)
- [Research Skills Developed](#research-skills-developed)
- [Professional Development](#professional-development)
- [Timeline & Milestones](#timeline--milestones)
- [Measuring Success](#measuring-success)

---

## Overview

My work on CHAT spans both software engineering and educational technology research. While the project began with a proof-of-concept, my independent study contributions focus on transforming it into a production-ready platform with rich research capabilities.

**Total Time Commitment:** 135-150 hours (9-10 hours/week × 15 weeks)  
**Credit Hours:** 3 credits  
**Semester:** Spring 2026

**Core Focus Areas:**
1. **Frontend & User Experience** - Creating accessible, intuitive interfaces
2. **Prompt Management System** - Empowering instructors with full control
3. **Multi-Persona AI Tutors** - Enabling personalized teaching styles
4. **Analytics & Visualization** - Providing actionable insights
5. **Canvas Integration** - Seamless LMS workflow
6. **Research & Evaluation** - Studying AI effectiveness in education

---

## Development Contributions

### 1. Frontend Development & User Experience

#### Student Interface

**Chat Interface Design**
- Modern, responsive chat UI supporting mobile, tablet, and desktop
- Dark mode and light mode themes with user preference persistence
- Real-time typing indicators for AI responses
- Message history with infinite scroll and search
- Markdown rendering for formatted AI responses (equations, code blocks, lists)
- Accessibility features: keyboard navigation, screen reader support, WCAG 2.1 AA compliance

**Student Dashboard**
- Course and assignment list with status indicators (incomplete, in-progress, submitted)
- Quick access to recent chats
- Persona selector with preview descriptions
- Progress tracking visualization
- Help and tutorial system

**Reflection Submission Workflow**
- Chat summary generation before submission
- Reflection text editor with word count
- Preview before submitting to Canvas
- Submission confirmation and status tracking

#### Instructor Interface

**Canvas-Style Dashboard**
- Course management interface matching Canvas design patterns
- Overview of student activity and engagement metrics
- Quick access to frequently used features
- Responsive sidebar navigation
- Notification system for important events

**Prompt Management Interface**
- Clean editor with syntax highlighting for markdown
- Side-by-side preview pane
- Tag and category organization
- Search and filter functionality
- Bulk operations (duplicate, archive, delete)

**Analytics Dashboard**
- Interactive charts showing usage trends
- Filterable data views (by course, assignment, date range, persona)
- Export controls for CSV/JSON
- Comparison tools for persona effectiveness
- Real-time updates as new data arrives

**Technical Implementation:**
- **HTML5/CSS3** for semantic, accessible markup
- **Vanilla JavaScript** with modern ES6+ features (potentially React in future iterations)
- **CSS Grid and Flexbox** for responsive layouts
- **CSS Custom Properties** for theming
- **Fetch API** for asynchronous server communication
- **Chart.js or Plotly.js** for data visualization
- **Local Storage API** for user preference persistence

---

### 2. Prompt Management System

The prompt management system is the core instructor-facing feature, enabling full control over AI tutor behavior without requiring AI expertise.

#### CRUD Operations

**Create Prompts**
- Template-based prompt creation (start from Socratic, Visual, etc. templates)
- Guided wizard for first-time users
- AI-assisted prompt generation (using ChatGPT to help write prompts)
- Metadata fields: title, description, persona type, target course, assignment
- Tag system for organization (e.g., "calculus," "beginner-friendly," "exam-mode")

**Read/View Prompts**
- List view with sorting and filtering
- Detailed view showing full prompt content and metadata
- Version history viewer with diff comparison
- Usage statistics (how many students have used this prompt)

**Update Prompts**
- In-browser markdown editor with live preview
- Auto-save drafts to prevent data loss
- Change notes field to document what was modified
- Preview with test AI before publishing to students

**Delete Prompts**
- Soft delete (archive) rather than permanent deletion
- Safety checks: warn if prompt is currently assigned to active assignments
- Bulk archive for cleaning up old prompts

#### Version Control

**Automatic Backups**
- Every save creates a timestamped backup
- Backups stored in `/data/prompts/backups/` with git-like naming
- Metadata tracking: who changed it, when, and why (change notes)

**Rollback Capability**
- Browse previous versions in a timeline view
- Preview old version before restoring
- One-click rollback to any previous version
- Rollback creates a new version (no data loss)

**Diff Viewer**
- Side-by-side comparison of versions
- Highlighted additions/deletions
- Jump to next/previous change

#### Testing & Preview

**Preview Mode**
- Test prompts with simulated student questions
- Try different AI models (GPT-4, GPT-3.5, Llama-3, etc.)
- See how guardrails affect responses
- Save test conversations for instructor review

**Pseudo-Student Testing** (Stretch Goal)
- AI-generated student profiles (struggling learner, advanced student, visual thinker)
- Automated testing of prompts with different student types
- Generate sample conversations before deploying to real students
- Identify edge cases and potential issues

#### AI-Assisted Prompt Creation

**Tutorial System**
- Step-by-step guide for using ChatGPT to generate prompts
- Best practices for educational prompt engineering
- Examples of effective vs. ineffective prompts
- Common pitfalls and how to avoid them

**Template Library**
- Pre-built templates for common scenarios:
  - Socratic questioning for problem-solving
  - Visual/spatial explanations
  - Step-by-step solution guidance
  - Conceptual explanation
  - Exam proctor mode (restricted hints)
  - Homework helper mode (more guidance)

**Technical Implementation:**
- **Backend:** Flask routes for CRUD operations (`/api/prompts/`)
- **Database:** File-based storage (markdown files with YAML frontmatter for metadata)
- **Version Control:** Custom versioning system using timestamped copies
- **Editor:** CodeMirror or Monaco Editor for syntax highlighting
- **Markdown Processing:** Python-Markdown with extensions for code blocks, math

---

### 3. Multi-Persona AI Tutor System

The persona system allows students to choose teaching styles that match their learning preferences while giving instructors control over pedagogical approaches.

#### Persona Definitions

**1. Socratic Tutor**
- **Philosophy:** Guide through questions, never give direct answers
- **Behavior:** Responds to student questions with clarifying questions
- **Guardrails:** Block any response that directly solves the problem
- **Best For:** Developing critical thinking, preparing for exams
- **Example Interaction:**
  - Student: "What's the derivative of x²?"
  - Socratic: "What does the derivative represent? What rule applies to polynomial functions?"

**2. Visual Tutor**
- **Philosophy:** Emphasize diagrams, analogies, and spatial reasoning
- **Behavior:** Describe visual representations, suggest drawing diagrams
- **Guardrails:** Encourage visualization, prompt for sketches
- **Best For:** Visual learners, geometry, physics, systems thinking
- **Example Interaction:**
  - Student: "I don't understand how pointers work"
  - Visual: "Imagine a house. The house is the data, and a pointer is the house's address. When you have the address, you can find the house..."

**3. Step Solver**
- **Philosophy:** Break problems into discrete, manageable steps
- **Behavior:** Provide structured, numbered steps with clear progression
- **Guardrails:** Enforce step-by-step format, prevent jumping ahead
- **Best For:** Complex multi-step problems, algorithms, procedures
- **Example Interaction:**
  - Student: "How do I solve this integral?"
  - Step Solver: "Let's break it into steps: Step 1: Identify the integration technique needed..."

**4. Explainer**
- **Philosophy:** Provide detailed conceptual explanations with examples
- **Behavior:** Offer thorough explanations, multiple examples, connections to prior knowledge
- **Guardrails:** Ensure comprehensiveness, require checking understanding
- **Best For:** Learning new concepts, building foundational knowledge
- **Example Interaction:**
  - Student: "What is recursion?"
  - Explainer: "Recursion is when a function calls itself. Think of it like looking in a mirror between two mirrors..."

#### Implementation

**Student Persona Selector**
- Displayed when starting a new chat or assignment
- Visual cards showing each persona with:
  - Icon/illustration
  - Name and tagline
  - Description of teaching style
  - "Best for" recommendations
- Persistent across sessions (remembers last choice)
- Can switch personas mid-conversation (starts new thread)

**Instructor Persona Assignment**
- Set default persona per assignment
- Allow or restrict student choice
- Configure guardrail strictness
- A/B testing mode: randomly assign personas for research

**Guardrails Middleware**

The guardrails system sits between student input and AI model, enforcing persona-specific behaviors:

```python
class PersonaGuardrails:
    def filter_response(self, response, persona_type):
        if persona_type == "socratic":
            # Ensure response ends with question
            # Block direct answers to computational problems
            # Encourage deeper thinking
        elif persona_type == "visual":
            # Encourage diagram descriptions
            # Suggest drawing or sketching
            # Use spatial language
        # ... etc
```

**Persona-Specific Prompts**

Each persona has:
- **Base personality prompt:** Defines teaching philosophy and tone
- **Assignment-specific content:** Problem context, learning objectives
- **Guardrail rules:** Specific instructions for filtering responses
- **Example conversations:** Few-shot examples of good persona behavior

**Technical Implementation:**
- **Persona data:** JSON configuration files in `/data/personas/`
- **Middleware:** Python decorators that wrap AI API calls
- **Prompt composition:** Concatenate base personality + assignment content + guardrail rules
- **Logging:** Track persona_id in every chat message for analytics
- **UI Components:** Reusable persona selector component

---

### 4. Analytics Dashboard & Chat Log Browser

Comprehensive analytics provide instructors with insights into student learning and enable researchers to study AI tutoring effectiveness.

#### Chat Log Browser

**Features:**
- **De-identified view:** Student names replaced with anonymous IDs
- **Conversation list:** Chronological list of all chats with metadata (course, assignment, persona, date, message count)
- **Detailed view:** Full transcript of student-AI conversation
- **Search functionality:** Full-text search across all conversations
- **Filtering:**
  - By course and assignment
  - By persona type
  - By date range
  - By message count (short vs. long conversations)
  - By AI model used
- **Export:** Download individual or bulk conversations as CSV/JSON

**Privacy Considerations:**
- All student identifying information removed
- Anonymized student IDs consistent within the database for longitudinal analysis
- Instructors can only access their own course data
- Research exports require additional approval

#### Metrics Dashboard

**Usage Statistics:**
- Total chats per day/week/month
- Active users over time
- Peak usage times (heatmap by hour of day / day of week)
- Average chat duration
- Average messages per conversation
- Conversations by assignment

**Persona Analytics:**
- Distribution of persona selections
- Average conversation length by persona
- Student satisfaction by persona (from surveys)
- Learning outcomes by persona (if grade data available)
- Persona switching patterns

**Content Analysis:**
- Most common student questions (keyword extraction)
- Topic clusters (unsupervised learning on chat content)
- Sentiment analysis (student frustration vs. understanding)
- Question types (factual, procedural, conceptual)

**Model Comparisons:**
- Usage by AI model (GPT-4 vs. GPT-3.5 vs. Llama-3, etc.)
- Response time by model
- Response quality (if rated by students or instructors)
- Cost per conversation by model

#### Interactive Visualizations

**Chart Types:**
- **Line charts:** Usage trends over time
- **Bar charts:** Comparisons across personas, courses, assignments
- **Heatmaps:** Activity patterns by time of day/week
- **Pie charts:** Distribution of personas, models
- **Scatter plots:** Correlation between usage and grades
- **Box plots:** Distribution of conversation lengths, message counts

**Interactivity:**
- Hover for detailed information
- Click to filter/drill down
- Zoom and pan on time-series data
- Toggle data series on/off
- Export charts as PNG for presentations

#### Export & Research Access

**For Instructors:**
- Export filtered chat logs as CSV/JSON
- Export analytics data for further analysis
- Generate reports for course improvement

**For Researchers:**
- De-identified bulk data exports
- API access for automated data collection
- Custom query interface for specific research questions
- Collaboration portal for requesting data access

**Technical Implementation:**
- **Backend:** Flask routes for analytics queries (`/api/analytics/`)
- **Data Processing:** Pandas for data manipulation and aggregation
- **Visualization:** Chart.js or Plotly.js for interactive charts
- **Database Queries:** Optimized Neo4j and JSON queries for performance
- **Caching:** Redis or in-memory caching for frequently accessed analytics
- **Export:** Generate CSV/JSON using Python's built-in libraries

---

### 5. Canvas Integration

Seamless integration with Canvas ensures CHAT fits naturally into existing course workflows.

#### Student Features

**Submit Chat Reflection Workflow:**

1. **Chat Completion:** Student finishes conversation with AI tutor
2. **Summary Generation:** System automatically generates summary of key topics discussed
3. **Reflection Prompt:** Student writes reflection on what they learned, how AI helped, remaining questions
4. **Preview:** Student reviews chat summary + reflection before submitting
5. **Submit to Canvas:** One-click submission to the associated Canvas assignment
6. **Confirmation:** Student receives confirmation with submission timestamp and unique code

**Technical Flow:**
```
[CHAT Platform] → Package transcript + reflection
                ↓
          [Canvas API] → Submit to assignment
                ↓
        [Grade Passback] → Confirm submission
                ↓
  [Student Dashboard] → Show completion status
```

**Implementation Details:**
- Canvas API endpoint: `POST /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions`
- Submission format: PDF or HTML with formatted chat transcript + reflection
- Unique submission code: Hash of (student_id + timestamp + chat_id) for verification

#### Instructor Features

**Feedback Panel:**
- View student reflection and chat summary
- Write rubric-based feedback
- Assign grades (or confirm participation credit)
- Post feedback directly to Canvas

**AI-Generated Summaries:**
- System generates instructor-facing summary of chat:
  - Topics student asked about
  - Concepts student seemed to struggle with
  - Quality of engagement
  - Suggested areas for follow-up
- Posted as private instructor notes in Canvas (invisible to students)

**Assignment Mapping:**
- Link Canvas assignments to CHAT prompts
- Set which persona is default for each assignment
- Configure guardrail strictness
- Set submission requirements (minimum messages, reflection length)

#### Automation Features

**Automatic Credit:**
- Students automatically receive participation credit upon submission
- Configurable: instructor can require manual grading instead

**Due Date Synchronization:**
- Pull Canvas assignment due dates into CHAT
- Display countdown timers in student interface
- Send reminders before deadlines

**Enrollment Sync:**
- Automatically sync Canvas course rosters with CHAT database
- Add/drop students reflected in real-time
- Handle multiple course sections

**Technical Implementation:**
- **Canvas API Authentication:** OAuth2 flow for instructor authorization
- **API Wrapper:** Python library for Canvas API (canvasapi or custom)
- **Webhook Listeners:** Receive Canvas events (enrollment changes, assignment updates)
- **Background Jobs:** Celery for asynchronous submission processing
- **Error Handling:** Retry logic for failed API calls, user-friendly error messages

---

### 6. Testing & Documentation

#### Usability Testing

**Student Testing Sessions:**
- Recruit 10-15 students from pilot courses
- Conduct moderated usability tests (think-aloud protocol)
- Test scenarios:
  - Finding and starting an assignment
  - Selecting a persona
  - Having a productive chat
  - Submitting reflection to Canvas
- Collect feedback via surveys (SUS - System Usability Scale)
- Iterate on design based on findings

**Instructor Testing Sessions:**
- Recruit 3-5 instructors from different departments
- Test prompt creation and editing workflow
- Test analytics dashboard comprehension
- Test Canvas integration workflow
- Conduct semi-structured interviews about adoption barriers

**Accessibility Testing:**
- Test with screen readers (NVDA, JAWS, VoiceOver)
- Test keyboard-only navigation
- Verify color contrast meets WCAG 2.1 AA standards
- Test with users who have disabilities (if possible)

#### Documentation

**Developer Documentation:**
- **Architecture Overview:** System design, component interactions
- **API Reference:** All endpoints with request/response examples
- **Database Schema:** Neo4j graph structure, JSON log format
- **Setup Guide:** Step-by-step instructions for local development
- **Deployment Guide:** Docker, production considerations, environment variables
- **Contributing Guide:** How to contribute code, PR process, coding standards

**User Documentation:**

*For Students:*
- Getting started guide
- How to choose a persona
- Tips for productive AI conversations
- Submitting reflections
- FAQ and troubleshooting

*For Instructors:*
- Platform overview and philosophy
- Creating effective prompts (with examples)
- Understanding personas and when to use them
- Interpreting analytics
- Canvas integration setup
- Best practices for AI-enhanced courses

**Research Documentation:**
- Study design and methodology
- Data dictionary (variables, formats, meaning)
- Privacy and ethics protocols
- How to request data access
- Example research questions and analyses

#### Presentation Materials

**EEF Symposium Presentation:**
- 15-minute talk with slides
- Project motivation and goals
- Demo of key features (video or live)
- Research findings (persona effectiveness, user feedback)
- Future directions
- Q&A preparation

**Supporting Materials:**
- Research poster
- Demo videos (student view, instructor view)
- Screenshots and UI mockups
- Handouts with QR codes to documentation

**Technical Implementation:**
- **Documentation Platform:** Markdown files + static site generator (MkDocs, Docsify)
- **Video Recording:** Screen capture with voiceover (OBS Studio)
- **Poster Design:** Canva or Adobe Illustrator
- **Presentation Slides:** Google Slides or PowerPoint with embedded videos

---

### 7. Advanced Features (Stretch Goals)

These features are aspirational goals that may be implemented if time permits or in future work.

#### Pseudo-Student Chatbot Testing

**Concept:** Create AI-generated "students" with different profiles to test prompts before deploying to real students.

**Student Profiles:**
- **Struggling Learner:** Asks basic questions, needs lots of guidance, gets confused easily
- **Advanced Student:** Asks sophisticated questions, makes connections, challenges AI
- **Visual Thinker:** Responds well to spatial descriptions, asks for diagrams
- **Concrete Thinker:** Needs step-by-step procedures, struggles with abstract concepts
- **Procedural Learner:** Wants algorithms and formulas, less interested in theory

**Workflow:**
1. Instructor creates new prompt
2. System generates conversations with each pseudo-student profile
3. Instructor reviews conversations to identify issues
4. Instructor refines prompt based on edge cases discovered
5. Repeat until satisfied

**Benefits:**
- Test prompts without risking student confusion
- Discover edge cases and failure modes
- Iterate rapidly on prompt design
- Build confidence before deployment

#### RLHF System (Reinforcement Learning from Human Feedback)

**Concept:** An "overseer" AI analyzes instructor corrections and automatically refines prompts.

**Workflow:**
1. Student chats with AI tutor
2. AI gives a response
3. Instructor reviews response and thinks it's not ideal
4. Instructor provides correction: "The AI should have asked about X first" or "This is too much information"
5. Overseer AI analyzes:
   - Original prompt
   - Student question
   - AI response
   - Instructor correction
6. Overseer generates prompt modification
7. Modified prompt suggested to instructor for review
8. If approved, becomes new prompt version

**Challenges:**
- Requires sophisticated meta-AI system
- Need good UI for instructor corrections
- Balancing automated changes with instructor control
- Evaluating whether automated changes actually improve outcomes

**Research Potential:**
- Study how quickly prompts improve with RLHF
- Compare human-refined vs. AI-refined prompts
- Understand what types of corrections are most valuable

#### Chat Replay Controls

**Concept:** VCR-style interface to step through conversations turn-by-turn.

**Features:**
- Timeline slider showing entire conversation
- Play button: auto-advance through messages
- Step forward/backward buttons
- Speed control (2x, 1x, 0.5x)
- Pause at specific points
- Add annotations and comments at any point
- Side-by-side comparison of two conversations

**Use Cases:**
- Instructor review of student conversations
- Usability testing: watching how students interact
- Presentations and demos
- Research analysis of conversation patterns
- Training instructors on how students use AI

#### C-to-Assembly Visualizer

**Concept:** Interactive tool showing how C code translates to assembly, with stack and register visualization.

**Features:**
- Side-by-side C and assembly code
- Step through execution line-by-line
- Visual stack with push/pop animations
- Register values updating in real-time
- Memory diagrams
- Explanation of each assembly instruction

**Use Cases:**
- Computer Architecture courses
- Systems programming
- Understanding compiler optimizations
- Debugging and performance tuning

**Integration with CHAT:**
- AI tutor can reference visualizations: "Look at the stack in the visualizer as we step through this function call"
- Students can ask questions about specific lines while viewing visualization
- Deepens understanding of low-level concepts

---

## Research Contributions

### 1. Study Design & Methodology

**Formative Research:**
- Conduct literature review on AI in education, prompt engineering, and learning styles
- Analyze competitive landscape of AI tutoring platforms
- Interview instructors about pedagogical needs and AI concerns
- Survey students about prior AI usage and preferences

**Pilot Study:**
- Deploy to 1-2 courses in initial weeks
- Collect preliminary data on usage patterns
- Conduct usability testing sessions
- Refine features based on early feedback

**Full Deployment Study:**
- Expand to 5-10 courses across different disciplines
- Collect comprehensive usage data (chat logs, persona selections, timestamps)
- Administer pre/post surveys on learning outcomes and satisfaction
- Conduct interviews with instructors and students
- Analyze grade data (if permitted and controlled for confounds)

### 2. Data Collection & Management

**Quantitative Data:**
- Chat transcripts (all messages, timestamps, persona used, model used)
- Usage metrics (logins, session duration, message counts)
- Persona selection data (which personas students choose, switching behavior)
- Assignment performance (grades on assignments using CHAT)
- System performance (response times, error rates)

**Qualitative Data:**
- Open-ended survey responses
- Interview transcripts
- Instructor feedback and feature requests
- Student reflections on learning

**Data Management:**
- All data stored locally in compliance with FERPA
- De-identification procedures for research use
- Secure backups and version control
- IRB approval for human subjects research (if required)
- Data retention and deletion policies

### 3. Analysis & Findings

**Research Question 1: Persona Effectiveness**
- **Analysis:** Compare learning outcomes (grades, survey responses) across personas
- **Methods:** ANOVA for grade comparisons, chi-square for preference distributions
- **Expected Findings:** Some personas will be more effective for certain types of learners or assignments

**Research Question 2: Learning Style Matching**
- **Analysis:** Correlate learning style assessments with persona preferences and outcomes
- **Methods:** Correlation analysis, cluster analysis
- **Expected Findings:** Students may gravitate toward personas that match their learning style, though optimal may differ

**Research Question 3: RLHF Feasibility** (if implemented)
- **Analysis:** Track prompt evolution over time, measure improvement metrics
- **Methods:** Content analysis of prompts, expert rating of prompt quality, student outcome comparison
- **Expected Findings:** RLHF can improve prompts, but human oversight remains important

**Research Question 4: Interaction Patterns**
- **Analysis:** Text mining of chat logs for common questions, confusion patterns
- **Methods:** Topic modeling (LDA), keyword extraction, sentiment analysis
- **Expected Findings:** Identifiable patterns in when students seek help and what they struggle with

**Research Question 5: Instructor Adoption**
- **Analysis:** Qualitative analysis of interviews, observation of actual usage
- **Methods:** Thematic coding, case studies
- **Expected Findings:** Key barriers include time investment, AI skepticism, and lack of technical comfort

### 4. Dissemination

**EEF Symposium (End of Semester):**
- 15-minute presentation with Q&A
- Research poster
- Live demos or recorded videos
- Handouts with project information

**Written Outputs:**
- Independent study final report
- Research paper draft for educational technology conference (EDM, LAK, AIED)
- Blog posts for broader audience
- Technical documentation for developers

**Potential Future Publications:**
- Conference papers at EDM (Educational Data Mining), LAK (Learning Analytics & Knowledge), or AIED (Artificial Intelligence in Education)
- Journal articles in *Journal of Educational Technology & Society* or *Computers & Education*
- Practitioner articles in *EDUCAUSE Review*

---

## Technical Skills Developed

### Full-Stack Web Development

**Frontend:**
- Semantic HTML5 and modern CSS3 (Grid, Flexbox, Custom Properties)
- Vanilla JavaScript and ES6+ features (async/await, destructuring, modules)
- Responsive design and mobile-first development
- Accessibility best practices (WCAG 2.1 AA)
- Interactive data visualization (Chart.js or Plotly.js)
- State management in complex interfaces

**Backend:**
- Flask application architecture (blueprints, application factory pattern)
- RESTful API design and implementation
- Request/response handling and validation
- Session management and authentication
- Background job processing (Celery)
- Error handling and logging

**Databases:**
- Neo4j graph database (nodes, relationships, Cypher queries)
- JSON file-based storage for unstructured data
- Database design for analytics and performance
- Data migration and backup strategies

**APIs & Integration:**
- OpenAI API (GPT models)
- Canvas LMS API (OAuth2, assignment submission, grade passback)
- Tapis/TACC OAuth2 authentication
- API rate limiting and error handling
- Webhook listeners for real-time updates

**DevOps & Deployment:**
- Docker containerization
- Docker Compose for multi-container applications
- Environment variable management
- Production deployment best practices
- Monitoring and logging

### AI & Machine Learning

**AI Model Integration:**
- Interfacing with multiple AI models (GPT-4, GPT-3.5, Llama-3, Gemini)
- Prompt engineering for educational contexts
- Designing guardrails and content filtering
- Managing context windows and token limits
- Comparing model performance and cost

**Advanced AI Concepts:**
- Reinforcement Learning from Human Feedback (RLHF) theory and implementation
- Text generation parameters (temperature, top_p, frequency penalty)
- Few-shot learning and in-context learning
- Adversarial prompt testing

**NLP & Text Analysis:**
- Topic modeling and keyword extraction
- Sentiment analysis
- Text classification
- Similarity metrics for version comparison

### Data Science & Visualization

**Data Processing:**
- Pandas for data manipulation and aggregation
- Data cleaning and normalization
- Feature extraction from chat logs
- Statistical analysis (means, distributions, correlations)

**Visualization:**
- Interactive charts and graphs
- Dashboard design and information architecture
- Visual storytelling with data
- Choosing appropriate chart types for different data

**Analytics:**
- Descriptive statistics
- Comparative analysis (across personas, courses, time periods)
- Trend identification
- Anomaly detection

### Software Engineering Best Practices

**Version Control:**
- Git branching strategies
- Meaningful commit messages
- Pull request workflow
- Code review practices

**Testing:**
- Unit testing with pytest
- Integration testing
- End-to-end testing
- Test-driven development

**Code Quality:**
- Writing clean, readable, maintainable code
- Following PEP 8 style guidelines
- Refactoring and technical debt management
- Documentation and inline comments

**Project Management:**
- Breaking large projects into manageable tasks
- Estimating time and managing scope
- Iterative development (Agile/Scrum principles)
- Balancing features, quality, and deadlines

---

## Research Skills Developed

### Study Design

- Formulating research questions
- Designing mixed-methods studies (quantitative + qualitative)
- Identifying appropriate methodologies
- Planning data collection procedures
- Considering ethical implications and IRB requirements

### Data Collection

- Creating effective surveys (avoiding bias, clear questions)
- Conducting semi-structured interviews
- Facilitating usability testing sessions
- Observing users without interfering
- Recording and organizing qualitative data

### Data Analysis

**Quantitative:**
- Descriptive statistics (mean, median, standard deviation)
- Inferential statistics (t-tests, ANOVA, chi-square)
- Correlation and regression analysis
- Statistical significance and effect sizes
- Using statistical software (Python scipy/statsmodels, or R)

**Qualitative:**
- Thematic coding of interview transcripts
- Pattern identification in open-ended responses
- Case study methodology
- Triangulation across data sources

### Academic Writing & Communication

- Writing literature reviews
- Structuring research papers (intro, methods, results, discussion)
- Creating effective visualizations for research findings
- Presenting to academic audiences
- Responding to questions and critiques

### Educational Technology Expertise

- Understanding learning theories (constructivism, connectivism)
- Applying pedagogical principles to technology design
- Evaluating educational effectiveness
- Understanding FERPA and student privacy laws
- Navigating institutional educational technology policies

---

## Professional Development

### Collaboration & Communication

**Working with Faculty:**
- Regular advisor meetings with clear agendas
- Progress updates and managing expectations
- Asking for help when stuck
- Receiving and incorporating feedback

**Working with Instructors:**
- Understanding instructor needs and pain points
- Translating technical features into pedagogical benefits
- Training instructors on new tools
- Providing ongoing support and troubleshooting

**Working with Students:**
- Understanding the student perspective
- Designing for diverse technical skill levels
- Responding to feedback and feature requests
- Creating user-friendly tutorials and help resources

**Working with Researchers:**
- Facilitating data access while protecting privacy
- Understanding research needs and constraints
- Collaborating on study design
- Co-authoring potential publications

### Project Management

**Planning & Organization:**
- Creating realistic timelines and milestones
- Breaking large goals into actionable tasks
- Prioritizing features based on impact and feasibility
- Managing scope creep and adjusting plans

**Self-Management:**
- Time management across coursework and independent study
- Maintaining motivation on long-term projects
- Balancing development and research tasks
- Documenting progress for accountability

**Problem-Solving:**
- Debugging complex technical issues
- Finding creative solutions to design challenges
- Researching technologies and best practices
- Knowing when to ask for help vs. persevere independently

### Professional Skills

**Technical Communication:**
- Writing clear documentation for different audiences
- Creating effective code comments
- Explaining technical concepts to non-technical stakeholders
- Presenting demos and walkthroughs

**Public Speaking:**
- Presenting at EEF Symposium
- Explaining research findings to diverse audiences
- Handling Q&A sessions
- Creating engaging presentation slides

**Portfolio Development:**
- Building a substantial, public-facing project for resume
- Documenting contributions and impact
- Showcasing both technical and research skills
- Creating compelling demo materials

---

## Timeline & Milestones

### Phase 1: Foundation (Weeks 1-3)

**Development:**
- ✅ Prompt management CRUD interface
- ✅ Version control with backups
- ✅ Preview and testing functionality

**Research:**
- ✅ Literature review
- ✅ Competitive analysis
- ✅ Initial instructor interviews

**Skills Focus:**
- Flask API development
- File system operations
- Markdown processing

---

### Phase 2: Personas (Weeks 4-6)

**Development:**
- ✅ Persona selector UI
- ✅ Four persona types implemented
- ✅ Guardrails middleware
- ✅ Persona persistence in logs

**Research:**
- ✅ Persona effectiveness study design
- ✅ Learning style survey creation
- ✅ Chat quality rubric development

**Skills Focus:**
- UI/UX design
- Middleware architecture
- Study design

---

### Phase 3: Analytics (Weeks 7-9)

**Development:**
- ✅ Chat log browser
- ✅ Metrics dashboard
- ✅ Interactive visualizations
- ✅ CSV/JSON export

**Research:**
- ✅ Pilot deployment (1-2 courses)
- ✅ Initial data collection
- ✅ Usability testing sessions

**Skills Focus:**
- Data visualization
- Database queries and optimization
- Usability testing

---

### Phase 4: Canvas Integration (Weeks 10-12)

**Development:**
- ✅ Reflection submission workflow
- ✅ Assignment mapping
- ✅ Instructor feedback panel
- ✅ AI-generated summaries

**Research:**
- ✅ Expanded deployment (5-10 courses)
- ✅ Comprehensive data collection
- ✅ Instructor interviews

**Skills Focus:**
- API integration
- OAuth2 authentication
- Qualitative data collection

---

### Phase 5: Completion (Weeks 13-15)

**Development:**
- ✅ Bug fixes and polish
- ✅ Comprehensive testing
- ✅ Documentation completion

**Research:**
- ✅ Data analysis (quantitative and qualitative)
- ✅ Findings synthesis
- ✅ EEF Symposium preparation

**Deliverables:**
- 📊 EEF Symposium presentation
- 📄 Final project report
- 📚 Complete documentation
- 🎓 Deployed platform serving real students

**Skills Focus:**
- Data analysis
- Academic writing
- Public presentation

---

## Measuring Success

### Development Success Metrics

**Functionality:**
- ✅ All core features implemented and working
- ✅ <5% error rate in production
- ✅ <2 second average response time
- ✅ 99% uptime during deployment period

**Usability:**
- ✅ System Usability Scale (SUS) score >70 (above average)
- ✅ <10 minutes for students to complete first assignment
- ✅ <5 support tickets per 100 users
- ✅ Positive feedback from usability testing

**Code Quality:**
- ✅ >80% test coverage
- ✅ Zero critical security vulnerabilities
- ✅ All code reviewed and documented
- ✅ Follows PEP 8 style guidelines

### Research Success Metrics

**Participation:**
- ✅ >100 students using platform
- ✅ >1000 chat conversations logged
- ✅ >5 instructors adopting platform
- ✅ Survey response rate >50%

**Data Quality:**
- ✅ Complete data collection with <5% missing values
- ✅ Successful de-identification of all student data
- ✅ IRB approval obtained (if required)
- ✅ Data ready for research use

**Findings:**
- ✅ Clear answers to at least 3 of 5 research questions
- ✅ Statistically significant results where applicable
- ✅ Rich qualitative insights from interviews
- ✅ Actionable recommendations for instructors

### Dissemination Success Metrics

**Presentation:**
- ✅ EEF Symposium presentation delivered
- ✅ Positive audience feedback and engagement
- ✅ Effective demos and visualizations
- ✅ Q&A handled confidently

**Documentation:**
- ✅ Complete developer documentation
- ✅ Comprehensive user guides
- ✅ Research methodology documented
- ✅ Future developers can onboard independently

**Impact:**
- ✅ Platform continues to be used after independent study ends
- ✅ Other instructors express interest in adoption
- ✅ Potential for conference paper submission
- ✅ Contributions to open-source educational technology

### Personal Success Metrics

**Learning:**
- ✅ Mastery of new technical skills (Flask, Neo4j, AI APIs)
- ✅ Understanding of educational research methods
- ✅ Ability to design and conduct user studies
- ✅ Growth in project management and self-direction

**Portfolio:**
- ✅ Substantial project for resume and job applications
- ✅ Live demo-able application
- ✅ Clear documentation of contributions
- ✅ Strong recommendation from advisor

**Career Preparation:**
- ✅ Experience with full development lifecycle
- ✅ Practice presenting technical work
- ✅ Understanding of academic research processes
- ✅ Network connections with faculty and researchers

---

## Conclusion

This independent study represents a substantial commitment of development and research work. Through CHAT, I will gain deep experience in full-stack web development, AI integration, educational technology, and research methodology. The project addresses real problems in education while creating a platform for ongoing research.

Most importantly, CHAT has the potential to improve learning outcomes for students and empower instructors with thoughtful AI integration tools. I'm excited to take on this challenge and contribute to the future of AI-enhanced education.

---

**Student:** Kaitlyn Samuelian  
**Advisor:** Professor Hodgkinson  
**Department:** Aerospace Engineering, CU Boulder  
**Project Repository:** https://github.com/yourusername/chat-platform

*Last Updated: October 2025*

