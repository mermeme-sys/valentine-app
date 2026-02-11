import streamlit as st
import time

# Page configuration
st.set_page_config(page_title="A Message For You", page_icon="🤍")

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #87CEEB 0%, #FFFACD 100%);
    }
    .heart {
        color: #ff4b4b;
        font-size: 100px;
        text-align: center;
    }
    .big-x {
        color: #d32f2f;
        font-size: 150px;
        text-align: center;
        font-weight: bold;
        animation: pulse 0.5s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    .big-text {
        font-family: 'Helvetica';
        color: #333;
        text-align: center;
    }
    .letter-box {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 30px;
        border-radius: 15px;
        border: 2px solid #ffb6c1;
        font-size: 18px;
        line-height: 1.6;
        color: #444;
    }
    </style>
    """, unsafe_allow_html=True)

# Session State to handle the flow
if 'step' not in st.session_state:
    st.session_state.step = 'start'

# --- STEP 1: INITIAL QUESTION ---
if st.session_state.step == 'start':
    st.markdown("<h1 class='big-text'>I have a question for you...</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Accept", use_container_width=True):
            st.session_state.step = 'ask'
            st.rerun()
            
    with col2:
        if st.button("Decline", use_container_width=True):
            # Show the big X
            st.markdown("<div class='big-x'>❌</div>", unsafe_allow_html=True)
            st.error("Wrong answer! Try again. 😉")
            # Brief pause so they see the X before the page refreshes/updates
            time.sleep(1.5)
            st.rerun()

# --- STEP 2: THE PROPOSAL ---
elif st.session_state.step == 'ask':
    st.markdown("<h1 class='big-text'>Will you be my Valentine?</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes", key="yes1", use_container_width=True):
            st.session_state.step = 'final'
            st.rerun()
    with col2:
        # Both buttons are 'Yes' anyway, sneaky!
        if st.button("Yes", key="yes2", use_container_width=True):
            st.session_state.step = 'final'
            st.rerun()

# --- STEP 3: THE CELEBRATION ---
elif st.session_state.step == 'final':
    st.balloons()
    st.markdown("<div class='heart'>❤️</div>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #ff1493;'>YAYYYY!!!!</h1>", unsafe_allow_html=True)
    
     # The Letter
    st.markdown(f"""
    <div class='letter-box'>
        <strong>To my favorite person, Happy Valentine’s Day, my love 🤍</strong><br><br>
        Today makes me think about just how much you mean to me and how lucky I am to have you in my life. 
        You are my heart, my safe place, my peace, my home even when we’re apart. Every day with you is 
        a gift I never take for granted. The love you give me, your kindness, your patience, your smile 
        it all fills me up in ways I can’t even put into words.<br><br>
        Even with the distance, my love for you only grows stronger. I carry you in every thought, every plan, 
        every hope for the future. I think about our moments together, our laughter, our hugs, our late-night 
        talks, and even our quiet moments just being close. They remind me of why you’re my person, my other 
        half, my forever.<br><br>
        I love everything about you the way you care so deeply, the way your presence calms me, the way 
        you make me feel loved even when life gets hard. I love imagining our future together, building a 
        home filled with love, warmth, and happiness. I dream about waking up next to you, holding you in 
        my arms, and never having to say goodbye. I want to make every day feel special for you, because 
        you make every day special for me just by being you.<br><br>
        This Valentine’s Day, I want you to know that no matter the distance, no matter the challenges, 
        my heart is always yours. I choose you every single day, and I’ll keep choosing you for the rest 
        of my life. You are my love, my home, my peace, and my joy. I can’t wait for all the adventures 
        we’ll share, all the quiet moments we’ll treasure, and all the love we’ll continue to build together.<br><br>
        Happy Valentine’s Day, my forever love. I love you more than words could ever explain, and I 
        will love you more every single day 🤍💗<br><br>
        <strong>I LOVE YOU MY SWEET GIRL</strong>
    </div>
    """, unsafe_allow_html=True)
