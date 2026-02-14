
import streamlit as st
from google import genai
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Explore with AI",
    page_icon="✈️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---------------- GOOGLE GEMINI API ----------------
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except (FileNotFoundError, KeyError):
    api_key = os.environ.get("GOOGLE_API_KEY")

    
if not api_key:
    st.error("Missing Google API Key! Please set it in .streamlit/secrets.toml or as an environment variable.")
    st.stop()

client = genai.Client(api_key=api_key)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
    }
    h1, h2, h3 {
        color: #ffffff !important;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    .stTextInput > div > div > input, .stNumberInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 10px;
    }
    .stTextInput > label, .stNumberInput > label {
        color: #e0e0e0 !important;
    }
    .stButton > button {
        background: linear-gradient(45deg, #FF512F 0%, #DD2476 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 50px;
        font-weight: bold;
        width: 100%;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .result-card {
        background: rgba(255, 255, 255, 0.95);
        color: #333333;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        margin-top: 2rem;
        margin-bottom: 2rem;
    }
    .result-card p, .result-card li {
        color: #444;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
# Project Title: Explore with AI: Custom Itineraries for Your Next Journey
# Team ID: LTVIP2026TMIDS91327

col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/201/201623.png", width=80) 
with col2:
    st.title("Explore with AI")
    st.markdown("*Custom Itineraries for Your Next Journey*")

st.markdown("---")

# ---------------- INPUT FORM ----------------
with st.container():
    destination = st.text_input("🌍 Where is your dream destination?", placeholder="e.g., Kyoto, Japan")
    
    col1, col2 = st.columns(2)
    with col1:
        days = st.number_input("☀️ Duration (Days)", min_value=1, value=5, step=1)
    with col2:
        nights = st.number_input("🌙 Duration (Nights)", min_value=0, value=4, step=1)

    interests = st.multiselect(
        "✨ Specific Interests (Optional)",
        ["Food & Dining", "History & Culture", "Nature & Hiking", "Museums", "Shopping", "Nightlife", "Relaxation"],
        default=[]
    )

# ---------------- GENERATION LOGIC ----------------
if st.button("🚀 Plan My Adventure"):
    if not destination.strip():
        st.warning("Please enter a destination to start!")
    else:
        with st.spinner("Preparing your itinerary... packing virtual bags... 🧳"):
            
            interest_str = ", ".join(interests) if interests else "General sightseeing"
            
            prompt = f"""
            Act as an expert travel guide. Create a structured, engaging travel itinerary for a trip to **{destination}**.
            
            **Trip Details:**
            - Duration: {days} Days, {nights} Nights
            - Interests: {interest_str}
            
            **Desired Format:**
            1. **Trip Title**: Catchy and exciting.
            2. **Overview**: A brief summary of what to expect.
            3. **Day-by-Day Plan**:
               - **Morning**: Activity + recommended breakfast spot type.
               - **Afternoon**: Main attraction + lunch idea.
               - **Evening**: Night activity + dinner recommendation.
            4. **Pro Tips**: Local customs, transport advice, or hidden gems.
            
            Keep the tone enthusiastic and helpful. Use emojis. Format with clean Markdown.
            """

            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                
                result_text = response.text

                # Display Result
                st.markdown(f"""
                <div class="result-card">
                    {result_text.replace(chr(10), '<br>')} 
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Oops! Something went wrong: {str(e)}")
