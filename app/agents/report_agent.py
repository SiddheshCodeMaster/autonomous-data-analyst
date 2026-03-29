from app.agents.base_agent import BaseAgent


class ReportAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Management Consultant",
            goal="""
            Create a professional McKinsey-style report with:
            - Executive Summary
            - Key Insights
            - Business Recommendations
            - Risks
            """,
        )
