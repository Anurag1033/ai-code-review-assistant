# 🚀 AI Code Review Assistant

An AI-powered code review platform that automatically analyzes source code using Google's Gemini LLM, generates detailed code reviews, detects programming languages, stores review history in PostgreSQL, and runs seamlessly inside Docker containers.

---

# 📖 Overview

AI Code Review Assistant automates the software code review process using Generative AI.

Developers can submit source code through REST APIs, and the system leverages Google's Gemini model via LangChain to generate detailed code reviews, including:

* Bug Detection
* Security Analysis
* Performance Suggestions
* Code Quality Improvements
* Overall Rating

All generated reviews are stored in PostgreSQL for future reference, filtering, analytics, and review history tracking.

---

# ✨ Features

### AI-Powered Reviews

* Automated code analysis using Gemini
* Detailed review reports
* Security and performance recommendations

### Review Management

* Save reviews in PostgreSQL
* Retrieve review history
* Get review by ID
* Delete reviews

### Advanced APIs

* Pagination support
* Review filtering by programming language
* Review statistics dashboard

### Containerized Deployment

* Dockerized application
* Docker Compose support
* One-command deployment

---

# 🏗️ System Architecture

```text
                    +-------------------+
                    |     Developer     |
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
                    |   Gemini 2.5      |
                    |  Code Analysis    |
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    |    PostgreSQL     |
                    | Review Storage    |
                    +-------------------+
```

---

# 🛠️ Tech Stack

## Backend

* Python 3.12
* FastAPI
* Pydantic

## AI & LLM

* Google Gemini 2.5 Flash
* LangChain
* Prompt Engineering

## Database

* PostgreSQL
* SQLAlchemy ORM

## DevOps

* Docker
* Docker Compose

## Development Tools

* Git
* GitHub

---

# 📡 API Endpoints

## Home

```http
GET /
```

---

## Generate Review

```http
POST /review
```

Request:

```json
{
  "code": "def add(a,b): return a+b"
}
```

---

## Get Paginated Reviews

```http
GET /reviews?page=1&limit=5
```

---

## Get Reviews By Language

```http
GET /reviews/Python
```

---

## Get Single Review

```http
GET /review/1
```

---

## Delete Review

```http
DELETE /review/1
```

---

## Review Statistics

```http
GET /stats
```

Example Response:

```json
{
  "total_reviews": 15,
  "python_reviews": 10,
  "java_reviews": 2,
  "javascript_reviews": 2,
  "cpp_reviews": 1
}
```

---

# 🗄️ Database Schema

## reviews

```text
reviews
│
├── id
├── code
├── language
├── review
└── created_at
```

---

# 🚀 Getting Started

## Prerequisites

Install:

* Python 3.12+
* Docker Desktop
* Git

---

## Clone Repository

```bash
git clone https://github.com/your-username/ai-code-review-assistant.git

cd ai-code-review-assistant
```

---

## Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key

DATABASE_URL=postgresql://postgres:password@db:5432/reviews
```

---

# 🐳 Run With Docker

Build and start containers:

```bash
docker compose up --build
```

Application:

```text
http://localhost:8000
```

Swagger Docs:

```text
http://localhost:8000/docs
```

---

# 📂 Project Structure

```text
ai-code-review-assistant/

├── app/
│
├── chains/
│   └── reviewer_chain.py
│
├── db/
│   ├── database.py
│   ├── models.py
│   └── init_db.py
│
├── prompts/
│   └── review_prompt.py
│
├── schema/
│   └── review.py
│
├── services/
│   ├── reviewer.py
│   └── language_detector.py
│
├── main.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .gitignore
├── README.md
└── .env
```

---

# 🔄 Review Workflow

```text
User submits source code
            ↓
FastAPI receives request
            ↓
LangChain creates prompt
            ↓
Gemini analyzes code
            ↓
Review generated
            ↓
Review saved to PostgreSQL
            ↓
Response returned to user
```

#

---

# 👨‍💻 Author

**Anurag Sharma**

