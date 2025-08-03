# agents/file_extractor.py

import os

class FileExtractorAgent:
    def run(self, code_dir: str):
        java_files = []
        for root, _, files in os.walk(code_dir):
            for file in files:
                if file.endswith(".java"):
                    full_path = os.path.join(root, file)
                    java_files.append(full_path)
        return java_files

# Instantiate the agent
file_extractor_agent = FileExtractorAgent()
