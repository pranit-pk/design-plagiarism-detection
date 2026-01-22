import cv2
import numpy as np


def orb_similarity(img1: np.ndarray, img2: np.ndarray) -> float:
    """
    Compute feature-based similarity using ORB keypoints.
    Returns a similarity score in range [0, 1].
    """
    if img1.shape != img2.shape:
        raise ValueError("Images must have the same shape for ORB comparison")

    # Convert to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create(nfeatures=500)

    kp1, des1 = orb.detectAndCompute(gray1, None)
    kp2, des2 = orb.detectAndCompute(gray2, None)

    # Handle edge cases (no features)
    if des1 is None or des2 is None:
        return 0.0

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    if not matches:
        return 0.0

    # Good matches relative to number of keypoints
    similarity = len(matches) / max(len(kp1), len(kp2))

    return float(min(1.0, similarity))
