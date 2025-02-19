import gradio as gr
import cv2
import numpy as np
import joblib
import feature_extraction as fe

rf_model = joblib.load("models/rf_model.pkl")

def classify_texture(image):
    # Convert PIL image to numpy array and ensure grayscale
    image = np.array(image.convert('L'))
    glcm_features = list(fe.extract_glcm_features(image).values())
    lbp_features = list(fe.extract_lbp_features(image))
    features = np.hstack([glcm_features, lbp_features])

    prediction = rf_model.predict([features])[0]
    return f"Predicted Texture: {prediction}"

demo = gr.Interface(fn=classify_texture, inputs=gr.Image(type="pil"), outputs="text")
demo.launch()
