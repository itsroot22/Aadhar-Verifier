# Aadhar Age and Face Verifier

This is a simple Streamlit web app that verifies a person's age and facial identity using an image of their Aadhar card and a selfie. It uses OCR to extract the date of birth from the Aadhar image and checks if the user is 18 or older. It also matches the face from the Aadhar card with a selfie using DeepFace.

## Features

- Extracts Date of Birth (DOB) from Aadhar card using Tesseract OCR
- Calculates age and verifies if the person is 18+
- Detects and crops face from the Aadhar card
- Compares the face with a selfie using DeepFace
- Displays confidence score for face match

## How It Works

1. User uploads an image of their Aadhar card.
2. The app extracts text using Tesseract and looks for a date pattern.
3. The extracted DOB is used to calculate the age.
4. The face from the Aadhar is detected using OpenCV.
5. The user uploads a selfie for comparison.
6. DeepFace checks if the two faces match and returns a confidence score.

## Installation

1. Install Tesseract OCR on your system:
   - [Download Tesseract](https://github.com/tesseract-ocr/tesseract)
   - For Windows, install it to: `C:\Program Files\Tesseract-OCR`
   - Ensure that the `eng.traineddata` file exists inside the `tessdata` folder.

2. Clone this repo and install the required Python packages:

```bash
pip install -r requirements.txt
