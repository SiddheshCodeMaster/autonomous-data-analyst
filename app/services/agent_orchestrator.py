from app.agents.data_cleaner import DataCleanerAgent
from app.agents.eda_agent import EDAAgent
from app.agents.insight_agent import InsightAgent
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
        self.cleaner = DataCleanerAgent()
        self.eda = EDAAgent()
        self.insight = InsightAgent()

    def run_pipeline(self, df):

        self.logger.info("Pipeline started")

        steps = []

        # Data prep
        self.logger.info("Extracting dataset features")

        column_info = get_column_info(df)
        sample_data = get_sample_data(df)
        numeric_summary = get_numeric_summary(df)
        correlation = get_correlation(df)

        # Cleaner
        self.logger.info("Running Data Cleaner Agent")

        cleaner_output = self.cleaner.run(
            str(
                {
                    "column_info": column_info,
                    "missing_values": df.isnull().sum().to_dict(),
                }
            )
        )

        steps.append(
            {
                "step": "Data Cleaning Agent",
                "status": "completed",
                "output": cleaner_output,
            }
        )

        # EDA
        self.logger.info("Running EDA Agent")

        eda_output = self.eda.run(
            str(
                {
                    "column_info": column_info,
                    "numeric_summary": numeric_summary,
                    "correlation": correlation,
                    "sample_data": sample_data,
                }
            )
        )

        steps.append({"step": "EDA Agent", "status": "completed", "output": eda_output})

        # Insights
        self.logger.info("Running Insight Agent")

        insight_output = self.insight.run(
            str({"eda_output": eda_output, "cleaning_output": cleaner_output})
        )

        steps.append(
            {"step": "Insight Agent", "status": "completed", "output": insight_output}
        )

        self.logger.info("Pipeline completed")

        return {"steps": steps}
