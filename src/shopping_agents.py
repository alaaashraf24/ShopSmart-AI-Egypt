# src/shopping_agents.py

import os
from crewai import Agent
from crewai_tools import BaseTool, ScrapeWebsiteTool
from tavily import TavilyClient
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API keys from environment
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

# Validate API keys
if not GOOGLE_API_KEY:
    raise ValueError("❌ Missing GOOGLE_API_KEY. Please set it in Streamlit secrets or environment.")
if not TAVILY_API_KEY:
    raise ValueError("❌ Missing TAVILY_API_KEY. Please set it in Streamlit secrets or environment.")

# Initialize the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    verbose=True,
    temperature=0.2,
    google_api_key=GOOGLE_API_KEY,
)

# Initialize Tavily client
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)


# ---- Helper: Convert numeric ratings to stars ----
def rating_to_stars(rating_str: str) -> str:
    try:
        if not rating_str or "Not Available" in rating_str:
            return "No rating ⭐"
        numeric = float(rating_str.split("/")[0].strip())
        full_stars = int(numeric)
        half_star = 1 if numeric - full_stars >= 0.5 else 0
        return "⭐" * full_stars + ("✰" if half_star else "")
    except Exception:
        return "No rating ⭐"


# ---- Tavily Tool (structured output) ----
class TavilySearchTool(BaseTool):
    name: str = "Tavily Search Tool"
    description: str = (
        "Searches the web using Tavily API for products. "
        "Always return product_name, price, rating, and link."
    )

    def _run(self, query: str):
        """Perform a search and return structured product results."""
        results = tavily_client.search(query)
        structured = []
        for r in results.get("results", []):
            structured.append({
                "product_name": r.get("title", "No title"),
                "price": r.get("price", "Not Available"),
                "rating": r.get("rating", "Not Available"),
                "link": r.get("url", ""),
            })
        return structured if structured else [{"product_name": "No results found"}]


# Initialize tools
tavily_tool = TavilySearchTool()
scrape_tool = ScrapeWebsiteTool()


# ---- Shopping Agents ----
class ShoppingAgents:
    def product_search_agent(self):
        return Agent(
            role="E-commerce Search Specialist for Egypt",
            goal="""Find the most relevant product listings on Amazon.eg, Jumia, and Noon
                 based on a user's detailed query. The output must be a structured JSON list
                 with product_name, price, rating, and link.""",
            backstory="""An expert in navigating Egyptian e-commerce platforms. You specialize in
                      extracting structured product information that is reliable and accurate.""",
            tools=[tavily_tool],
            llm=llm,
            verbose=True,
            allow_delegation=False,
        )

    def product_analyst_agent(self):
        return Agent(
            role="Product Features and Pricing Analyst",
            goal="""Analyze the structured product listings and ensure that price and rating
                 fields are correctly parsed. Normalize missing values to 'Not Available'.
                 Return a cleaned JSON list with product_name, price, rating, and link.""",
            backstory="""A meticulous analyst with a sharp eye for detail. You ensure structured
                      product data is consistent and usable for recommendation.""",
            tools=[scrape_tool],
            llm=llm,
            verbose=True,
            allow_delegation=False,
        )

    def review_analyzer_agent(self):
        return Agent(
            role="Customer Review Synthesizer",
            goal="""Scrape and analyze customer reviews for the single best product identified
                 by the analyst. Summarize the findings into a list of pros and cons.""",
            backstory="""An expert in sentiment analysis and text summarization. You distill
                      reviews into clear pros and cons for better decision-making.""",
            tools=[scrape_tool],
            llm=llm,
            verbose=True,
            allow_delegation=False,
        )

    def recommendation_agent(self):
        return Agent(
            role="Shopping Recommendation Expert",
            goal="""Synthesize all gathered information (features, price, rating, and reviews)
                 into a polished Markdown recommendation. Show product name, price, star rating,
                 pros, cons, and a direct purchase link.""",
            backstory="""A trusted shopping advisor who presents recommendations in a clear,
                      concise, and user-friendly way.""",
            instructions=f"""Format the final output like this:

## 🏆 Final Recommendation

**Product Name**: <product_name>  
💰 **Price**: <price>  
⭐ **Rating**: {{rating_to_stars('<rating>')}} (<rating>)

### ✅ Why We Recommend This
<one short paragraph>

### 👍 Pros
- <pros>

### 👎 Cons
- <cons>

### 🔗 Purchase Link
[Buy Now](<link>)
""",
            tools=[],
            llm=llm,
            verbose=True,
            allow_delegation=False,
        )
