from fastapi import APIRouter, UploadFile, File
from app.services.llm_service import call_llm
from app.utils.file_handler import load_file
from app.services.agent_orchestrator import AgentOrchestrator
from fastapi.responses import FileResponse
from app.utils.report_generator import generate_pdf_report
import uuid

router = APIRouter()
REPORT_STORE = {}


@router.post("/analyze")
def analyze_data(prompt: str):
    response = call_llm(prompt)

    if "choices" not in response:
        return {"error": "LLM call failed", "details": response}

    return {"analysis": response["choices"][0]["message"]["content"]}


@router.post("/analyze-file")
async def analyze_file(file: UploadFile = File(...)):

    df = load_file(file)

    orchestrator = AgentOrchestrator()
    results = orchestrator.run_pipeline(df)

    pdf_path = generate_pdf_report(results["steps"])

    report_id = str(uuid.uuid4())

    REPORT_STORE[report_id] = pdf_path

    return {"steps": results["steps"], "report_id": report_id}


@router.get("/download-report/{report_id}")
def download_report(report_id: str):

    if report_id not in REPORT_STORE:
        return {"error": "Report not found"}

    return FileResponse(
        path=REPORT_STORE[report_id],
        filename="analysis_report.pdf",
        media_type="application/pdf",
    )
