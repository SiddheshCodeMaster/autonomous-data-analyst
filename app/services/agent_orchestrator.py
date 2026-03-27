from app.agents.data_cleaner import DataCleanerAgent
from app.agents.eda_agent import EDAAgent
from app.agents.insight_agent import InsightAgent
from app.utils.data_tools import (
    get_numeric_summary,
    get_correlation,
    get_sample_data,
    get_column_info,
)


class AgentOrchestrator:
    def __init__(self):
        self.cleaner = DataCleanerAgent()
        self.eda = EDAAgent()
        self.insight = InsightAgent()

    def run_pipeline(self, df):

        column_info = get_column_info(df)
        sample_data = get_sample_data(df)
        numeric_summary = get_numeric_summary(df)
        correlation = get_correlation(df)

        # Step 1: Cleaning Agent
        cleaner_input = {
            "column_info": column_info,
            "missing_values": df.isnull().sum().to_dict(),
        }

        cleaner_output = self.cleaner.run(str(cleaner_input))

        # Step 2: EDA Agent
        eda_input = {
            "column_info": column_info,
            "numeric_summary": numeric_summary,
            "correlation": correlation,
            "sample_data": sample_data,
        }

        eda_output = self.eda.run(str(eda_input))

        # Step 3: Insight Agent
        insight_input = {"eda_output": eda_output, "cleaning_output": cleaner_output}

        insight_output = self.insight.run(str(insight_input))

        return {
            "cleaning": cleaner_output,
            "eda": eda_output,
            "insights": insight_output,
        }
