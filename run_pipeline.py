import pandas as pd
from app.services.agent_orchestrator import AgentOrchestrator
from app.utils.cli_renderer import *
import os
from app.utils.file_handler import load_file


def run():

    show_header()

    file_path = input("\nEnter file path (.csv, .xlsx, .xls): ").strip()

    if not os.path.exists(file_path):
        log_error("File not found!")
        return

    log_info("Loading dataset...")

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        log_error(str(e))

    orchestrator = AgentOrchestrator()

    results = orchestrator.run_pipeline(df)

    for step in results["steps"]:
        log_agent(step["step"])
        simulate_delay(1)

        log_success("Completed")
        console.print(Panel(step["output"]))

    log_info("Analysis complete!")


if __name__ == "__main__":
    run()
