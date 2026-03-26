from fastapi import APIRouter, UploadFile, File
from app.services.llm_service import call_llm
from app.utils.file_handler import read_csv, get_basic_summary

router = APIRouter()


@router.post("/analyze")
def analyze_data(prompt: str):
    response = call_llm(prompt)

    if "choices" not in response:
        return {"error": "LLM call failed", "details": response}

    return {"analysis": response["choices"][0]["message"]["content"]}


@router.post("/analyze-csv")
async def analyze_csv(file: UploadFile = File(...)):

    df = read_csv(file.file)
    summary = get_basic_summary(df)

    prompt = f"""
    You are a data analyst.

    Here is dataset metadata:
    {summary}

    Provide:
    1. Key observations
    2. Data issues
    3. Suggested analysis
    """

    response = call_llm(prompt)

    if "choices" not in response:
        return {"error": response}

    return {
        "summary": summary,
        "analysis": response["choices"][0]["message"]["content"],
    }
