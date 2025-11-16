import streamlit as st
import random

# ------------------------
# Initialize session state
# ------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ------------------------
# Background and styles
# ------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }
    .stButton>button {
        background-color: #FF6F61;
        color: white;
        height: 3em;
        width: 200px;
        border-radius: 10px;
        border: none;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        margin: 5px;
    }
    .stButton>button:hover {
        background-color: #FF3B2E;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------
# Navigation Buttons
# ------------------------
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Home"):
        st.session_state.page = "home"
with col2:
    if st.button("Categories"):
        st.session_state.page = "categories"
with col3:
    if st.button("About"):
        st.session_state.page = "about"

# ------------------------
# Home Page
# ------------------------
if st.session_state.page == "home":
    st.markdown("<h1 style='text-align:center; color:white;'>Welcome to Motivio ✨</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#FFD700;'>Your Daily Dose of Motivation</h3>", unsafe_allow_html=True)
    
    quotes = [
        "Believe in yourself!",
        "Every day is a second chance.",
        "Stay positive, work hard, make it happen.",
        "Dream big and dare to fail.",
        "You are stronger than you think.",
    ]
    
    st.markdown("<h2 style='color:#FFD700;'>💡 Today's Motivation:</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:20px; color:white;'>{random.choice(quotes)}</p>", unsafe_allow_html=True)
    
    if st.button("Give Me Another!"):
        st.markdown(f"<p style='font-size:20px; color:white;'>{random.choice(quotes)}</p>", unsafe_allow_html=True)
    
    challenges = [
        "Write down 3 things you are grateful for today.",
        "Take a 10-minute walk and clear your mind.",
        "Compliment someone today.",
        "Learn one new thing today."
    ]
    
    if st.button("Show Me Today's Challenge"):
        challenge = random.choice(challenges)
        st.markdown(
            f'<div style="background-color: rgba(0,0,0,0.6); padding:15px; border-radius:10px; color:#FFD700; font-size:20px;">🎯 {challenge}</div>',
            unsafe_allow_html=True
        )

# ------------------------
# Categories Page
# ------------------------
elif st.session_state.page == "categories":
    st.title("Motivio - Categories 💫")
    
    categories = {
        "Success": [
            "Success is not final, failure is not fatal.",
            "The harder you work, the luckier you get."
        ],
        "Happiness": [
            "Happiness is not something ready made. It comes from your actions.",
            "Enjoy the little things."
        ],
        "Productivity": [
            "Do something today that your future self will thank you for.",
            "Focus on being productive instead of busy."
        ]
    }
    
    choice = st.selectbox("Choose your category:", ["Success", "Happiness", "Productivity"])
    st.markdown(f"<p style='font-size:20px; color:#FFD700;'>💫 {random.choice(categories[choice])}</p>", unsafe_allow_html=True)

# ------------------------
# About Page
# ------------------------
elif st.session_state.page == "about":
    st.title("About Motivio 📝")
    st.markdown("""
    <p style='font-size:18px; color:#FFD700;'>
    Motivio is your daily companion for positivity and inspiration.  
    <br><br>
    Features:
    <ul>
    <li>Daily motivational quotes</li>
    <li>Choose motivation by category</li>
    <li>Daily challenges to boost productivity and happiness</li>
    </ul>
    Stay motivated every day! ✨
    </p>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    /* Full-screen inspiring background with soft overlay */
    .stApp {
        background: linear-gradient(rgba(255,255,255,0.15), rgba(255,255,255,0.15)),
                    url("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1470&q=80");
        background-size: cover;
        background-attachment: fixed;
        color: white;
        font-family: 'Arial', sans-serif;
    }

    /* Button style: bright, modern */
    .stButton>button {
        background: linear-gradient(90deg, #ff7e5f, #feb47b);
        color: white;
        height: 3em;
        width: 200px;
        border-radius: 12px;
        border: none;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        margin: 5px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #feb47b, #ff7e5f);
        transform: scale(1.05);
    }

    /* Quote / challenge boxes */
    .quote-box {
        background-color: rgba(255, 255, 255, 0.2);
        padding: 15px;
        border-radius: 12px;
        color: #FFD700;
        font-size: 20px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("About Motivio 📝")

st.markdown("""
<p style='font-size:18px; color:#FFD700;'>
Welcome to <strong>Motivio</strong> — your daily source of inspiration and positivity!  
<br><br>
This website was thoughtfully created by <strong>Samarth Agrawal</strong> with a simple but powerful mission:  
to help people stay motivated, embrace positivity, and take small daily actions that can transform their lives.  
<br><br>
Whether you’re seeking a boost to kickstart your day, guidance to stay productive, or just a spark of encouragement, Motivio is here to brighten your journey. ✨
</p>
""", unsafe_allow_html=True)
