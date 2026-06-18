from src.profile_builder.role_rules import ROLE_RULES

def detect_role(skills):
    scores = {}

    for role, role_skills in ROLE_RULES.items():

        score = len(
            set(skills).intersection(set(role_skills))
        )

        scores[role] = score

    best_role = max(scores, key=scores.get)

    confidence = round(scores[best_role] / len(ROLE_RULES[best_role]), 2)

    return {"role": best_role, "confidence": confidence, "scores": scores}