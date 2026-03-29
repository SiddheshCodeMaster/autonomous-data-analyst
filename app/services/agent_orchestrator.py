from app.agents.data_cleaner import DataCleanerAgent
from app.agents.eda_agent import EDAAgent
from app.agents.insight_agent import InsightAgent
from app.agents.report_agent import ReportAgent

from app.utils.data_tools import (
    get_numeric_summary,
    get_correlation,
    get_sample_data,
    get_column_info,
)

from app.utils.logger import get_logger


class AgentOrchestrator:
    def __init__(self):
        self.logger = get_logger("Orchestrator")

        # Agents
        self.cleaner = DataCleanerAgent()
        self.eda = EDAAgent()
        self.insight = InsightAgent()
        self.report = ReportAgent()

    def run_pipeline(self, df):

        self.logger.info("Pipeline started")

        steps = []

        try:
            # =========================
            # STEP 0: DATA PREPARATION
            # =========================
            self.logger.info("Extracting dataset features")

            column_info = get_column_info(df)
            sample_data = get_sample_data(df)
            numeric_summary = get_numeric_summary(df)
            correlation = get_correlation(df)

            # =========================
            # STEP 1: DATA CLEANING
            # =========================
            self.logger.info("Running Data Cleaner Agent")

            cleaner_input = {
                "column_info": column_info,
                "missing_values": df.isnull().sum().to_dict(),
            }

            cleaner_output = self.cleaner.run(str(cleaner_input))

            steps.append(
                {
                    "step": "Data Cleaning Agent",
                    "status": "completed",
                    "output": cleaner_output,
                }
            )

            # =========================
            # STEP 2: EDA
            # =========================
            self.logger.info("Running EDA Agent")

            eda_input = {
                "column_info": column_info,
                "numeric_summary": numeric_summary,
                "correlation": correlation,
                "sample_data": sample_data,
            }

            eda_output = self.eda.run(str(eda_input))

            steps.append(
                {
                    "step": "EDA Agent",
                    "status": "completed",
                    "output": eda_output,
                }
            )

            # =========================
            # STEP 3: INSIGHTS
            # =========================
            self.logger.info("Running Insight Agent")

            insight_input = {
                "eda_output": eda_output,
                "cleaning_output": cleaner_output,
            }

            insight_output = self.insight.run(str(insight_input))

            steps.append(
                {
                    "step": "Insight Agent",
                    "status": "completed",
                    "output": insight_output,
                }
            )

            # =========================
            # STEP 4: FINAL REPORT (🔥 NEW)
            # =========================
            self.logger.info("Generating Final Report")

            report_input = {
                "cleaning": cleaner_output,
                "eda": eda_output,
                "insights": insight_output,
            }

            report_output = self.report.run(str(report_input))

            steps.append(
                {
                    "step": "Final Report",
                    "status": "completed",
                    "output": report_output,
                }
            )

            self.logger.info("Pipeline completed successfully")

            return {"steps": steps, "report": report_output}

        except Exception as e:
            self.logger.error(f"Pipeline failed: {str(e)}")

            steps.append(
                {
                    "step": "Error",
                    "status": "failed",
                    "output": str(e),
                }
            )

            return {"steps": steps}
