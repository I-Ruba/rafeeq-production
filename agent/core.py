"""
Core Agent orchestration logic for Rafeeq in Production.
"""
from tools.custom_tools import search_knowledge_base, write_system_record, calculate_budget_metrics

class RafeeqAgent:
    def __init__(self):
        self.step_count = 0
        self.current_cost = 0.00
        self.memory = []

    def run(self, prompt: str, require_approval: bool = False) -> str:
        self.step_count += 1
        self.current_cost += 0.002
        
        # Check budget rule
        budget_status = calculate_budget_metrics(self.step_count, self.current_cost)
        if "WARNING" in budget_status:
            return budget_status

        # Handle intent
        if "write" in prompt.lower():
            if require_approval:
                result = write_system_record(prompt, approved=True)
            else:
                result = write_system_record(prompt, approved=False)
        else:
            result = search_knowledge_base(prompt)

        self.memory.append({"prompt": prompt, "response": result})
        return result

