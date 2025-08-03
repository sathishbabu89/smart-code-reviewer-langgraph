# agents/code_smell.py

import os
from typing import List, Dict
from litellm import completion

class CodeSmellAgent:
    def __init__(self):
        self.model = "deepseek-chat"
        self.api_key = os.getenv("LITELLM_API_KEY")
        self.base_url = "https://api.deepseek.com/v1"
        self.provider = "deepseek"

    def run(self, java_files: List[str]) -> Dict[str, str]:
        feedback = {}
        for file_path in java_files:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    code = f.read()

                prompt = (
                    "You're a senior Java architect. Carefully analyze the following Java code "
                    "and identify any code smells (e.g., large classes, long methods, duplicated logic, poor cohesion, etc). "
                    "Provide detailed comments with suggestions for refactoring.\n\n"
                    f"Java File Content:\n{code}"
                )

                response = completion(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    api_key=self.api_key,
                    base_url=self.base_url,
                    provider=self.provider,
                    temperature=0.3
                )

                feedback[file_path] = response.choices[0].message["content"]

            except Exception as e:
                feedback[file_path] = f"Error analyzing file: {e}"

        return feedback

code_smell_agent = CodeSmellAgent()
