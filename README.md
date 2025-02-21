title: Texture Classification
emoji: 🚀
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.1
app_file: scripts/app.py
pinned: false



# Texture Classifier

This repository contains an implementation of a texture classification system that distinguishes between images of stone, brick, and wood textures. The project utilizes feature extraction techniques such as Gray-Level Co-occurrence Matrix (GLCM) and Local Binary Pattern (LBP), combined with machine learning classifiers, to achieve accurate texture recognition.


## REPORT

[📘 view Report](report.md)

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset Preparation](#dataset-preparation)
  - [Image Collection](#image-collection)
  - [Data Splitting](#data-splitting)
- [Feature Extraction Techniques](#feature-extraction-techniques)
  - [GLCM](#glcm)
  - [LBP](#lbp)
- [Classification](#classification)
  - [Choosing Classifiers](#choosing-classifiers)
  - [Training and Evaluation](#training-and-evaluation)
- [Interactive Interface](#interactive-interface)
- [Installation and Usage](#installation-and-usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The goal of this project is to develop a machine learning model capable of classifying images into three categories: stone, brick, or wood. By extracting texture features from images and applying classical machine learning algorithms (excluding deep learning), the system aims to provide accurate and efficient texture classification.

## Dataset Preparation

### Image Collection

- **Objective**: Gather a diverse set of images representing stone, brick, and wood textures.
- **Recommendation**: Collect approximately 150 images, with 50 images per category.
- **Considerations**: Ensure that images vary in conditions such as lighting and scale to simulate real-world scenarios.

### Data Splitting

- **Training Set**: Use 70% of the images for training the model.
- **Testing Set**: Reserve 30% of the images for evaluating model performance.
- **Balance**: Maintain an equal representation of each category in both training and testing sets.

## Feature Extraction Techniques

### GLCM

The Gray-Level Co-occurrence Matrix (GLCM) is used to extract statistical texture features from images.

**Implementation Steps**:

1. Compute the GLCM for each image.
2. Extract features including:
   - Contrast
   - Correlation
   - Energy
   - Homogeneity
3. Experiment with different distances and angles to optimize feature extraction.

### LBP

The Local Binary Pattern (LBP) method captures local texture patterns in images.

**Implementation Steps**:

1. Apply the LBP operator to each image.
2. Generate histograms of LBP codes to create feature vectors.
3. Test various radii and neighbor point configurations to determine the most effective parameters.

## Classification

### Choosing Classifiers

Select appropriate machine learning algorithms such as:

- Support Vector Machines (SVM)
- k-Nearest Neighbors (k-NN)
- Decision Trees

### Training and Evaluation

1. Train separate classifiers using feature vectors obtained from each texture analysis method (GLCM and LBP).
2. Optimize classifier parameters through cross-validation.
3. Evaluate each classifier on the testing set using metrics like accuracy and precision. A confusion matrix can also provide insights into classification performance.

## Interactive Interface

To enhance usability, an interactive interface is developed using [Gradio](https://gradio.app/), a Python library that facilitates the creation of web-based interfaces for machine learning models.

**Features**:

- Users can upload an image and receive a classification result (stone, brick, or wood).
- The interface allows selection between different classification algorithms.

## Installation and Usage

**Prerequisites**:

- Python 3.x
- Required Python packages listed in `requirements.txt`

**Installation Steps**:

1. Clone the repository:
   ```bash
   git clone https://github.com/AlexanderHMagno/Texture-Clasifier.git
