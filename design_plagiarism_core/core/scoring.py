from typing import Dict, Tuple


# Metric weights (must sum to 1.0)
WEIGHTS = {
    "pixel": 0.15,
    "ssim": 0.35,
    "orb": 0.30,
    "histogram": 0.20,
}


def compute_final_score(scores: Dict[str, float]) -> float:
    """
    Compute weighted final similarity score.
    """
    final_score = 0.0
    for metric, weight in WEIGHTS.items():
        final_score += weight * scores.get(metric, 0.0)

    return round(final_score, 4)


def get_verdict(score: float) -> str:
    """
    Determine similarity verdict based on final score.
    """
    if score >= 0.75:
        return "High Similarity"
    elif score >= 0.5:
        return "Moderate Similarity"
    else:
        return "Low Similarity"


def generate_explanation(scores: Dict[str, float]) -> str:
    """
    Generate a human-readable explanation for the verdict.
    """
    explanations = []

    if scores["ssim"] >= 0.7:
        explanations.append("strong structural similarity")
    if scores["orb"] >= 0.6:
        explanations.append("high feature correspondence")
    if scores["histogram"] >= 0.6:
        explanations.append("similar color distribution")
    if scores["pixel"] >= 0.9:
        explanations.append("near-identical pixel match")

    if not explanations:
        return "Low similarity across structure, features, and color"

    return "Detected " + ", ".join(explanations)
