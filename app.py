# app.py

import streamlit as st
from dotenv import load_dotenv
import os

from crewai import Crew, Process

from src.shopping_agents import ShoppingAgents
from src.shopping_tasks import ShoppingTasks

# Load environment variables for local development
load_dotenv()

# Set Streamlit page configuration
st.set_page_config(page_title="ShopSmart AI", page_icon="🛍️", layout="wide")

# Page header
st.title("🛍️ ShopSmart AI: Your Shopping Assistant for Egypt")
st.markdown("""
<style>
    .stApp {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

st.header("Find the Best Products on Amazon.eg, Jumia & Noon")

# Check for API keys and display a warning if not found
if not os.environ.get("GOOGLE_API_KEY") or not os.environ.get("TAVILY_API_KEY"):
    st.error("🚨 API keys for Google and Tavily are not set. Please add them to your .env file or Streamlit secrets.")
else:
    # User input form
    with st.form("shopping_form"):
        user_query = st.text_input("What product are you looking for? (e.g., 'best budget smartphone with a good camera under 5000 EGP')", key="user_query")
        submit_button = st.form_submit_button("Find Best Deal")

    if submit_button and user_query:
        with st.spinner('🤖 The AI crew is on the job... Please wait...'):
            try:
                # Initialize agents and tasks
                agents = ShoppingAgents()
                tasks = ShoppingTasks()

                # Instantiate agents
                search_agent = agents.product_search_agent()
                analyst_agent = agents.product_analyst_agent()
                review_agent = agents.review_analyzer_agent()
                recommendation_agent = agents.recommendation_agent()

                # Instantiate tasks
                search_task = tasks.search_task(search_agent, user_query)
                analysis_task = tasks.analysis_task(analyst_agent, search_task)
                review_task = tasks.review_analysis_task(review_agent, analysis_task)
                recommendation_task = tasks.recommendation_task(
                    recommendation_agent, [search_task, analysis_task, review_task]
                )

                # Form the crew
                shopping_crew = Crew(
                    agents=[search_agent, analyst_agent, review_agent, recommendation_agent],
                    tasks=[search_task, analysis_task, review_task, recommendation_task],
                    process=Process.sequential,
                    verbose=True
                )

                # Kick off the crew's work
                result = shopping_crew.kickoff()

                # Display the result
                st.subheader("Here's Your Product Recommendation:")
                st.markdown(result, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.info("Please try rephrasing your query or check your API key quotas.")

# Sidebar with additional information
st.sidebar.title("About ShopSmart AI")
st.sidebar.info(
    "This application uses a multi-agent system powered by CrewAI and Google's Gemini model "
    "to provide intelligent shopping recommendations. It's designed as a portfolio project "
    "to showcase advanced AI engineering skills."
)
st.sidebar.markdown("---")
st.sidebar.subheader("How It Works")
st.sidebar.markdown("""
- **Search Specialist**: Finds products on Amazon.eg, Jumia, and Noon.
- **Product Analyst**: Compares features and prices to find the best option.
- **Review Analyzer**: Summarizes customer feedback into pros and cons.
- **Recommendation Expert**: Delivers the final, data-driven recommendation.
""")