import cv2
import numpy as np
from typing import Tuple


def load_image(path: str) -> np.ndarray:
    """
    Load an image from disk in BGR format using OpenCV.
    Raises ValueError if image cannot be loaded.
    """
    image = cv2.imread(path)

    if image is None:
        raise ValueError(f"Unable to load image from path: {path}")

    return image


def resize_keep_aspect(
    image: np.ndarray,
    target_size: Tuple[int, int] = (512, 512)
) -> np.ndarray:
    """
    Resize image while maintaining aspect ratio.
    Pads remaining area with black pixels.
    """
    h, w = image.shape[:2]
    target_w, target_h = target_size

    scale = min(target_w / w, target_h / h)
    new_w, new_h = int(w * scale), int(h * scale)

    resized = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)

    canvas = np.zeros((target_h, target_w, 3), dtype=np.uint8)
    x_offset = (target_w - new_w) // 2
    y_offset = (target_h - new_h) // 2

    canvas[y_offset:y_offset + new_h, x_offset:x_offset + new_w] = resized
    return canvas


def to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Convert BGR image to grayscale.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def normalize_image(image: np.ndarray) -> np.ndarray:
    """
    Normalize pixel values to range [0, 1].
    """
    return image.astype(np.float32) / 255.0
