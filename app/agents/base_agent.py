from app.services.llm_service import call_llm


class BaseAgent:
    def __init__(self, role, goal):
        self.role = role
        self.goal = goal

    def run(self, input_text):
        prompt = f"""
        You are a {self.role}.

        Your goal:
        {self.goal}

        STRICT INSTRUCTIONS:
        - Do NOT give generic advice
        - Use ONLY the provided data
        - Be specific and data-driven
        - Give bullet points

        INPUT DATA:
        {input_text}

        OUTPUT FORMAT:
        - Key Findings:
        - Issues:
        - Recommendations:
        """

        response = call_llm(prompt)

        if "choices" not in response:
            return f"Error: {response}"

        return response["choices"][0]["message"]["content"]
