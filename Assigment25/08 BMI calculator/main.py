import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="🧮", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f6;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .title {
        text-align: center;
        font-size: 3em;
        font-weight: bold;
        color: #2e7d32;
    }
    .subtitle {
        text-align: center;
        font-size: 1.5em;
        color: #555;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🧮 BMI Calculator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Built with ❤️ using Python + Streamlit</div>', unsafe_allow_html=True)

st.write("---")

st.header("📋 Enter your details")

weight = st.number_input("⚖️ Weight (in kilograms)", min_value=0.0, format="%.2f")
height = st.number_input("📏 Height (in meters)", min_value=0.0, format="%.2f")

if st.button("Calculate BMI 🚀"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.success(f"🎯 Your BMI is: **{bmi:.2f}**")

        if bmi < 18.5:
            st.info("🍃 You are **Underweight**. Try to have a nutritious diet!")
        elif 18.5 <= bmi < 24.9:
            st.success("🏋️‍♂️ You have a **Normal Weight**. Keep it up!")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ You are **Overweight**. Consider a healthy lifestyle!")
        else:
            st.error("🔥 You are **Obese**. Important to consult a healthcare provider!")
    else:
        st.error("❌ Please enter a valid height above 0 meters.")

st.write("---")
st.caption("🛠️ Developed by Syed Ahsan | Powered by Python & Streamlit")
