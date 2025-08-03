    # agents/naming_review.py

import os
from typing import List, Dict
from litellm import completion

class NamingReviewAgent:
    def __init__(self):
        self.model = "deepseek-chat"
        self.api_key = os.getenv("LITELLM_API_KEY")
        self.base_url = "https://api.deepseek.com/v1"  # ✅ FIXED: was api_base
        self.provider = "deepseek"

    def run(self, java_files: List[str]) -> Dict[str, str]:
        feedback = {}
        for file_path in java_files:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    code = f.read()

                prompt = (
                    "You're a Java code reviewer. Please analyze the following code "
                    "and provide detailed feedback on naming conventions, method names, class names, "
                    "and suggest improvements.\n\n"
                    f"Java File Content:\n{code}"
                )

                # ✅ Full explicit call to DeepSeek via LiteLLM
                response = completion(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    api_key=self.api_key,
                    base_url=self.base_url,  # ✅ use base_url not api_base
                    provider=self.provider,
                    temperature=0.3
                )

                feedback[file_path] = response.choices[0].message["content"]

            except Exception as e:
                feedback[file_path] = f"Error reading or analyzing file: {e}"

        return feedback

naming_review_agent = NamingReviewAgent()
