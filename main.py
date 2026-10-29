"""
Main entry point for Rafeeq Assistant service.
"""
from agent.core import RafeeqAgent
from evals.eval_tasks import run_evaluations

def main():
    print("Initializing Rafeeq Assistant Service...")
    agent = RafeeqAgent()
    
    # Test normal query
    response = agent.run("Search company policy on remote work")
    print("Agent Response:", response)
    
    # Run Evals
    print("Running evaluation suite...")
    evals = run_evaluations()
    print(f"Evaluations completed. Total tasks evaluated: {len(evals)}")

if __name__ == "__main__":
    main()

