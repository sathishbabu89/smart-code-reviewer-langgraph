# langgraph_review.py (modified)

import os
from pathlib import Path
from typing import TypedDict, List, Dict, Any   

from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph, END
from agents.file_extractor import file_extractor_agent
from agents.naming_review import naming_review_agent
from agents.code_smell import code_smell_agent
from agents.security_review import security_review_agent as security_agent

# Define the schema properly as a TypedDict
class ReviewState(TypedDict):
    code_dir: str
    java_files: List[str]
    review_feedback: Dict[str, Dict[str, str]]
    final_report: str  # ✅ Add this!

# -- State schema
def initialize_state(code_dir: str) -> Dict[str, Any]:
    return {
        "code_dir": code_dir,
        "java_files": [],
        "review_feedback": {}
    }

# -- File extraction
def extract_java_files_node(state: Dict[str, Any]) -> Dict[str, Any]:
    java_files = file_extractor_agent.run(state["code_dir"])
    state["java_files"] = java_files
    return state

# -- Full analysis: naming + smell + security
def analyze_code_node(state: Dict[str, Any]) -> Dict[str, Any]:
    java_files = state["java_files"]

    naming_feedback = naming_review_agent.run(java_files)
    code_smell_feedback = code_smell_agent.run(java_files)
    security_feedback = security_agent.run(java_files)

    # Merge all agent feedbacks
    state["review_feedback"] = {
        file: {
            "naming": naming_feedback.get(file, "No feedback"),
            "smells": code_smell_feedback.get(file, "No feedback"),
            "security": security_feedback.get(file, "No feedback")
        }
        for file in java_files
    }

    return state

# -- Final report
def generate_report_node(state: Dict[str, Any]) -> Dict[str, Any]:
    report = "### Code Review Report\n\n"
    for file, feedback in state["review_feedback"].items():
        report += f"**File:** `{file}`\n"
        for category, result in feedback.items():
            report += f"- **{category.capitalize()}**: {result}\n"
        report += "\n"

    state["final_report"] = report  # ✅ Add this line
    return state  # ✅ Make sure to return the state dictionary


# -- Graph builder
def build_graph():
    
 
    builder = StateGraph(ReviewState)
    builder.add_node("extract_files", extract_java_files_node)
    builder.add_node("analyze_code", analyze_code_node)
    builder.add_node("generate_report", generate_report_node)

    builder.set_entry_point("extract_files")
    builder.add_edge("extract_files", "analyze_code")
    builder.add_edge("analyze_code", "generate_report")
    builder.set_finish_point("generate_report")

    return builder.compile()

# -- Runner
def run_code_review(code_dir: str) -> str:
    graph = build_graph()
    initial_state = initialize_state(code_dir)
    result = graph.invoke(initial_state)
    return result["final_report"]  # ✅ Extract final_report
