from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_google_genai import GoogleGenerativeAI
import json
import pandas as pd
from typing import List, Dict, Optional

# 1. Initialize the LLM with language support
def get_llm(language: str = "English") -> GoogleGenerativeAI:
    return GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

# 2. First chain: Generate 5 questions with optional image descriptions
question_prompt = PromptTemplate(
    input_variables=["topic", "language", "include_images"],
    template="""Create 5 quiz questions about {topic} in {language}:
- 2 beginner questions
- 2 intermediate questions  
- 1 advanced question

If include_images is "yes", add an "image_description" field for visual questions.

Return ONLY valid JSON:
{
  "questions": [
    {
      "difficulty": "beginner" | "intermediate" | "advanced",
      "question": "question text",
      "image_description": "description for visual question (optional)"
    },
    ...
  ]
}"""
)
question_chain = LLMChain(llm=get_llm(), prompt=question_prompt, output_key="questions_json")

# 3. Second chain: Generate answers
answer_prompt = PromptTemplate(
    input_variables=["questions_json"],
    template="""For each question in this JSON, provide the answer and explanation:
{questions_json}

Return ONLY valid JSON:
{
  "quiz": [
    {
      "difficulty": "beginner" | "intermediate" | "advanced",
      "question": "question text",
      "answer": "correct answer",
      "explanation": "detailed explanation",
      "image_description": "description (optional)"
    },
    ...
  ]
}"""
)
answer_chain = LLMChain(llm=get_llm(), prompt=answer_prompt, output_key="final_quiz_json")

# 4. SequentialChain
quiz_generator = SequentialChain(
    chains=[question_chain, answer_chain],
    input_variables=["topic", "language", "include_images"],
    output_variables=["final_quiz_json"]
)

# 5. Automatic scoring function
def score_quiz(quiz_data: Dict, user_answers: List[str]) -> Dict:
    """
    Validate user answers against quiz data.
    user_answers: List of user's answer strings (one per question)
    """
    results = {
        "total": len(quiz_data["quiz"]),
        "correct": 0,
        "scores": [],
        "percentage": 0
    }
    
    for i, item in quiz_data["quiz"]:
        is_correct = item["answer"].lower() == user_answers[i].lower()
        results["scores"].append({
            "question": i + 1,
            "difficulty": item["difficulty"],
            "user_answer": user_answers[i],
            "correct_answer": item["answer"],
            "is_correct": is_correct,
            "explanation": item["explanation"]
        })
        if is_correct:
            results["correct"] += 1
    
    results["percentage"] = (results["correct"] / results["total"]) * 100
    return results

# 6. Export to CSV/Excel
def export_quiz_to_csv(quiz_data: Dict, filename: str = "quiz.csv") -> str:
    """Export quiz to CSV file"""
    df = pd.DataFrame(quiz_data["quiz"])
    df.to_csv(filename, index=False)
    return filename

def export_quiz_to_excel(quiz_data: Dict, filename: str = "quiz.xlsx") -> str:
    """Export quiz to Excel file"""
    df = pd.DataFrame(quiz_data["quiz"])
    df.to_excel(filename, index=False)
    return filename

# 7. Generate quiz with all features
result = quiz_generator({
    "topic": "photosynthesis",
    "language": "English",
    "include_images": "yes"
})
quiz_data = json.loads(result["final_quiz_json"])

# 8. Display quiz
print("📚 Quiz Generated!")
for i, item in quiz_data["quiz"]:
    print(f"{i+1}. [{item['difficulty'].upper()}] {item['question']}")
    if item.get("image_description"):
        print(f"   🖼️ Image: {item['image_description']}")
    print(f"   Answer: {item['answer']}\n")

# 9. Automatic scoring example
user_answers = [
    "plants convert light to energy",  # Question 1
    "chlorophyll",                      # Question 2
    "CO2 + H2O + light → glucose + O2", # Question 3
    "stomata",                          # Question 4
    "mitochondria"                     # Question 5 (incorrect)
]

score_result = score_quiz(quiz_data, user_answers)
print(f"\n🎯 Score: {score_result['correct']}/{score_result['total']} ({score_result['percentage']:.1f}%)")

# 10. Export to CSV/Excel
csv_file = export_quiz_to_csv(quiz_data, "photosynthesis_quiz.csv")
excel_file = export_quiz_to_excel(quiz_data, "photosynthesis_quiz.xlsx")
print(f"\n💾 Exported to: {csv_file} and {excel_file}")

# 11. Multi-language example (Spanish)
result_spanish = quiz_generator({
    "topic": "fotosíntesis",
    "language": "Spanish",
    "include_images": "no"
})
quiz_spanish = json.loads(result_spanish["final_quiz_json"])
print(f"\n🌍 Spanish Quiz: {quiz_spanish['quiz'][0]['question']}")
