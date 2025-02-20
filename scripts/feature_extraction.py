import cv2
import numpy as np
import os
import pandas as pd
import skimage.feature as skf
from skimage.feature import local_binary_pattern
from configuration import check_categories
PROCESSED_PATH = "data/processed/"

def extract_glcm_features(image):
    """Extracts GLCM features from an image."""
    glcm = skf.graycomatrix(image, distances=[1,3,5], angles=[0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256, symmetric=True, normed=True)
    return {
        "contrast": skf.graycoprops(glcm, 'contrast')[0, 0],
        "correlation": skf.graycoprops(glcm, 'correlation')[0, 0],
        "energy": skf.graycoprops(glcm, 'energy')[0, 0],
        "homogeneity": skf.graycoprops(glcm, 'homogeneity')[0, 0]
    }

def extract_lbp_features(image, radius=3, n_points=8 * 3):
    """Extracts LBP histogram from an image."""
    lbp = local_binary_pattern(image, n_points, radius, method="ror")
    hist, _ = np.histogram(lbp.ravel(), bins=np.arange(0, n_points + 3), density=True)
    return hist

def extract_features():
    data = []
    for category in check_categories:
        category_path = os.path.join(PROCESSED_PATH, category)
        for img_name in os.listdir(category_path):
            img_path = os.path.join(category_path, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

            if img is not None:
                glcm_features = extract_glcm_features(img)
                lbp_features = extract_lbp_features(img)
                combined_features = list(glcm_features.values()) + list(lbp_features)
                data.append([category] + combined_features)

    df = pd.DataFrame(data)
    df.to_csv("data/features.csv", index=False)
    print("✅ Feature extraction complete! Saved in data/features.csv")

if __name__ == "__main__":
    extract_features()
