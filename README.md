AIview – AI-Based Interview Simulation System

AIview is an AI-powered interview preparation platform that simulates real interview environments and provides **automated, personalized feedback** on user responses.

It integrates resume-based question generation, answer evaluation, and performance analytics into a single workflow.

📌 Overview

Traditional interview preparation lacks structured evaluation and actionable feedback. AIview addresses this by:

* Generating **personalized interview questions** from resumes
* Simulating a **real interview flow** (technical + behavioral)
* Providing **AI-driven evaluation with scores and feedback**
* Offering **performance tracking via dashboard**

The system is designed as a **local prototype**, focusing on usability and AI integration rather than large-scale deployment.

✨ Key Features

* 📄 Resume-based question generation
* 🤖 AI-powered answer evaluation (0–10 scoring)
* 🎤 Text + Speech interaction support
* 📊 Performance dashboard & interview history
* 🧠 Structured feedback (strengths, weaknesses, suggestions)
* 📚 Learning module (tips, frameworks, examples)

🏗️ System Architecture

The system follows a modular architecture:

* **Frontend**: UI for interaction (resume upload, Q&A, results)
* **Backend (Flask)**: Handles logic, interview flow, API calls
* **AI Model (Gemini API)**: Generates questions + evaluates answers
* **Database (SQLAlchemy)**: Stores sessions, responses, results

👉 The architecture diagram (page 6 of the report) shows:

* Data flow between frontend → backend → AI → database
* Sequential processing from resume upload to feedback generation 

🔄 Workflow

1. Upload resume
2. Resume parsing (skills, education, experience extraction)
3. AI generates structured interview questions
4. User answers questions (text/voice)
5. AI evaluates responses
6. Results stored in database
7. Dashboard displays performance insights



🛠️ Tech Stack

| Layer          | Technology Used         |
| -------------- | ----------------------- |
| Backend        | Python, Flask           |
| Frontend       | HTML, CSS, JavaScript   |
| AI Engine      | Gemini API              |
| Database       | SQLAlchemy              |
| Resume Parsing | pdfplumber, python-docx |

---

## 📂 Project Structure (Suggested)

```
AIview/
│── app.py
│── actions.py / backend modules
│── templates/
│── static/
│── database/
│── utils/
│── requirements.txt
│── README.md
```

*(Adjust based on your actual repo structure)*

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/aiview.git
cd aiview
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the application

```bash
python app.py
```

---

## 📊 Evaluation Output

The system generates:

* ✅ Score (0–10 scale)
* 💪 Strengths
* ⚠️ Weaknesses
* 🧠 Reasoning
* 📈 Improvement suggestions

---

## ⚠️ Limitations

* Depends on external AI API (latency & availability issues)
* AI evaluation may show **inconsistencies**
* No human-level contextual understanding
* Not production-ready (prototype only) 

---

## 🔮 Future Improvements

* Fine-tuned or local AI models
* Multi-language support
* Improved UI/UX
* Integration with real hiring systems
* Better evaluation consistency

---

## 🧠 Ethical Considerations

* Potential bias in AI evaluation
* Privacy concerns with resume data
* AI feedback should be treated as **guidance, not absolute judgment** 

---

## 📸 Screenshots

Include screenshots from your report:

* Home page
* Interview interface
* Dashboard
* Results

*(You can upload images to GitHub and link them here)*

---

## 👨‍💻 Author

**Shashwat Devan**
B.Tech – Computer Science and Communication Engineering
KIIT University

---

## 📜 License

This project is for academic and prototype purposes. Add a license (MIT recommended) if needed.

---

## ⭐ Contribution

This is a prototype project, but suggestions and improvements are welcome!

---

If you want, I can:

* tailor this to **exact GitHub folder structure (your repo)**
* add **badges (build, license, Python version)**
* or make it **resume/project portfolio optimized** (for recruiters)
