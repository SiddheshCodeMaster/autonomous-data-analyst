from app.agents.base_agent import BaseAgent


class DataCleanerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Data Cleaning Specialist",
            goal="Identify missing values, incorrect data types, and suggest cleaning steps",
        )
