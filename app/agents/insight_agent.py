from app.agents.base_agent import BaseAgent


class InsightAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Business Analyst",
            goal="Generate actionable business insights from the dataset",
        )
