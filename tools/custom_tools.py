```python
"""
Custom Tools and MCP integration definitions for Rafeeq.
"""

def search_knowledge_base(query: str) -> str:
    """Searches the organizational knowledge base for relevant context."""
    # Simulated implementation for capstone
    return f"Knowledge base results for: {query}"

def write_system_record(record_data: str, approved: bool = False) -> str:
    """Writes a record to the system. Requires explicit approval."""
    if not approved:
        return "ERROR: Write operation requires explicit human-in-the-loop approval."
    return f"SUCCESS: Record successfully written: {record_data}"

def calculate_budget_metrics(steps: int, token_cost: float) -> str:
    """Tracks and evaluates step and cost budgets."""
    max_steps = 10
    max_cost = 0.05
    if steps > max_steps or token_cost > max_cost:
        return f"BUDGET WARNING: Steps ({steps}/{max_steps}) or Cost (${token_cost}/${max_cost}) exceeded limits."
    return "Budget within safe operational limits."

