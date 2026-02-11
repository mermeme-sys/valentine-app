import streamlit as st
import time

# Set page config for a romantic feel
st.set_page_config(page_title="A Special Message", page_icon="❤️")

# Custom CSS to make it pretty
st.markdown("""
    <style>
    .main {
        background-color: #fff5f5;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 20px;
        padding: 10px 25px;
    }
    </style>
    """, unsafe_allow_html=True)

if 'answer' not in st.session_state:
    st.session_state.answer = False

# --- STEP 1: The Question ---
if not st.session_state.answer:
    st.title("💌 I have a question for you...")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes! 🥰"):
            st.session_state.answer = True
            st.rerun()
    with col2:
        # A little joke: the 'No' button moves or just doesn't work
        if st.button("No 😢"):
            st.warning("Error: This button is broken. Try the other one!")

# --- STEP 2: The Explosion & Paragraph ---
else:
    # Exploding effect (using balloons as a built-in "explosion")
    st.balloons()
    st.snow() # Looks like petals/magic
    
    st.header("YAY! ❤️")
    
    # The Exploding Heart (using an Emoji or Image)
    st.markdown("<h1 style='text-align: center; font-size: 100px;'>💥❤️🌸</h1>", unsafe_allow_html=True)
    
    # Your Paragraph
    st.write("---")
    st.subheader("To my favorite person,")
    st.write("""
        Insert your heartfelt paragraph here. You can talk about your 
        favorite memories, why you love her, and how much she means to you.
        
        Flowers for you: 🌹🌷🌻🌼🌹
    """)
    st.write("---")