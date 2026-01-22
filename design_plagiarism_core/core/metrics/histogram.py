import cv2
import numpy as np


def histogram_similarity(img1: np.ndarray, img2: np.ndarray) -> float:
    """
    Compute color histogram similarity using correlation.
    Returns a similarity score in range [0, 1].
    """
    if img1.shape != img2.shape:
        raise ValueError("Images must have the same shape for histogram comparison")

    # Convert BGR to HSV (better for color comparison)
    hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    # Compute histograms for H and S channels
    hist1 = cv2.calcHist([hsv1], [0, 1], None, [50, 60], [0, 180, 0, 256])
    hist2 = cv2.calcHist([hsv2], [0, 1], None, [50, 60], [0, 180, 0, 256])

    # Normalize histograms
    cv2.normalize(hist1, hist1)
    cv2.normalize(hist2, hist2)

    # Correlation returns [-1, 1]
    score = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    # Normalize to [0, 1]
    similarity = (score + 1) / 2

    return float(max(0.0, min(1.0, similarity)))
