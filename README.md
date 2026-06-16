# ResumeIntelligenceSystem# 🤖 AI Resume Intelligence Platform

An AI-powered recruitment and resume screening platform that automates candidate evaluation using ATS scoring, semantic matching, FAISS vector search, and LLM-powered recruiter insights. Built with Streamlit, Sentence Transformers, SQLite, and Groq LLMs.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://resumeintelligencesystem-ibqcqv74msreb3iyfvb9wq.streamlit.app/)
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://resumeintelligencesystem-ibqcqv74msreb3iyfvb9wq.streamlit.app/)

---

## 🚀 Live Demo

🔗 **Try the live application here**

https://resumeintelligencesystem-ibqcqv74msreb3iyfvb9wq.streamlit.app/

Upload resumes → Paste a Job Description → Rank Candidates → Generate AI Insights.

---

## ⚙️ How It Works

```text
Resume Upload (PDF / ZIP)
            ↓
Resume Parsing (PyPDF2)
            ↓
Skill Extraction
            ↓
ATS Matching Engine
            ↓
Semantic Similarity Matching
(Sentence Transformers)
            ↓
Final Candidate Ranking
            ↓
AI Recruiter Assistant (Groq)
      ├── Resume Summary
      ├── Recruiter Feedback
      ├── Job Fit Analysis
      ├── Resume Chat
      └── Candidate Comparison
            ↓
Recruiter Dashboard
```

---

## 🛠️ Tech Stack

| Layer            | Technology            |
| ---------------- | --------------------- |
| Frontend         | Streamlit             |
| LLM              | Groq (Llama 3.3 70B)  |
| Embeddings       | Sentence Transformers |
| Vector Search    | FAISS                 |
| Database         | SQLite                |
| Visualization    | Plotly                |
| PDF Processing   | PyPDF2                |
| Machine Learning | Scikit-Learn          |
| Reporting        | ReportLab             |

---

## ✨ Features

### 📄 Resume Processing

* Upload multiple PDF resumes
* ZIP resume upload support
* Automatic resume text extraction
* Resume skill extraction

### 🎯 Candidate Evaluation

* ATS score calculation
* Semantic resume-job matching
* Final candidate scoring
* Automatic candidate ranking

### 🤖 AI Recruiter Assistant

* AI-generated resume summaries
* Recruiter feedback generation
* Missing skill identification
* Job fit analysis
* Resume Q&A chatbot
* AI candidate comparison

### 🔍 Candidate Recommendation Engine

* FAISS-powered vector search
* Semantic candidate retrieval
* Skill-based recommendations

### 📊 Recruiter Dashboard

* Candidate analytics
* Ranking visualization
* Search stored candidates
* Performance metrics

### 📑 Report Generation

* Candidate PDF reports
* CSV ranking export
* Recruiter insights reports

### 🔐 Authentication

* Login system
* Session management
* Demo recruiter access

---

## 🏗️ Architecture

```text
Streamlit Frontend
        ↓
Resume Processing Layer
        ↓
ATS + Semantic Matching Engine
        ↓
FAISS Vector Store
        ↓
Groq AI Services
    ├── Summary Generator
    ├── Feedback Generator
    ├── Job Fit Analyzer
    ├── Resume Chat
    └── Candidate Comparator
        ↓
SQLite Database
```

---

## 📁 Project Structure

```text
ResumeIntelligenceSystem/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
│   └── db.py
│
├── src/
│   ├── auth.py
│   ├── parser.py
│   ├── skills.py
│   ├── ats.py
│   ├── matcher.py
│   ├── recruiter.py
│   ├── ranking.py
│   ├── summary.py
│   ├── feedback.py
│   ├── job_fit.py
│   ├── comparison.py
│   ├── chat.py
│   ├── embeddings.py
│   ├── faiss_store.py
│   ├── recommendation.py
│   ├── report_generator.py
│   └── zip_processor.py
│
├── tests/
└── .streamlit/
    └── config.toml
```

---

## 🔧 Local Setup & Installation

### 1. Clone Repository

```bash
git clone https://github.com/varun0852/ResumeIntelligenceSystem.git

cd ResumeIntelligenceSystem
```

### 2. Create Virtual Environment

```bash
python -m venv venv

venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create .env File

```env
GROQ_API_KEY=your_groq_api_key
```

### 5. Run Application

```bash
streamlit run app.py
```

---

## ☁️ Deployment

| Service       | Platform                  |
| ------------- | ------------------------- |
| Application   | Streamlit Community Cloud |
| Database      | SQLite                    |
| AI Models     | Groq                      |
| Vector Search | FAISS                     |

### Live URL

https://resumeintelligencesystem-ibqcqv74msreb3iyfvb9wq.streamlit.app/

---

## 🔮 Future Improvements

* Multi-user recruiter accounts
* OCR support for scanned resumes
* AI-generated interview questions
* Email candidate shortlists
* PostgreSQL integration
* Advanced recruiter analytics
* Cloud vector database support
* LinkedIn profile analysis

---

## 👤 Author

**Varun** — AI/ML Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/varun-a87781274/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/varun0852)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:diwakarvarun752@gmail.com)

---

⭐ If you found this project useful, consider starring the repository.
