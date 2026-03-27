from app.services.llm_service import call_llm
from app.utils.logger import get_logger


class BaseAgent:
    def __init__(self, role, goal):
        self.role = role
        self.goal = goal
        self.logger = get_logger(self.role)

    def run(self, input_text):
        self.logger.info("Starting agent execution")

        prompt = f"""
        You are a {self.role}.

        Your goal:
        {self.goal}

        STRICT INSTRUCTIONS:
        - Do NOT give generic advice
        - Use ONLY the provided data
        - Be specific and data-driven

        INPUT:
        {input_text}

        OUTPUT FORMAT:
        - Key Findings
        - Issues
        - Recommendations
        """

        response = call_llm(prompt)

        if "choices" not in response:
            self.logger.error(f"LLM Error: {response}")
            return f"Error: {response}"

        output = response["choices"][0]["message"]["content"]

        self.logger.info("Agent execution completed")

        return output
