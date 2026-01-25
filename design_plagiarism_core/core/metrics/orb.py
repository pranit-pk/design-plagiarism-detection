import cv2


def orb_similarity(img1, img2):
    orb = cv2.ORB_create(nfeatures=500)

    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    if des1 is None or des2 is None:
        return 0.0

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    max_possible = min(len(kp1), len(kp2))

    if max_possible == 0:
        return 0.0

    return len(matches) / max_possible
