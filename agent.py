from langchain.tools import tool

# -------- TOOLS -------- #

@tool
def log_interaction(doctor: str, notes: str):
    """Log an interaction with a healthcare professional."""
    return f"Interaction with {doctor} logged. Notes: {notes}"


@tool
def edit_interaction(doctor: str, new_notes: str):
    """Edit an interaction."""
    return f"Interaction updated for {doctor}"


@tool
def view_history(doctor: str):
    """View interaction history."""
    return f"Showing history for {doctor}"


@tool
def schedule_followup(doctor: str, date: str):
    """Schedule follow up."""
    return f"Follow up scheduled with {doctor} on {date}"


@tool
def summarize_notes(notes: str):
    """Summarize notes."""
    return f"Summary: {notes}"


# -------- SIMPLE AGENT SIMULATION -------- #

def run_agent():
    print("AI CRM Agent Started\n")

    result = log_interaction.invoke({
        "doctor": "Dr Sharma",
        "notes": "Discussed diabetes medication"
    })

    print(result)


run_agent()