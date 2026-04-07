def grade_easy(state):
    return 1.0 if state["balance"] >= 900 else 0.0

def grade_medium(state):
    return 1.0 if state["balance"] >= 1100 else 0.0

def grade_hard(state):
    score = state["balance"] / 1500
    return max(0.0, min(1.0, score))
