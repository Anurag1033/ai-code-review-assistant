# 🚀 AI Code Review Assistant

An AI-powered code review platform that automatically analyzes source code, identifies bugs, suggests improvements, and stores review history using Large Language Models (LLMs).

---

# 📖 Overview

I built this project to automate the software code review process using Generative AI.

Developers can submit source code through REST APIs, and the system leverages Google's Gemini model through LangChain to generate detailed code reviews, including bug detection, security concerns, performance recommendations, and overall code quality ratings.

All generated reviews are persisted in PostgreSQL, allowing developers to track and revisit previous reviews.

---

# 🏗️ System Architecture

```text
                    +-------------------+
                    |      Developer    |
                    +---------+---------+
                              |
                              | HTTP Request
                              v
                    +-------------------+
                    |      FastAPI      |
                    |     REST APIs     |
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    |   Review Service  |
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    |    LangChain      |
                    | Prompt Pipeline   |
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    |    Gemini API     |
                    | Code Analysis AI  |
                    +---------+---------+
                              |
                              | Review Result
                              v
                    +-------------------+
                    |    PostgreSQL     |
                    | Review Storage    |
                    +-------------------+
```

---

# 🛠️ Tech Stack

### Backend

* Python 3.12
* FastAPI
* Pydantic

### AI & LLM

* Google Gemini API
* LangChain
* Prompt Engineering

### Database

* PostgreSQL
* SQLAlchemy ORM

### Development Tools

* Git
* GitHub
* Virtual Environment (venv)

---

# 🧩 Core Components

## FastAPI Application

**Responsibility:**

* Exposes REST APIs
* Handles incoming code review requests
* Returns AI-generated responses

### Available Endpoints

```http
GET /
POST /review
GET /reviews
GET /review/{id}
```

---

## LangChain Review Pipeline

**Responsibility:**

* Creates structured prompts
* Sends code to Gemini
* Receives and processes AI-generated reviews

### Flow

```text
Source Code
    ↓
Prompt Template
    ↓
LangChain
    ↓
Gemini
    ↓
Review Response
```

---

## PostgreSQL Database

**Responsibility:**

Stores:

* Submitted source code
* Generated AI reviews
* Review history

### Review Table

```text
reviews
│
├── id
├── code
└── review
```

---

# 🚦 Getting Started

## Prerequisites

Install:

* Python 3.12+
* PostgreSQL
* Git

---

## 1. Clone Repository

```bash
git clone <repository-url>

cd ai-code-review-assistant
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key

DATABASE_URL=postgresql://postgres:password@localhost:5432/code_review_db
```

---

## 5. Create Database Tables

```bash
python create_tables.py
```

---

## 6. Run Application

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# 🧪 Testing the Application

### Review Code

```http
POST /review
```

Request:

```json
{
  "code": "def add(a,b): return a+b"
}
```

Response:

```json
{
  "review": "Detailed AI-generated code review..."
}
```

---

### View Review History

```http
GET /reviews
```

---

### Get Review By ID

```http
GET /review/1
```

---

# 📂 Repository Structure

```text
ai-code-review-assistant/

├── app/
│   ├── chains/
│   │   └── reviewer_chain.py
│   │
│   ├── db/
│   │   ├── database.py
│   │   └── models.py
│   │
│   ├── prompts/
│   │   └── review_prompt.py
│   │
│   ├── services/
│   │   └── reviewer.py
│   │
│   └── main.py
│
├── .env
├── create_tables.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 👨‍💻 Author

**Anurag Sharma**
