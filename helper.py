from PIL import Image
import pytesseract
import cv2
import numpy as np
import re
from deepface import DeepFace
import os

# Tesseract setup
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"

def extract_dob(image_file):
    img = Image.open(image_file)
    text = pytesseract.image_to_string(img)

    # Find DOB using regex
    dob = None
    match = re.search(r'(\d{2}[/-]\d{2}[/-]\d{4})', text)
    if match:
        dob = match.group(1).replace('/', '-')

    # Convert to OpenCV and extract face
    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    face_img = extract_face(img_cv)

    return dob, face_img

def extract_face(cv_img):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        return Image.fromarray(cv_img[y:y+h, x:x+w][..., ::-1])  # BGR to RGB
    return None

def match_faces(face1_img, face2_file):
    try:
        img1 = np.array(face1_img)
        img2 = np.array(Image.open(face2_file))

        result = DeepFace.verify(
            img1_path=img1,
            img2_path=img2,
            model_name="VGG-Face",
            enforce_detection=False
        )

        verified = result.get("verified", False)
        distance = result.get("distance", 1.0)
        confidence = (1 - distance) * 100

        return verified, confidence

    except Exception as e:
        print("Face match error:", e)
        return False, 0
