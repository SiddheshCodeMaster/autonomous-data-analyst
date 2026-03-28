from fastapi import APIRouter, UploadFile, File
from app.services.llm_service import call_llm
from app.utils.file_handler import load_file
from app.services.agent_orchestrator import AgentOrchestrator


router = APIRouter()


@router.post("/analyze")
def analyze_data(prompt: str):
    response = call_llm(prompt)

    if "choices" not in response:
        return {"error": "LLM call failed", "details": response}

    return {"analysis": response["choices"][0]["message"]["content"]}


@router.post("/analyze-file")
async def analyze_file(file: UploadFile = File(...)):

    try:
        df = load_file(file.file)
    except Exception as e:
        return {"error": str(e)}

    orchestrator = AgentOrchestrator()
    return orchestrator.run_pipeline(df)
