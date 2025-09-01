# src/shopping_tasks.py

from crewai import Task

class ShoppingTasks:
    """
    Defines the tasks for the shopping crew.
    Each task is tied to one agent and designed to run sequentially,
    with the output of one feeding into the next.
    """

    def search_task(self, agent, user_query: str):
        return Task(
            description=f"""
                Use the **Tavily Search Tool** to conduct a thorough search for products
                matching the user's query: '{user_query}'.

                ✅ Focus exclusively on these websites:
                   - Amazon.eg
                   - Jumia.com.eg
                   - Noon.com

                ✅ Return only direct product URLs, not ads or unrelated links.
                ❌ Do not include explanations or commentary.
            """,
            expected_output="A clean list of valid product URLs from Amazon.eg, Jumia.com.eg, or Noon.com.",
            agent=agent,
        )

    def analysis_task(self, agent, context):
        return Task(
            description="""
                For each URL provided by the search task, use the **ScrapeWebsiteTool** to extract:
                  - Product name
                  - Price
                  - Key features and specifications

                Then:
                  - Compare all the products
                  - Select the single best product based on **value-for-money** and **features**
                  - Return only that product's URL
            """,
            expected_output="The single best product's URL (only the URL, no extra text).",
            agent=agent,
            context=[context],
        )

    def review_analysis_task(self, agent, context):
        return Task(
            description="""
                Use the **ScrapeWebsiteTool** on the chosen product page to analyze **customer reviews**.

                Summarize into:
                  - 3 to 5 Pros
                  - 3 to 5 Cons

                Make sure the summary is concise and bullet-point formatted.
            """,
            expected_output="A bullet-point list of 3-5 pros and 3-5 cons.",
            agent=agent,
            context=[context],
        )

    def recommendation_task(self, agent, context_list):
        return Task(
            description="""
                Synthesize all the findings (URLs, analysis, and customer reviews)
                to craft a **final product recommendation**.

                Format the output as **Markdown** for display in Streamlit.
                It must include:

                ## 🏆 Final Recommendation

                **Product Name**: <insert name here>

                ### ✅ Why We Recommend This
                - Short summary of the product's main benefits

                ### 👍 Pros
                - Bullet-point list of pros

                ### 👎 Cons
                - Bullet-point list of cons

                ### 🔗 Purchase Link
                [Buy Now](<product URL>)

                Keep the output clean, structured, and easy to read.
            """,
            expected_output="A Markdown-formatted product recommendation with headers, bold text, bullet lists, and a purchase link.",
            agent=agent,
            context=context_list,
        )
