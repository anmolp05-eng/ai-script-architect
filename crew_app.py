import streamlit as st
from google import genai

# 1. Page Configuration
st.set_page_config(page_title="AI Multi-Agent Campaign Architect", page_icon="🤝", layout="centered")

st.title("🤝 Multi-Agent Influencer Brief & Contract Generator")
st.subheader("Orchestrate an AI team to automate brand-to-creator onboarding workflows")

# 2. Sidebar Setup
st.sidebar.header("🔑 Setup & Configuration")
st.sidebar.markdown("[Get a free Gemini API Key here](https://aistudio.google.com/)")
api_key = st.sidebar.text_input("Enter your Google Gemini API Key:", type="password")

brand_name = st.text_input("Brand Name:", placeholder="e.g., Star Vision Events")
campaign_goals = st.text_area("What are the campaign goals?", placeholder="e.g., Launching a regional lifestyle experience targeting Gen-Z foodies in Dubai.")
budget_tier = st.selectbox("Campaign Budget Tier:", ["Micro (Barter/Low Budget)", "Mid-Tier (Macro-Influencers)", "Premium (Celebrity/Bollywood Talent)"])

# 3. Custom Multi-Agent Assembly Line Logic
if st.button("🚀 Deploy AI Crew"):
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar.")
    elif not brand_name or not campaign_goals:
        st.warning("Please fill in the Brand Name and Campaign Goals.")
    else:
        # Progress placeholders to show the user the agents are talking
        status_box = st.empty()
        
        try:
            # Initialize Google GenAI client
            client = genai.Client(api_key=api_key)
            
            # --- AGENT 1: THE CAMPAIGN STRATEGIST ---
            status_box.info("🧠 Agent 1 (Senior Campaign Strategist) is analyzing market fit...")
            
            prompt_strategist = f"""
            You are a Senior Influencer Campaign Strategist with 10+ years of experience launching viral marketing activations across India and the GCC.
            Analyze the following campaign goals for the brand '{brand_name}' with a budget tier of '{budget_tier}'.
            Goals: {campaign_goals}
            
            Output 3 high-impact content pillars and define the ideal creator archetypes. Keep your output concise and structured.
            """
            
            response_strategy = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt_strategist,
            )
            strategy_output = response_strategy.text
            
            # --- AGENT 2: THE CREATIVE DIRECTOR ---
            status_box.info("🎨 Agent 2 (Creative Director) is writing the Influencer Brief...")
            
            prompt_creative = f"""
            You are a Creative Content Director. You specialize in turning abstract brand strategies into highly actionable creator briefs.
            Review the following strategy developed by your Strategist teammate:
            
            {strategy_output}
            
            Based entirely on this strategy, draft a professional Influencer Creative Brief containing:
            1. Visual Constraints & Aesthetic Direction
            2. Content Do's & Don'ts
            3. Audio/Pacing Benchmarks
            """
            
            response_brief = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt_creative,
            )
            brief_output = response_brief.text

            # --- AGENT 3: THE LEGAL COUNSEL ---
            status_box.info("⚖️ Agent 3 (Legal & Compliance Advisor) is drafting contract clauses...")
            
            prompt_legal = f"""
            You are an Influencer Legal & Compliance Advisor. You ensure brand protection and clear deliverables.
            Review the final Creative Brief drafted by your teammate:
            
            {brief_output}
            
            For a budget tier of '{budget_tier}', draft a compliance framework sheet containing:
            1. Mandatory Timeline Milestones (Draft due date, posting windows)
            2. Content Usage Rights & Exclusivity terms
            3. Regulatory Disclosure requirements (e.g., #Ad guidelines for India/GCC)
            """
            
            response_legal = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt_legal,
            )
            legal_output = response_legal.text
            
            # --- DISPLAY THE COLLABORATION OUTPUT ---
            status_box.success("✨ Campaign Pipeline Assembly Complete!")
            
            st.markdown("## 📋 Pipeline Results")
            
            with st.expander("🧠 View Strategy (Agent 1)"):
                st.markdown(strategy_output)
                
            with st.expander("🎨 View Creative Brief (Agent 2)"):
                st.markdown(brief_output)
                
            with st.expander("⚖️ View Legal Framework (Agent 3)"):
                st.markdown(legal_output)
                
        except Exception as e:
            status_box.empty()
            st.error(f"An execution error occurred: {e}")