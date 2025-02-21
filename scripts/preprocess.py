import cv2
import os
from configuration import check_categories
DATA_PATH = "data/raw/"
PROCESSED_PATH = "data/processed/"
IMG_SIZE = (200, 200)  # Resize images

def preprocess_images():

    # Create processed directory if it doesn't exist
    if not os.path.exists(PROCESSED_PATH):
        os.makedirs(PROCESSED_PATH)
    
    # Delete all files and subdirectories in PROCESSED_PATH if it exists
    for root, dirs, files in os.walk(PROCESSED_PATH, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    for category in check_categories:
        category_path = os.path.join(DATA_PATH, category)
        processed_category_path = os.path.join(PROCESSED_PATH, category)

        if not os.path.exists(processed_category_path):
            os.makedirs(processed_category_path)

        for img_name in os.listdir(category_path):
            img_path = os.path.join(category_path, img_name)
            img = cv2.imread(img_path)

            if img is not None:
                img = cv2.resize(img, IMG_SIZE)
                gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(os.path.join(processed_category_path, img_name), gray_img)

if __name__ == "__main__":
    preprocess_images()
    print("✅ Images preprocessed and saved in data/processed/")
