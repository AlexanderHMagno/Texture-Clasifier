import os
import joblib
import cv2
import numpy as np
import feature_extraction as fe
from configuration import check_categories
# Constants
TEST_PATH = "data/test"
MODEL_PATHS = {
    "Random Forest": "models/rf_model.pkl",
    "SVM": "models/svm_model.pkl",
    "Decision Tree": "models/dt_model.pkl",
}

# Load models
models = {name: joblib.load(path) for name, path in MODEL_PATHS.items()}

# Initialize results dictionary
model_results = {
    name: {cat: {"correct": 0, "wrong": 0} for cat in check_categories}
    for name in models.keys()
}

def extract_features(image: np.ndarray) -> np.ndarray:
    """Extracts GLCM and LBP features from the given image."""
    glcm_features = list(fe.extract_glcm_features(image).values())
    lbp_features = list(fe.extract_lbp_features(image))
    return np.hstack([glcm_features, lbp_features])

def classify_texture(image: np.ndarray, expected_category: str):
    """Classifies the image using all models and updates results."""
    features = extract_features(image)
    
    for model_name, model in models.items():
        prediction = model.predict([features])[0]
        result_key = "correct" if prediction == expected_category else "wrong"
        model_results[model_name][expected_category][result_key] += 1

def test_model():
    """Runs the classification test on all test images."""
    for category in model_results["Random Forest"].keys():
        category_path = os.path.join(TEST_PATH, category)
        if not os.path.exists(category_path):
            print(f"Warning: Category path does not exist: {category_path}")
            continue

        for img_name in os.listdir(category_path):
            img_path = os.path.join(category_path, img_name)
            image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if image is None:
                print(f"Skipping invalid image: {img_path}")
                continue

            try:
                classify_texture(image, category)
            except Exception as e:
                print(f"Error processing {img_path}: {e}")
    
    print(model_results)

# Run model tests
test_model()
