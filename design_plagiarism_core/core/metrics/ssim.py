import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim


def ssim_similarity(img1: np.ndarray, img2: np.ndarray) -> float:
    """
    Compute Structural Similarity Index (SSIM) between two images.
    Returns a similarity score in range [0, 1].
    """
    if img1.shape != img2.shape:
        raise ValueError("Images must have the same shape for SSIM")

    # Convert to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    score, _ = ssim(gray1, gray2, full=True)

    # SSIM score is already in [-1, 1], but practically [0, 1]
    return float(max(0.0, min(1.0, score)))
