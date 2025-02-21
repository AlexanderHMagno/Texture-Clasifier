# Texture Classifier Report

## Hugging Face Deployment

[😄 HuggingFace](https://huggingface.co/spaces/axelhortua/texture-clasification-traditional-ml)


## Overview

This repository documents the findings and observations from implementing a texture classification system using GLCM (Gray-Level Co-occurrence Matrix) and LBP (Local Binary Pattern) for distinguishing between stone, brick, and wood textures.

## Findings and Observations

### 1) GLCM and LBP as Sources of Texture Analysis

- My first attempt was to generate separate feature sets using GLCM and LBP.

- LBP provided 18 different feature points per image.

- GLCM produced 4 statistical texture features (Energy, Contrast, Homogeneity, and Correlation).

- As standalone methods, both algorithms gave a fair certainty of classification.

- However, when combining both feature sets, classification accuracy increased from 72% to 85%.

### 2) Size of Images

- Another major challenge was image acquisition and preprocessing:

- Collecting thousands of images was difficult due to background noise.

- Many images contained 50% unnecessary background, affecting feature extraction.

- To improve this, I removed white backgrounds and focused only on the texture.

- Image size inconsistency was another issue: stone and brick images were 5x larger than wood images.

- To ensure consistency, I resized all images during preprocessing.

### 3) Models

- I implemented SVM and Decision Trees for classification:

- Initially, I also tested Random Forest, but due to my small dataset, it failed to provide reliable results.

- Based on recommendations, I used SVM and Decision Trees, as they performed better on smaller datasets.

### 4) Prediction Issues

- No matter how I tuned the feature extraction parameters, stone and brick textures appeared highly correlated.

- The classifier often confused stone and brick, predicting either brick or wood incorrectly.

- Even after multiple retraining attempts, it was rarely able to classify stones correctly.

### 5) Accuracy and Testing

- In train.py, I used accuracy_score from sklearn.metrics:

- SVM achieved 86% accuracy.

- Decision Trees reached 78% accuracy.

- A separate test.py script was included to evaluate performance on the test dataset, though the test dataset itself is not provided in this report.

### 6) Data Folder and Feature File

- The dataset folder is not submitted, nor is features.csv.

- This was done intentionally to avoid exposing raw dataset files.

## Conclusion

- This model is not highly reliable, and I view this project as a learning experience rather than a production-ready classifier.

- This lab serves as a general introduction to pre-neural network computer vision.

- In the future, I will likely laugh at myself when I revisit this project.

- If this represents the current state of classical computer vision, I definitely have a lot to improve on! 😆

## Folder Structure

```
Texture-Clasifier/
├── scripts/
│   ├── train.py
│   ├── test.py
│   ├── feature_extraction.py
│   ├── preprocess.py
├── models/
├── data/ (not included)
├── README.md
├── report.md
```
## Explanation of Scripts

### scripts/train.py

- Trains the model using extracted features.

- Uses SVM and Decision Trees for classification.

- Saves the trained models for later use.

### scripts/test.py

- Loads the trained model and evaluates it on the test set.

- Computes accuracy and precision metrics.

### scripts/feature_extraction.py

- Computes GLCM and LBP features from images.

- Stores extracted feature vectors for training.

### scripts/preprocess.py

- Handles image resizing and background removal.

- Ensures all images have a consistent format before feature extraction.

