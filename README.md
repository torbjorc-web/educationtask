# AI Quiz Generator and Teacher Dashboard

This project builds an AI-powered quiz generator using LangChain chain composition and provides a browser-based quiz app plus a teacher dashboard.

## Features

- Generate beginner, intermediate, and advanced quiz questions.
- Create detailed answers and explanations.
- Present quizzes in an interactive browser form.
- Track student progress over time in a teacher dashboard.
- Upload JSON files directly in the dashboard.
- Export merged dashboard data as JSON or CSV.

## Project Files

- `quiz_app.py` — Python code for generating quiz data.
- `quiz_app.html` — Interactive quiz student interface.
- `teacher_dashboard.html` — Dashboard with embedded sample data.
- `teacher_dashboard_upload.html` — Dashboard that accepts uploaded JSON files.
- `teacher_dashboard_upload_export.html` — Dashboard with upload and export support.
- `quiz_data.json` — Example quiz data output.
- `analytics.json` — Example analytics summary.
- `student_improvement.json` — Example student progress data.

## Requirements

Install these packages in your notebook or environment:

```bash
pip install langchain langchain-community langchain-google-genai pandas
```

You also need a Google Gemini API key.

## API Key Setup

### Google Colab
- Open the secrets panel.
- Add `GEMINI_API_KEY`.
- Enable notebook access.

### Local Jupyter / VS Code
- Set an environment variable, or use a `.env` file.

Example:

```bash
export GEMINI_API_KEY="your_key_here"
```

## How It Works

### 1. Quiz generation
The Python code uses LangChain with:
- `PromptTemplate`
- `LLMChain`
- `SequentialChain`

The first chain creates quiz questions. The second chain generates answers and explanations.

### 2. Student quiz app
The HTML quiz app displays questions, accepts answers, grades them, and shows explanations.

### 3. Teacher dashboard
The dashboard shows:
- Total students
- Attempts
- Average score
- Performance distribution
- Difficulty breakdown
- Student progress trends
- Quiz overview

### 4. Upload and export
The upload dashboard lets you:
- Load quiz and progress JSON files
- Export merged data as JSON
- Export merged data as CSV

## Example JSON Formats

### Quiz data
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

### Analytics data
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

### Student progress data
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

### Generate quiz data
Run the Python script to create `quiz_data.json`.

### Open the quiz app
Open `quiz_app.html` in a browser.

### Open the teacher dashboard
Open `teacher_dashboard_upload_export.html` in a browser.

### Upload files
Load your JSON files through the upload form in the dashboard.

## Notes

- The dashboard uses Plotly from a CDN.
- The upload version can run with sample data if no files are provided.
- You can customize topics, languages, and difficulty levels in the Python code.

## Suggested Folder Layout

```text
project/
├── quiz_app.py
├── quiz_app.html
├── teacher_dashboard.html
├── teacher_dashboard_upload.html
├── teacher_dashboard_upload_export.html
├── quiz_data.json
├── analytics.json
└── student_improvement.json
```
