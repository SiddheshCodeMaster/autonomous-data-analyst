from app.agents.base_agent import BaseAgent


class EDAAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Exploratory Data Analyst",
            goal="Analyze dataset structure and identify trends and patterns",
        )
