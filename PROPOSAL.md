# Independent Study Proposal

## CHAT: Canvas-linked Human-AI Teaching Platform

---

**Student:** Kaitlyn Samuelian  
**Faculty Advisor:** Professor Hodgkinson  
**Department:** Aerospace Engineering  
**Institution:** University of Colorado Boulder  
**Credit Hours:** 1-3 credits (flexible based on scope)  
**Semester:** Spring 2026  
**Date:** October 2025

---

## I. Project Overview

### What is CHAT?

CHAT (Canvas-linked Human-AI Teaching) is an AI tutoring platform that gives instructors control over AI behavior while maintaining student privacy and integrating with Canvas LMS. Unlike generic AI chatbots, CHAT allows instructors to customize teaching approaches, enforce pedagogical methods, and analyze how students interact with AI tutors.

### Current State

A proof-of-concept already exists with:
- Flask web server with GPT integration
- OAuth2 authentication
- Neo4j database for student-class relationships
- JSON chat logging
- Docker deployment
- Basic Canvas integration

### Why This Matters

Current AI tutoring tools have critical limitations:
- No instructor control over AI responses
- Privacy concerns with student data on external servers
- No integration with existing course infrastructure
- Missing analytics on student learning patterns
- Generic one-size-fits-all approach

CHAT addresses these gaps while creating a research platform for studying AI-enhanced learning.

## II. Goals

### Development Goals

1. **Frontend & User Experience**
   - Modern, accessible chat interface
   - Student and instructor dashboards
   - Responsive design

2. **Prompt Management System**
   - Interface for instructors to create/edit prompts
   - Version control and testing
   - Organization and search

3. **Multi-Persona AI Tutors**
   - Different teaching styles (Socratic, Visual, Step-by-Step, Explainer)
   - Student choice of preferred persona
   - Analytics comparing persona effectiveness

4. **Analytics Dashboard**
   - View de-identified conversations
   - Usage metrics and patterns
   - Export capabilities for research

5. **Canvas Integration**
   - Student submission workflow
   - Assignment mapping
   - Instructor feedback tools

### Research Goals

1. Investigate how different AI teaching personalities affect learning
2. Study student interaction patterns with AI tutors
3. Understand instructor adoption barriers
4. Explore prompt engineering for educational contexts
5. Create a platform for ongoing educational AI research

## III. Learning Objectives

By completing this independent study, I will develop skills in:

**Technical Skills:**
- Full-stack web development (Flask, JavaScript, databases)
- AI integration and prompt engineering
- API integration (OpenAI, Canvas, OAuth2)
- Data visualization and analytics
- Docker and deployment

**Research Skills:**
- Educational technology study design
- User research and usability testing
- Quantitative and qualitative data analysis
- Academic presentation and writing

**Professional Skills:**
- Project management and self-direction
- Collaboration with faculty, instructors, and students
- Technical documentation
- Public presentation

## IV. Timeline (Flexible)

The project will follow a 15-week timeline with flexibility based on credit hours and what works best:

### Weeks 1-3: Foundation
- Prompt management system (CRUD, version control)
- Initial instructor interviews
- Literature review

### Weeks 4-6: Personas
- Implement multiple AI teaching personalities
- Persona selector interface
- Guardrails for different teaching approaches

### Weeks 7-9: Analytics
- Chat log browser
- Metrics dashboard and visualizations
- Pilot deployment with 1-2 courses

### Weeks 10-12: Integration
- Enhanced Canvas integration
- Assignment mapping
- Instructor feedback tools

### Weeks 13-15: Completion
- Usability testing
- Data analysis
- Documentation
- EEF Symposium presentation

## V. Expected Outcomes

### Deliverables

1. **Working Platform:** Deployed system serving real students
2. **Documentation:** Technical docs and user guides
3. **Research Findings:** Analysis of student-AI interactions and persona effectiveness
4. **Presentation:** EEF Symposium presentation with demos
5. **Code Repository:** Open-source codebase for future development

### Impact

- Provides instructors with AI tools they can actually control and trust
- Maintains student privacy through local data storage
- Creates research platform for educational AI studies
- Potentially deployable to other institutions
- Contributes to understanding of AI in education

## VI. Research Questions

1. **Do different AI teaching personalities affect student learning outcomes?**
2. **Do students naturally choose personas that match their learning styles?**
3. **What patterns emerge in student-AI interactions?**
4. **What barriers exist to instructor adoption of AI tutoring tools?**
5. **How can prompt engineering be made accessible to non-technical instructors?**

Data will be collected from actual student usage (with IRB approval as needed) and made available to educational researchers in de-identified form.

## VII. Evaluation Criteria

Success will be measured by:

### Development (40-60% depending on credit hours)
- Completion of planned features
- Code quality and documentation
- Successful deployment with real users
- Usability test results

### Research (30-40%)
- Study design and data collection
- Analysis of findings
- Quality of presentation and documentation

### Professional Skills (10-20%)
- Project management and meeting milestones
- Communication with advisor and stakeholders
- Adaptability and problem-solving

## VIII. Flexibility & Scope

The exact scope will be determined based on:
- Credit hours (1-3 credits)
- Technical challenges encountered
- Instructor and student availability for testing
- Research opportunities that emerge

Core features (prompt management, personas, basic analytics) are prioritized. Advanced features (RLHF, pseudo-student testing, advanced visualizations) are stretch goals.

## IX. Resources Needed

- **Development tools:** Personal laptop, API access (OpenAI, Canvas)
- **Infrastructure:** TACC authentication, potential CU hosting
- **Testing participants:** Instructors and students from pilot courses
- **Advisor time:** Regular meetings and guidance
- **IRB approval:** If required for research data collection

## X. Next Steps

Upon approval:
1. Finalize credit hours and exact scope
2. Submit IRB application if needed
3. Begin development with prompt management system
4. Identify pilot courses for testing
5. Set up regular advisor meetings

---

**Student Signature:** _________________________ **Date:** _____________

**Advisor Signature:** _________________________ **Date:** _____________

**Department Approval:** _______________________ **Date:** _____________
