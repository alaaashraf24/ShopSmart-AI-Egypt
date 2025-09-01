# src/shopping_tasks.py

from crewai import Task

class ShoppingTasks:
    """
    This class defines the tasks for the shopping crew. Each task is associated
    with an agent and has a specific description and expected output. The tasks
    are designed to be sequential, with the output of one task feeding into the next.
    """
    def search_task(self, agent, user_query):
        return Task(
            description=f"""
                Conduct a thorough search for products that match the user's query: '{user_query}'.
                Focus your search exclusively on these websites: Amazon.eg, Jumia.com.eg, and Noon.com.
                Your final answer must be a list of URLs from these websites for the most promising products.
                Do not include any other text or explanation in your output.
            """,
            expected_output="A list of URLs for relevant products.",
            agent=agent,
        )

    def analysis_task(self, agent, context):
        return Task(
            description="""
                For each URL provided, scrape the website to analyze its content.
                Extract key product details such as name, price, key features, and specifications.
                Compare the products and identify the single best option based on value and features.
                Your final answer must be the URL of this single best product.
            """,
            expected_output="The URL of the single best product.",
            agent=agent,
            context=[context],
        )

    def review_analysis_task(self, agent, context):
        return Task(
            description="""
                Scrape the website of the provided best product URL to find and analyze customer reviews.
                Summarize the overall sentiment and identify the most frequently mentioned pros and cons.
                Your final answer must be a bullet-point list of 3-5 pros and 3-5 cons.
            """,
            expected_output="A bullet-point list summarizing pros and cons.",
            agent=agent,
            context=[context],
        )

    def recommendation_task(self, agent, context_list):
        return Task(
            description="""
                Based on the comprehensive analysis of the product's features, price, and customer reviews,
                craft a final recommendation for the user.
                The recommendation should be engaging and persuasive, clearly stating why this product is the best choice.
                Include the product name, a summary of its benefits, the summarized pros and cons, and the final purchase URL.
            """,
            expected_output="A final, well-structured product recommendation.",
            agent=agent,
            context=context_list,
        )