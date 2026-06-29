import streamlit as st
from google import genai

# 1. Page Configuration
st.set_page_config(page_title="AI Reel Script Architect", page_icon="🎬", layout="centered")

st.title("🎬 AI Short-Form Script Architect (Free Gemini Version)")
st.subheader("Turn raw footage ideas into high-retention Instagram Reels & TikToks")
st.write("Leveraging creator-first frameworks to maximize watch time.")

# 2. Sidebar for API Key & Settings
st.sidebar.header("🔑 Setup & Configuration")
st.sidebar.markdown("[Get a free Gemini API Key here](https://aistudio.google.com/)")
api_key = st.sidebar.text_input("Enter your Google Gemini API Key:", type="password")

genre = st.sidebar.selectbox(
    "Content Genre",
    ["Travel & Wanderlust", "Food & Dining", "Fashion & Lifestyle", "Meme & Viral Marketing"]
)

pacing = st.sidebar.selectbox(
    "Video Pacing & Energy",
    ["Fast-Paced & Energetic (High Cuts)", "Aesthetic & Cinematic (Smooth/Relaxed)", "Direct-to-Camera (Educational/Story)"]
)

# 3. Main Input Form
st.header("📸 Campaign & Footage Details")
raw_footage = st.text_area(
    "Describe your raw clips or the story sequence:",
    placeholder="Example:\nClip 1: Walking into a hidden coffee shop in Dubai.\nClip 2: Close up of matcha latte being poured.\nClip 3: First sip reaction with a smile.",
    height=150
)

target_audience = st.text_input("Target Audience / Brand Vibe:", placeholder="e.g., Gen-Z foodies, luxury travelers, tech enthusiasts")

# 4. AI Script Generation Logic
if st.button("🚀 Synthesize Viral Script"):
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar to run the app.")
    elif not raw_footage:
        st.warning("Please input some raw footage descriptions first!")
    else:
        with st.spinner("Analyzing pacing algorithms and drafting copy..."):
            try:
                # Initialize Google GenAI client with user's key
                client = genai.Client(api_key=api_key)
                
                # Construct the combined instruction prompt
                user_prompt = f"""
                You are an elite short-form video growth engineer and expert content creator.
                Your job is to transform raw video concepts into highly engaging, retention-optimized 
                scripts for Instagram Reels and TikTok. Every script must include a compelling hook, 
                clear visual/audio directions, and an algorithmic call-to-action.
                
                Create a short-form video script based on the following details:
                - **Genre**: {genre}
                - **Pacing Style**: {pacing}
                - **Target Audience**: {target_audience}
                - **Raw Clip Concept**: {raw_footage}
                
                Format your output beautifully using Markdown with these exact sections:
                1. 🔥 **The Hook (0-3s)**: Visual cue, text on screen, and spoken audio.
                2. 📝 **The Core Narrative (3-15s)**: Segment-by-segment visual directions matched with the voiceover.
                3. 📈 **Algorithmic CTA (15-20s)**: High-retention ending phrase.
                4. 💡 **Bonus Strategy**: 3 highly relevant hashtags and a recommended trending audio style.
                """
                
                # Call Gemini API using the fast, cost-effective flash model
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=user_prompt,
                )
                
                # Display Result
                st.success("✨ Script Generated Successfully!")
                st.markdown("---")
                st.markdown(response.text)
                st.markdown("---")
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
