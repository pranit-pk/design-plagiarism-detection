from typing import Dict

from .preprocessing import load_image, resize_keep_aspect
from .metrics.pixel import pixel_similarity
from .metrics.ssim import ssim_similarity
from .metrics.orb import orb_similarity
from .metrics.histogram import histogram_similarity
from .scoring import compute_final_score, get_verdict, generate_explanation


def compare_images(image_path_1: str, image_path_2: str) -> Dict:
    """
    Compare two design images and return a similarity report.
    """

    # Load images
    img1 = load_image(image_path_1)
    img2 = load_image(image_path_2)

    # Preprocess (resize with aspect ratio preserved)
    img1 = resize_keep_aspect(img1)
    img2 = resize_keep_aspect(img2)

    # Compute individual metric scores
    scores = {
        "pixel": pixel_similarity(img1, img2),
        "ssim": ssim_similarity(img1, img2),
        "orb": orb_similarity(img1, img2),
        "histogram": histogram_similarity(img1, img2),
    }

    # Final score & verdict
    final_score = compute_final_score(scores)
    verdict = get_verdict(final_score)
    explanation = generate_explanation(scores)

    # Final report
    report = {
        "scores": scores,
        "final_score": final_score,
        "verdict": verdict,
        "explanation": explanation,
    }

    return report
