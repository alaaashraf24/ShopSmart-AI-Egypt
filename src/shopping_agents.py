# src/shopping_agents.py

from crewai import Agent
from crewai_tools.tools import ScrapeWebsiteTool, TavilySearchResults
from langchain_google_generativeai import ChatGoogleGenerativeAI
import os

# Initialize the LLM
# Ensure you have your GOOGLE_API_KEY in your environment
llm = ChatGoogleGenerativeAI(model="gemini-pro", verbose=True, temperature=0.2, google_api_key=os.environ.get("GOOGLE_API_KEY"))

# Initialize tools
tavily_tool = TavilySearchResults()
scrape_tool = ScrapeWebsiteTool()

class ShoppingAgents:
    """
    This class defines the agents that will be part of the shopping crew.
    Each agent has a specific role, goal, and backstory, along with tools
    it can use to perform its tasks.
    """
    def product_search_agent(self):
        return Agent(
            role="E-commerce Search Specialist for Egypt",
            goal="""Find the most relevant product listings on Amazon.eg, Jumia, and Noon
                 based on a user's detailed query. The output should be a list of URLs.""",
            backstory="""An expert in navigating the complexities of Egyptian e-commerce platforms.
                      You are skilled at using advanced search techniques to uncover the best product
                      options available, focusing exclusively on Amazon.eg, Jumia, and Noon.""",
            tools=[tavily_tool],
            llm=llm,
            verbose=True,
            allow_delegation=False,
        )

    def product_analyst_agent(self):
        return Agent(
            role="Product Features and Pricing Analyst",
            goal="""Analyze the product listings from the provided URLs to extract key features,
                 specifications, and pricing information. Select the single best product based on
                 this analysis and provide its URL.""",
            backstory="""A meticulous analyst with a sharp eye for detail. You excel at comparing
                      products, identifying the best value for money, and understanding what
                      features matter most to consumers. Your analysis is data-driven and objective.""",
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
            backstory="""An expert in sentiment analysis and text summarization. You can quickly
                      read through hundreds of reviews to distill the most important points,
                      highlighting common praises and complaints to give a clear picture of
                      customer satisfaction.""",
            tools=[scrape_tool],
            llm=llm,
            verbose=True,
            allow_delegation=False,
        )

    def recommendation_agent(self):
        return Agent(
            role="Shopping Recommendation Expert",
            goal="""Synthesize all the gathered information (product features, pricing, and
                 customer reviews) to provide a final, comprehensive recommendation to the user.
                 The recommendation should be clear, concise, and include a direct link to the
                 product page.""",
            backstory="""A trusted shopping advisor who combines analytical insights with an
                      understanding of user needs. You provide clear, actionable recommendations
                      that help users make confident purchasing decisions. Your final output is
                      the culmination of the team's entire effort.""",
            llm=llm,
            verbose=True,
            allow_delegation=False,
        )