from fastapi import APIRouter, UploadFile, File
from app.services.llm_service import call_llm
from app.utils.file_handler import read_csv, get_basic_summary
from app.services.agent_orchestrator import AgentOrchestrator

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

    orchestrator = AgentOrchestrator()
    results = orchestrator.run_pipeline(summary)

    return {"summary": summary, "agent_outputs": results}
