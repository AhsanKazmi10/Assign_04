import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="My First Website", page_icon="🌐", layout="wide")

# --- Custom CSS Styling ---
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
        color: #1a73e8;
        padding-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        font-size: 1.5em;
        color: #555;
        padding-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Main Title ---
st.markdown('<div class="title">🌐 Welcome to My Website</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Built with 🐍 Python and Streamlit</div>', unsafe_allow_html=True)

# --- Horizontal Line ---
st.write("---")

# --- About Section ---
st.header("🧑‍💻 About Me")
st.write("""
Hello! I'm a passionate developer learning how to create awesome websites and apps with Python.  
I love coding, tech, and building cool projects! 🚀
""")

# --- Skills Section ---
st.header("⚡ Skills")
st.write("""
- Python 🐍
- Web Development 🌐
- Machine Learning 🤖
- Problem Solving 🧠
""")

# --- Projects Section ---
st.header("🛠️ Projects")
st.write("""
Here are some projects I have worked on:
- BMI Calculator App 🧮
- Password Generator 🔐
- Countdown Timer ⏳
- Hangman Game 🎯
""")

# --- Contact Section ---
st.header("📞 Contact Me")
st.write("Feel free to connect with me!")
st.write("- 📧 Email: syedahsankazmi95@gmail.com")
st.write("- 💼 LinkedIn: [https://www.linkedin.com/in/ahsankazmi110/])")

# --- Footer ---
st.write("---")
st.caption("🚀 Built with Streamlit | © 2025 Syed Ahsan")
