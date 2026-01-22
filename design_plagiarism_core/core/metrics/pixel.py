import numpy as np


def pixel_similarity(img1: np.ndarray, img2: np.ndarray) -> float:
    """
    Compute pixel-level similarity using Mean Squared Error (MSE).
    Returns a similarity score in range [0, 1].
    """
    if img1.shape != img2.shape:
        raise ValueError("Images must have the same shape for pixel comparison")

    # Convert to float to avoid overflow
    img1 = img1.astype(np.float32)
    img2 = img2.astype(np.float32)

    mse = np.mean((img1 - img2) ** 2)

    # Normalize: higher MSE → lower similarity
    similarity = 1 / (1 + mse)

    return float(similarity)
