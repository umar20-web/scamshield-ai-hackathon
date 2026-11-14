import streamlit as st
import joblib

st.set_page_config(
    page_title="ScamShield",
    page_icon="🛡️"
)

model = joblib.load("scamshield_model.pkl")

st.title("🛡️ ScamShield")
st.subheader("AI-Powered SMS Scam Detector")

st.write("Paste an SMS below to check whether it looks suspicious.")

message = st.text_area("Enter your SMS message:")

if st.button("Check Message"):
    if message.strip():
        prediction = model.predict([message])[0]

        if prediction == 1:
            st.error("⚠️ POSSIBLE SPAM! Be careful.")
        else:
            st.success("✅ LIKELY NORMAL MESSAGE")

        st.caption(
            "AI predictions can be wrong. Never share your password, PIN or OTP."
        )
    else:
        st.warning("Please enter a message first.")

st.divider()
st.caption("ScamShield | Veritas AI Hackathon 2026")
