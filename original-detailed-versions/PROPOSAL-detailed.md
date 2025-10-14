# Independent Study Proposal

## CHAT: Canvas-linked Human-AI Teaching Platform
### Development and Research in AI-Integrated Learning Systems

---

**Student:** Kaitlyn Samuelian  
**Faculty Advisor:** Professor Hodgkinson  
**Department:** Aerospace Engineering  
**Institution:** University of Colorado Boulder  
**Credit Hours:** 3 credits  
**Semester:** Spring 2026  
**Date:** October 2025

---

## I. Executive Summary

This independent study proposes the development and research of CHAT (Canvas-linked Human-AI Teaching), an AI-integrated learning platform that addresses critical gaps in current educational AI tools. The project combines substantial software engineering work with educational technology research, investigating how customizable AI tutors with different teaching personalities affect student learning outcomes while maintaining FERPA compliance and institutional control.

The platform will serve real students in courses across the university, with de-identified data accessible to educational researchers. This positions the work as both a practical development project and a research platform for studying human-AI interaction in educational contexts.

## II. Project Description

### Background and Motivation

The integration of AI chatbots into education has accelerated rapidly, yet current implementations suffer from several fundamental limitations:

1. **Lack of Pedagogical Control:** Generic AI tools (ChatGPT, Claude, etc.) provide inconsistent responses that may not align with instructor teaching methods or course-specific requirements.

2. **Privacy and Compliance Concerns:** Most AI platforms send student data to external servers, creating FERPA compliance issues and limiting institutional adoption.

3. **No Instructor Agency:** Educators cannot customize AI behavior, enforce specific teaching methodologies (e.g., Socratic method), or prevent AI from giving complete solutions.

4. **Absence of Learning Analytics:** Institutions have no systematic way to understand how students use AI tutors, what questions they ask, or whether AI assistance improves learning outcomes.

5. **Disconnection from LMS Infrastructure:** AI tools exist separately from Canvas and other learning management systems, creating friction in assignment workflows and credit attribution.

CHAT addresses these challenges by providing a comprehensive platform that gives instructors full control over AI tutor behavior, stores all data locally for FERPA compliance, integrates seamlessly with Canvas, and generates rich analytics for both instructors and researchers.

### Current State of the Project

A proof-of-concept version of CHAT already exists with the following implemented features:

- **Flask-based web server** serving a GPT-powered Socratic math helper
- **OAuth2 authentication** via Tapis/TACC for secure student login
- **Neo4j graph database** managing student-class relationships and enrollment
- **JSON-based chat logging** with persistent storage
- **Docker containerization** for deployment
- **Basic Canvas integration** including unique code generation for credit submission

This foundation provides a solid starting point for the substantial development and research work proposed in this independent study.

### Project Goals

#### Primary Development Goals

1. **Modern Frontend & User Experience**
   - Design an accessible, intuitive chat interface with dark/light themes
   - Create Canvas-style instructor dashboard
   - Implement responsive layouts for mobile, tablet, and desktop
   - Ensure WCAG 2.1 AA accessibility compliance

2. **Comprehensive Prompt Management System**
   - Full CRUD interface for creating, editing, and deleting prompt files
   - Version control with automatic backups and rollback capability
   - Preview and testing functionality before deployment
   - AI-assisted prompt generation tutorials
   - Organization system with tags and search

3. **Multi-Persona AI Tutor System**
   - Implement 4+ distinct AI teaching personalities:
     - **Socratic Tutor:** Question-based guidance, no direct answers
     - **Visual Tutor:** Emphasis on diagrams, analogies, visual thinking
     - **Step Solver:** Structured step-by-step problem solving
     - **Explainer:** Detailed conceptual explanations with examples
   - Student persona selector (choose preferred teaching style)
   - Guardrails middleware enforcing persona-specific behaviors
   - Assignment-level persona defaults set by instructors

4. **Analytics Dashboard & Chat Log Browser**
   - De-identified conversation viewer with filtering and search
   - Metrics dashboard (usage patterns, common questions, model statistics)
   - Interactive visualizations using Plotly.js or Chart.js
   - Persona effectiveness comparison analytics
   - CSV/JSON export for research purposes

5. **Enhanced Canvas Integration**
   - "Submit Chat Reflection" workflow for students
   - Automatic packaging of chat transcript + reflection
   - Instructor feedback panel
   - AI-generated chat summaries as private instructor notes
   - Assignment mapping linking Canvas assignments to CHAT prompts

6. **Testing, Documentation & Dissemination**
   - Usability testing with real students and instructors
   - Comprehensive technical documentation for future developers
   - User guides for instructors and students
   - EEF Symposium presentation with demos and visualizations

#### Primary Research Goals

1. **Investigate AI Persona Effectiveness in Learning**
   - Do students learn better with certain AI teaching personalities?
   - How do persona preferences correlate with student learning styles?
   - Which personas are most effective for different types of assignments?

2. **Study Prompt Engineering for Educational AI**
   - What prompt structures produce the most effective Socratic tutoring?
   - How do small changes in prompts affect student-AI interactions?
   - Can instructors without AI expertise create effective prompts?

3. **Explore Reinforcement Learning from Human Feedback (RLHF)**
   - Can an "overseer" AI analyze instructor corrections and automatically improve prompts?
   - How quickly can AI tutors adapt to instructor preferences?
   - What types of corrections are most valuable for prompt refinement?

4. **Analyze Patterns in Student-AI Interactions**
   - What questions do students most commonly ask?
   - When do students turn to AI tutors during the problem-solving process?
   - Are there predictable patterns that indicate student confusion?

5. **Evaluate AI Integration in Traditional LMS Environments**
   - What barriers exist to instructor adoption of AI tutoring tools?
   - How does CHAT integration affect student assignment submission behavior?
   - Does AI availability reduce office hours attendance or student-instructor interaction?

### Research Questions

This project will investigate the following research questions:

**RQ1:** How do different AI tutor personas (Socratic, Visual, Step Solver, Explainer) affect student learning outcomes, engagement, and satisfaction?

**RQ2:** Do students naturally gravitate toward specific AI personas based on their learning styles, and does matching persona to learning style improve performance?

**RQ3:** Can reinforcement learning from human feedback (RLHF) enable automatic prompt improvement when instructors correct AI responses?

**RQ4:** What patterns emerge in student-AI conversations that predict learning difficulties or misconceptions?

**RQ5:** How do instructors adapt their teaching practices when AI tutors are available, and what factors facilitate or hinder AI tool adoption?

## III. Learning Objectives and Outcomes

By completing this independent study, the student will:

### Technical Skills Development

1. **Full-Stack Web Development**
   - Design and implement responsive, accessible user interfaces
   - Build RESTful APIs with Flask
   - Manage complex application state
   - Integrate third-party APIs (OpenAI, Canvas, OAuth2)

2. **Database Design and Management**
   - Work with graph databases (Neo4j)
   - Design efficient data schemas for analytics
   - Implement data export and anonymization pipelines

3. **AI/ML Integration**
   - Interface with multiple AI models (GPT-4, Llama-3, Gemini)
   - Implement prompt engineering best practices
   - Design guardrails and content filtering systems
   - Explore RLHF concepts and implementation

4. **Data Visualization**
   - Create interactive charts and dashboards
   - Design effective information presentation for different audiences
   - Implement real-time analytics updates

5. **Software Engineering Best Practices**
   - Version control with Git
   - Test-driven development
   - Documentation and code maintainability
   - Containerization and deployment

### Research Skills Development

1. **Educational Technology Research**
   - Design user studies for educational software
   - Collect and analyze qualitative feedback
   - Understand FERPA and research ethics in educational contexts

2. **Data Analysis**
   - Analyze large datasets of student-AI interactions
   - Identify patterns and trends in educational data
   - Statistical comparison of learning outcomes across conditions

3. **Human-Computer Interaction**
   - Conduct usability testing
   - Iterate designs based on user feedback
   - Apply HCI principles to educational interfaces

4. **Academic Communication**
   - Write technical documentation for diverse audiences
   - Create compelling presentations for symposiums
   - Collaborate with educational researchers

### Domain Knowledge Development

1. **Educational Theory**
   - Understand constructivist learning principles
   - Apply Socratic teaching methods to AI design
   - Learn theories of learning styles and personalization

2. **Learning Management Systems**
   - Understand Canvas architecture and APIs
   - Design integrations that enhance existing workflows
   - Navigate institutional educational technology requirements

3. **AI Ethics and Privacy**
   - Implement FERPA-compliant data storage
   - Design privacy-preserving analytics
   - Consider ethical implications of AI in education

## IV. Methodology

### Development Methodology

The project will follow an **Agile development approach** with 2-week sprints:

1. **Sprint Planning:** Define specific features and success criteria
2. **Development:** Implement features with continuous integration
3. **Testing:** Unit tests, integration tests, and user testing
4. **Review:** Demo to advisor and gather feedback
5. **Retrospective:** Reflect on process and adjust plans

### Research Methodology

**Phase 1: Formative Research (Weeks 1-6)**
- Literature review of AI in education
- Competitive analysis of existing AI tutoring platforms
- Initial user interviews with instructors and students
- Persona development and prompt template creation

**Phase 2: Development & Pilot Testing (Weeks 7-12)**
- Iterative development of features
- Small-scale pilot with 1-2 courses
- Collect preliminary usage data and feedback
- Refine personas and prompts based on real interactions

**Phase 3: Evaluation & Analysis (Weeks 13-15)**
- Larger deployment with multiple courses
- Formal usability testing sessions
- Statistical analysis of persona effectiveness
- Qualitative analysis of instructor and student feedback
- Synthesis of findings for EEF Symposium presentation

### Data Collection

The following data will be collected (with IRB approval if required):

- **Chat transcripts** (de-identified) - all student-AI conversations
- **Usage metrics** - login times, session duration, message counts
- **Persona selection data** - which personas students choose
- **Assignment performance** - grades on assignments using AI tutors
- **User surveys** - satisfaction, perceived usefulness, learning gains
- **Instructor interviews** - adoption barriers, feature requests, pedagogical insights

### Collaboration with Educational Researchers

The project will actively engage educational researchers by:
- Providing de-identified database access
- Offering consultation on research question design
- Supporting additional studies using the platform
- Co-authoring potential publications

## V. Timeline and Milestones

### 15-Week Semester Schedule

#### **Weeks 1-3: Foundation & Prompt Management**

**Development:**
- Define prompt file schema (.md format with metadata)
- Implement CRUD interface for prompt creation/editing/deletion
- Build preview functionality to test prompts before publication
- Create version control system with automatic backups
- Implement rollback capability to previous prompt versions

**Research:**
- Literature review on prompt engineering in education
- Analysis of existing AI tutoring systems
- Initial instructor interviews about teaching methodologies

**Deliverables:**
- Functional prompt management system
- Literature review summary document
- Interview findings report

---

#### **Weeks 4-6: Persona System Development**

**Development:**
- Design and implement persona selector UI for students
- Create persona-specific prompt templates (Socratic, Visual, Step Solver, Explainer)
- Develop guardrail middleware for enforcing persona behaviors
- Implement persona_id persistence in chat logs
- Build instructor interface for assigning default personas to assignments

**Research:**
- Design persona effectiveness study
- Create pre-deployment survey for learning style assessment
- Develop rubric for evaluating chat quality by persona

**Deliverables:**
- Functional multi-persona system
- Study design document
- Survey instruments

---

#### **Weeks 7-9: Analytics & Visualization**

**Development:**
- Build chat log browser with filtering and search
- Create metrics dashboard (usage stats, common questions, model comparisons)
- Implement persona comparison analytics
- Develop interactive visualizations (Plotly.js/Chart.js)
- Add CSV/JSON export functionality for researchers

**Research:**
- Begin pilot deployment with 1-2 courses
- Collect initial usage data
- Analyze early patterns in student interactions
- Conduct mid-point usability testing

**Deliverables:**
- Functional analytics dashboard
- Pilot deployment report
- Preliminary data analysis

---

#### **Weeks 10-12: Canvas Integration & Enhancement**

**Development:**
- Implement assignment mapping system
- Build "Submit Chat Reflection" workflow for students
- Create instructor feedback panel
- Develop AI-generated summary feature
- Enhance authentication and authorization

**Research:**
- Expand deployment to additional courses
- Collect instructor feedback on dashboard usability
- Analyze student reflection quality
- Compare learning outcomes across personas (preliminary)

**Deliverables:**
- Full Canvas integration
- Expanded deployment
- Instructor feedback report

---

#### **Weeks 13-15: Testing, Documentation & Dissemination**

**Development:**
- Comprehensive usability testing with students and instructors
- Bug fixes and polish based on feedback
- Complete technical documentation
- Write user guides and tutorials

**Research:**
- Final data collection and analysis
- Statistical analysis of persona effectiveness
- Qualitative synthesis of interviews and surveys
- Draft research paper or conference abstract

**Dissemination:**
- Create EEF Symposium presentation
- Develop demo videos and walkthroughs
- Design research poster
- Present findings to stakeholders

**Deliverables:**
- Final tested and documented platform
- EEF Symposium presentation
- Research findings report
- Comprehensive project documentation

---

### Key Milestones

| Week | Milestone | Success Criteria |
|------|-----------|------------------|
| 3 | Prompt Management Complete | Instructors can create, edit, test, and version prompts |
| 6 | Persona System Functional | Students can select from 4 personas with distinct behaviors |
| 9 | Analytics Dashboard Live | Instructors can view usage data and export chat logs |
| 12 | Canvas Integration Complete | Students can submit reflections; instructors receive summaries |
| 15 | Project Completion & Presentation | EEF Symposium presentation delivered; all documentation complete |

## VI. Expected Contributions to the Field

This independent study will contribute to educational technology in several significant ways:

### 1. Practical Tool for Educators

CHAT will provide a working, deployable platform that:
- Gives instructors unprecedented control over AI tutor behavior
- Maintains FERPA compliance through local data storage
- Integrates seamlessly with existing LMS infrastructure
- Requires no AI expertise from instructors

### 2. Research Platform

The platform will enable research on:
- AI persona effectiveness in learning contexts
- Prompt engineering best practices for education
- Student interaction patterns with AI tutors
- Instructor adoption factors for AI tools

### 3. Open-Source Educational Infrastructure

By open-sourcing the project:
- Other institutions can adopt and adapt CHAT
- Researchers gain access to a proven platform for educational AI studies
- The broader community can contribute improvements and new features

### 4. Methodological Innovations

The project explores:
- **RLHF for education:** Adapting reinforcement learning from human feedback to automatically improve teaching prompts
- **Persona-based AI tutoring:** Moving beyond one-size-fits-all AI to personalized teaching styles
- **Privacy-preserving analytics:** Demonstrating how to gain insights while maintaining student privacy

### 5. Student Learning Outcomes

Ultimately, this work aims to:
- Improve student access to personalized tutoring
- Reduce barriers to help-seeking behavior
- Support diverse learning styles
- Enhance rather than replace human instruction

## VII. Evaluation Criteria

The independent study will be evaluated based on:

### Development Deliverables (50%)

- **Code Quality:** Well-structured, documented, tested code
- **Feature Completeness:** All planned features implemented and functional
- **Usability:** Intuitive interfaces validated through user testing
- **Technical Documentation:** Comprehensive guides for future developers
- **Deployment:** Working production instance serving real students

### Research Deliverables (30%)

- **Study Design:** Rigorous methodology for investigating research questions
- **Data Collection:** Comprehensive, ethical data collection from real users
- **Analysis:** Thoughtful analysis of both quantitative and qualitative data
- **Findings:** Meaningful insights into AI personas and educational effectiveness
- **Presentation:** Clear communication of results at EEF Symposium

### Professional Skills (20%)

- **Project Management:** Meeting milestones and managing scope
- **Communication:** Regular advisor meetings and progress updates
- **Collaboration:** Engaging with instructors, students, and researchers
- **Adaptability:** Responding to feedback and changing requirements
- **Reflection:** Thoughtful consideration of challenges and learning

### Specific Evaluation Metrics

**For Development:**
- Number of features completed vs. planned
- Code test coverage percentage
- Number of users successfully onboarded
- Usability testing scores
- System uptime and performance

**For Research:**
- Number of student participants
- Completeness of data collection
- Depth of analysis
- Quality of presentation materials
- Contribution to field (citations, adoptions, collaborations)

## VIII. Resources Required

### Provided by CU Boulder

- **Computing Infrastructure:** TACC/Tapis authentication, potential server hosting
- **Software Licenses:** Canvas API access, university software licenses
- **Research Support:** IRB approval process, potential research participant compensation
- **Advisor Time:** Regular meetings with Professor Hodgkinson

### Student-Provided

- **Development Environment:** Personal laptop, development tools
- **API Access:** OpenAI API credits for GPT models (potentially covered by research account)
- **Time Commitment:** Approximately 135-150 hours over 15 weeks (9-10 hours/week for 3 credits)

### Potential External Resources

- **Educational Researcher Collaboration:** Partnerships with CU School of Education faculty
- **User Testing Participants:** Students and instructors from courses using CHAT
- **Open-Source Community:** Potential contributors to the GitHub repository

## IX. Risk Assessment and Mitigation

### Technical Risks

**Risk 1: API Cost Overruns**
- *Mitigation:* Implement rate limiting, use caching, support local models (Llama-3)

**Risk 2: Canvas API Changes**
- *Mitigation:* Abstract Canvas integration behind service layer, monitor Canvas changelog

**Risk 3: Scalability Issues**
- *Mitigation:* Load testing, Docker orchestration, database query optimization

### Research Risks

**Risk 1: Low User Adoption**
- *Mitigation:* Partner with enthusiastic instructors, provide incentives, emphasize value proposition

**Risk 2: Insufficient Data for Analysis**
- *Mitigation:* Start data collection early, plan for multiple courses, have backup qualitative methods

**Risk 3: IRB Approval Delays**
- *Mitigation:* Submit IRB early, plan development work during approval period, de-identify all data

### Project Management Risks

**Risk 1: Scope Creep**
- *Mitigation:* Clear milestone definitions, prioritize core features, defer stretch goals to post-study

**Risk 2: Technical Challenges Taking Longer Than Expected**
- *Mitigation:* Build in buffer time, have backup plans for complex features, regular advisor check-ins

**Risk 3: Student Illness or Unexpected Events**
- *Mitigation:* Document progress continuously, automate where possible, maintain communication with advisor

## X. Post-Independent Study Plans

This independent study lays the foundation for ongoing work:

### Summer 2026
- Implement advanced features (RLHF system, pseudo-student testing)
- Expand deployment to additional courses and potentially other universities
- Submit research findings to educational technology conferences (e.g., EDM, LAK, AIED)

### Fall 2026
- Potential second independent study for advanced research components
- Explore grant opportunities (NSF IUSE, Google CS Education, etc.)
- Develop mobile app version

### Long-Term Vision
- Multi-institution deployment
- Publication in educational technology journals
- Contribution to open-source educational AI ecosystem
- Potential startup opportunity for commercialization

## XI. References and Related Work

### AI in Education

1. Kulik, J. A., & Fletcher, J. D. (2016). Effectiveness of intelligent tutoring systems: A meta-analytic review. *Review of Educational Research, 86*(1), 42-78.

2. Luckin, R., & Cukurova, M. (2019). Designing educational technologies in the age of AI: A learning sciences-driven approach. *British Journal of Educational Technology, 50*(6), 2824-2838.

3. Holstein, K., McLaren, B. M., & Aleven, V. (2019). Co-designing a real-time classroom orchestration tool to support teacher-AI complementarity. *Journal of Learning Analytics, 6*(2), 27-52.

### Prompt Engineering

4. Reynolds, L., & McDonell, K. (2021). Prompt programming for large language models: Beyond the few-shot paradigm. *Extended Abstracts of CHI 2021*.

5. White, J., et al. (2023). A prompt pattern catalog to enhance prompt engineering with ChatGPT. *arXiv preprint arXiv:2302.11382*.

### Learning Styles and Personalization

6. Pashler, H., McDaniel, M., Rohrer, D., & Bjork, R. (2008). Learning styles: Concepts and evidence. *Psychological Science in the Public Interest, 9*(3), 105-119.

7. VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist, 46*(4), 197-221.

### FERPA and Privacy in Educational Technology

8. U.S. Department of Education. (2018). *Protecting Student Privacy While Using Online Educational Services: Requirements and Best Practices*. Privacy Technical Assistance Center.

9. Reidenberg, J. R., & Schaub, F. (2018). Achieving big data privacy in education. *Theory and Research in Education, 16*(3), 263-279.

### Learning Analytics

10. Siemens, G., & Long, P. (2011). Penetrating the fog: Analytics in learning and education. *Educause Review, 46*(5), 30-40.

11. Ferguson, R. (2012). Learning analytics: Drivers, developments and challenges. *International Journal of Technology Enhanced Learning, 4*(5/6), 304-317.

## XII. Conclusion

This independent study represents a unique opportunity to combine substantial software engineering work with meaningful educational technology research. The CHAT platform addresses real problems faced by instructors and students while creating a foundation for ongoing research into AI-enhanced learning.

The project scope is ambitious but achievable given the existing proof-of-concept and the 3-credit time commitment. The work will result in:

- A deployable, open-source platform serving real students
- Rich data enabling research on AI persona effectiveness
- Professional-quality documentation and presentation materials
- Contributions to the educational technology field
- Significant skill development in full-stack development, AI integration, and educational research

Most importantly, CHAT has the potential to improve learning outcomes for students while giving instructors the tools they need to thoughtfully integrate AI into their teaching practice.

I am excited to undertake this work under Professor Hodgkinson's guidance and look forward to presenting the results at the EEF Symposium and beyond.

---

**Student Signature:** _________________________ **Date:** _____________

**Advisor Signature:** _________________________ **Date:** _____________

**Department Approval:** _______________________ **Date:** _____________

