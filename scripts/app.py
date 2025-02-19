import gradio as gr
import cv2
import numpy as np
import joblib
import feature_extraction as fe
from configuration import theme, css, article

rf_model = joblib.load("models/rf_model.pkl")
svm_model = joblib.load("models/svm_model.pkl")

def classify_texture(image):

    if image is None:
        return "Error: No image provided", "Error: No image provided"
    # Convert PIL image to numpy array and ensure grayscale
    image = np.array(image.convert('L'))


    glcm_features = list(fe.extract_glcm_features(image).values())
    lbp_features = list(fe.extract_lbp_features(image))
    features = np.hstack([glcm_features, lbp_features])

    rf_prediction = rf_model.predict([features])[0]
    svm_prediction = svm_model.predict([features])[0]

    return f"Random Forest: {rf_prediction}", f"SVM: {svm_prediction}"


# Create a more professional interface
demo = gr.Interface(
    fn=classify_texture,
    inputs= [gr.Image(type="pil", label="Upload Texture Image")],

    outputs=[gr.Label(label="Classification Random Forest"), gr.Label(label="Classification SVM")],
    title="Material Texture Classifier",
    description="""This application classifies material textures into three categories: stone, brick, and wood.
                   Upload an image of a texture and the model will predict its material type.""",
    examples=[
        ["data/samples/rock.png", 'SVM'],
        ["data/samples/brick.png", 'SVM'],
        ["data/samples/wood.jpg", 'SVM']
    ],
    article = article,
    theme = theme ,
    css = css
)


demo.launch()
