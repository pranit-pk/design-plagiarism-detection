from typing import Dict

# Phase 2: Explicit metric weights (must sum to 1.0)
WEIGHTS = {
    "pixel": 0.15,
    "ssim": 0.35,
    "orb": 0.30,
    "histogram": 0.20,
}


def compute_final_score(scores: Dict[str, float]) -> float:
    """
    Compute weighted final similarity score.
    All scores are assumed to be normalized in [0, 1].
    """
    final_score = 0.0

    for metric, score in scores.items():
        weight = WEIGHTS.get(metric, 0.0)
        final_score += score * weight

    return round(final_score, 3)


def get_verdict(final_score: float) -> str:
    """
    Convert final score into a human-readable verdict.
    """
    if final_score >= 0.75:
        return "High Similarity"
    elif final_score >= 0.45:
        return "Moderate Similarity"
    else:
        return "Low Similarity"


def generate_explanation(scores: Dict[str, float]) -> str:
    """
    Generate a simple explanation based on the dominant metric.
    """
    dominant_metric = max(scores, key=scores.get)
    dominant_score = scores[dominant_metric]

    return (
        f"The similarity is primarily driven by {dominant_metric.upper()} "
        f"with a score of {dominant_score:.2f}."
    )
