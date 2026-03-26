from app.agents.data_cleaner import DataCleanerAgent
from app.agents.eda_agent import EDAAgent
from app.agents.insight_agent import InsightAgent


class AgentOrchestrator:
    def __init__(self):
        self.cleaner = DataCleanerAgent()
        self.eda = EDAAgent()
        self.insight = InsightAgent()

    def run_pipeline(self, summary):

        cleaner_output = self.cleaner.run(str(summary))

        eda_output = self.eda.run(cleaner_output)

        insight_output = self.insight.run(eda_output)

        return {
            "cleaning": cleaner_output,
            "eda": eda_output,
            "insights": insight_output,
        }
