import gradio as gr
import cv2
import numpy as np
import joblib
import feature_extraction as fe
from configuration import theme, css, article

rf_model = joblib.load("models/rf_model.pkl")

def classify_texture(image):
    # Convert PIL image to numpy array and ensure grayscale
    image = np.array(image.convert('L'))
    glcm_features = list(fe.extract_glcm_features(image).values())
    lbp_features = list(fe.extract_lbp_features(image))
    features = np.hstack([glcm_features, lbp_features])

    prediction = rf_model.predict([features])[0]
    return f"Predicted Texture: {prediction}"


# Create a more professional interface
demo = gr.Interface(
    fn=classify_texture,
    inputs= [gr.Image(type="pil", label="Upload Texture Image")],
    outputs=gr.Label(label="Classification Result"),
    title="Material Texture Classifier",
    description="""This application classifies material textures into three categories: stone, brick, and wood.
                   Upload an image of a texture and the model will predict its material type.""",
    examples=[
        ["data/samples/rock.png", 'stone'],
        ["data/samples/brick.png", 'brick'],
        ["data/samples/wood.png", 'wood']
    ],
    article = article,
    theme = theme ,
    css = css
)


demo.launch()
