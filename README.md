# AI Quiz Generator Project

This project generates quiz questions with LangChain and presents them in an interactive quiz app plus a teacher dashboard.

## Files in This Repo

- `script.py` — main Python entry point for quiz generation.
- `quizapp.html` — interactive quiz application for students.
- `teacherdashboard.html` — teacher dashboard for viewing progress data.
- `quiz_data.json` — generated quiz questions and answers.
- `analytics.json` — aggregated performance analytics.
- `student_improvement.json` — student progress over time.

## Features

- Generate beginner, intermediate, and advanced quiz questions.
- Create answers and explanations for each question.
- Display the quiz in a browser-based HTML app.
- Track student performance over time in a dashboard.
- Load dashboard data from JSON files.
- Export merged dashboard data as JSON or CSV.

## Requirements

Install the required Python packages:

```bash
pip install langchain langchain-community langchain-google-genai pandas
```

You also need a Google Gemini API key.

## API Key Setup

### Google Colab
- Use Colab secrets.
- Add `GEMINI_API_KEY`.
- Enable notebook access.

### Local Jupyter or VS Code
- Set an environment variable, or use a `.env` file.

Example:

```bash
export GEMINI_API_KEY="your_key_here"
```

## How It Works

### 1. Python generation
`script.py` uses LangChain components to generate quiz questions, answers, and explanations, then saves them to `quiz_data.json`.

### 2. Quiz app
`quizapp.html` lets students answer the generated questions in the browser and view instant results.

### 3. Teacher dashboard
`teacherdashboard.html` shows student summaries, charts, quiz overview, and performance trends.

## Example JSON Structures

### quiz_data.json
```json
{
  "quiz": [
    {
      "id": 1,
      "difficulty": "beginner",
      "question": "What is photosynthesis?",
      "answer": "The process plants use to convert light energy into chemical energy",
      "explanation": "Plants convert light, water, and carbon dioxide into glucose and oxygen."
    }
  ]
}
```

### analytics.json
```json
{
  "total_students": 5,
  "total_attempts": 9,
  "average_score": 64.4,
  "best_score": 100,
  "worst_score": 20,
  "average_time_taken": 8.1,
  "students_by_performance": {
    "excellent (90-100%)": 2,
    "good (70-89%)": 2,
    "fair (50-69%)": 2,
    "needs improvement (<50%)": 3
  },
  "difficulty_breakdown": {
    "beginner": {"correct": 16, "total": 18, "percentage": 88.9},
    "intermediate": {"correct": 8, "total": 18, "percentage": 44.4},
    "advanced": {"correct": 3, "total": 9, "percentage": 33.3}
  }
}
```

### student_improvement.json
```json
[
  {
    "student_name": "Emma Johnson",
    "dates": ["2026-06-10", "2026-06-15", "2026-06-20"],
    "scores": 
  }
]
```

## Usage

### Run the generator
Execute `script.py` to create or refresh `quiz_data.json`.

### Open the quiz app
Open `quizapp.html` in your browser.

### Open the teacher dashboard
Open `teacherdashboard.html` in your browser.

## Suggested Folder Layout

```text
project/
├── script.py
├── quizapp.html
├── teacherdashboard.html
├── README.md
├── quiz_data.json
├── analytics.json
└── student_improvement.json
```
