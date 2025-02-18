import cv2
import os

DATA_PATH = "data/raw/"
PROCESSED_PATH = "data/processed/"
IMG_SIZE = (200, 200)  # Resize images

def preprocess_images():
    if not os.path.exists(PROCESSED_PATH):
        os.makedirs(PROCESSED_PATH)

    for category in ["stone", "brick", "wood"]:
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
