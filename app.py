import streamlit as st
from helper import extract_dob, match_faces

st.set_page_config(page_title="Aadhar Verifier", layout="centered")
st.title("Aadhar Age & Face Verifier")

# Upload inputs
aadhar_img = st.file_uploader("📄 Upload Aadhar Image", type=["jpg", "png", "jpeg"])
selfie_img = st.file_uploader("🤳 Upload Selfie Image", type=["jpg", "png", "jpeg"])

# Run on button click
if st.button("✅ Verify") and aadhar_img and selfie_img:
    with st.spinner("Processing..."):
        dob, aadhar_face = extract_dob(aadhar_img)

        # Date of Birth logic
        if dob:
            st.success(f"📅 Date of Birth: {dob}")
            year = int(dob.split("-")[-1])
            age = 2025 - year
            st.info(f"🎂 Age: {age} years")
            if age >= 18:
                st.success("✅ Age Verified (18+)")
            else:
                st.warning("⚠️ Underage")
        else:
            st.warning("❗ DOB not found!")

        # Face match logic
        if aadhar_face:
            st.image(aadhar_face, caption="🪪 Face from Aadhar")
            st.image(selfie_img, caption="📷 Selfie")

            match, score = match_faces(aadhar_face, selfie_img)
            THRESHOLD = 95  # Strict threshold

            if match and score >= THRESHOLD:
                st.success(f"✅ Face Matched! Confidence: {score:.2f}%")
            else:
                st.error(f"❌ Face Not Matched. Confidence: {score:.2f}% (Below {THRESHOLD}%)")
                st.info("📸 Please upload a clearer or real photo for accurate verification.")
        else:
            st.warning("😕 Could not extract face from Aadhar image")
