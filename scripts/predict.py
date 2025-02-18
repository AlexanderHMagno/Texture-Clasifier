import cv2
import numpy as np
import joblib
import scripts.feature_extraction as fe

rf_model = joblib.load("models/rf_model.pkl")

def predict_texture(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    glcm_features = list(fe.extract_glcm_features(img).values())
    lbp_features = list(fe.extract_lbp_features(img))
    features = np.hstack([glcm_features, lbp_features])

    prediction = rf_model.predict([features])[0]
    print(f"Predicted Texture: {prediction}")

# Example usage
predict_texture("data/raw/stone/sample.jpg")
