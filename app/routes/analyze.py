from fastapi import APIRouter
from app.services.llm_service import call_llm

router = APIRouter()


@router.post("/analyze")
def analyze_data(prompt: str):
    response = call_llm(prompt)

    if "choices" not in response:
        return {"error": "LLM call failed", "details": response}

    return {"analysis": response["choices"][0]["message"]["content"]}
