import streamlit as st
from google import genai

# 1. Page Layout Configuration
st.set_page_config(page_title="Promo Copy & Visual Architect", page_icon="🎨", layout="centered")

st.title("🎨 Standalone Promotional Copy & Visual Generator")
st.subheader("Generate multi-platform campaign assets and structured visual prompts instantly")

# 2. Configuration Sidebar
st.sidebar.header("🔑 Setup & Configuration")
st.sidebar.markdown("[Get a free Gemini API Key here](https://aistudio.google.com/)")
api_key = st.sidebar.text_input("Enter your Google Gemini API Key:", type="password")

# 3. Campaign Input Framework
campaign_name = st.text_input("Campaign / Product Name:", placeholder="e.g., The Fusion Thali Box Launch")
platform = st.selectbox("Target Distribution Platform:", ["Instagram Grid/Carousels", "LinkedIn Professional", "TikTok Promo Video"])
vibe_style = st.select_slider("Brand Vibe & Tone:", options=["Ultra-Luxury/Premium", "Chic & Aesthetic", "Witty & Viral/Meme-centric"])
product_details = st.text_area("Core Product Selling Points:", placeholder="e.g., Indian fusion street food concept featuring premium packaging designed for fast-casual takeaway and office delivery.")

# 4. Prompt Engineering & Execution Pipeline
if st.button("✨ Architect Campaign Visuals & Copy"):
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar.")
    elif not campaign_name or not product_details:
        st.warning("Please fill in the Campaign Name and Product Details.")
    else:
        with st.spinner("Generating marketing assets and visual prompts..."):
            try:
                # Initialize GenAI Client
                client = genai.Client(api_key=api_key)
                
                # Deep Context Engineering Prompt
                master_prompt = f"""
                You are an Elite Digital Creative Director specializing in high-converting food and lifestyle marketing assets.
                Analyze the following details:
                Product/Campaign: {campaign_name}
                Platform: {platform}
                Tone & Vibe: {vibe_style}
                Core Offering: {product_details}
                
                Output a cohesive, dual-asset campaign kit:
                
                1. PLATFORM-OPTIMIZED COPY:
                Draft a high-converting promotional post tailored specifically to {platform} using the '{vibe_style}' tone. Include an attention-grabbing hook, clear benefit spacing, highly visible CTAs, and a curated hashtag cloud.
                
                2. DATA-OPTIMIZED VISUAL GEN PROMPT (MIDJOURNEY/IMAGEN STYLE):
                Create a detailed, production-grade text-to-image generation prompt. It must enforce hyper-realistic commercial food/lifestyle photography styles, clear lighting directives (e.g., warm overhead studio light, moody dramatic lighting), depth of field, and specific compositional styling instructions matching a high-end ad asset.
                """
                
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=master_prompt,
                )
                
                # Split and structure the output into two clean UI modules
                raw_output = response.text
                
                st.success("🎉 Campaign Assets Built Successfully!")
                st.markdown("---")
                
                # Display Results in organized tabs
                tab1, tab2 = st.tabs(["📝 Promotional Copy", "🖼️ Visual AI Prompt"])
                
                with tab1:
                    st.markdown("### 📋 Copy Matrix")
                    st.write(raw_output.split("2.")[0].replace("1. PLATFORM-OPTIMIZED COPY:", "").strip())
                    
                with tab2:
                    st.markdown("### 🔍 Text-to-Image Engine Configuration")
                    st.info("Copy the optimized prompt below directly into Midjourney, Imagen, or DALL-E 3 for professional ad creatives.")
                    if "2." in raw_output:
                        st.write(raw_output.split("2.")[1].replace("DATA-OPTIMIZED VISUAL GEN PROMPT (MIDJOURNEY/IMAGEN STYLE):", "").strip())
                    else:
                        st.write(raw_output)
                        
            except Exception as e:
                st.error(f"An execution error occurred: {e}")