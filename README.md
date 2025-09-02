# 🛍️ ShopSmart Multi-Agent AI

[![Streamlit](https://img.shields.io/badge/Deployed%20on-Streamlit%20Cloud-brightgreen?logo=streamlit)]  
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python)](https://www.python.org/)  
[![CrewAI](https://img.shields.io/badge/AI%20Framework-CrewAI-purple)](https://github.com/joaomdmoura/crewAI)  

**ShopSmart Multi-Agent AI** is an intelligent shopping assistant built with **CrewAI**, **Google Gemini (Generative AI)**, and **multi-agent orchestration**.  
It helps users in **Egypt** find the **best products across Amazon.eg, Jumia, and Noon** by:  

- 🔎 Searching e-commerce platforms  
- 📊 Comparing features and pricing  
- 💬 Analyzing customer reviews  
- 🏆 Delivering a **final AI-driven recommendation**  

🚀 The project is fully deployed on **Streamlit Cloud**.  

---

## ✨ Features  

- **Multi-Agent Architecture** powered by [CrewAI](https://github.com/joaomdmoura/crewAI):  
  - 🔎 *Search Specialist*: Finds relevant product listings  
  - 📊 *Product Analyst*: Compares features & pricing  
  - 💬 *Review Synthesizer*: Summarizes customer feedback  
  - 🏆 *Recommendation Expert*: Provides the final purchase recommendation  

- **Real-Time Data Sources**  
  - Product listings from **Amazon.eg**, **Jumia**, and **Noon**  
  - Web search integration via **Tavily API**  
  - On-page scraping with **CrewAI Tools**  

- **Generative AI (LLM)**  
  - Powered by **Google Gemini** (`gemini-2.0-flash`)  
  - Used for reasoning, summarization, and recommendation generation  

- **Deployed Application**  
  - Fully interactive **Streamlit UI**  
  - Secure environment with `.env` and Streamlit Secrets  

---

## 🖼️ Demo  

### 🔍 Example Query  
> *"Best budget smartphone with a good camera under 5000 EGP"*  

### ✅ AI Workflow  
1. Search → 2. Analyze → 3. Summarize Reviews → 4. Recommend  

### 📊 Example Output  
```markdown
## 🏆 Final Recommendation  

**Product Name**: XYZ Budget Smartphone  

### ✅ Why We Recommend This  
- Affordable price with excellent camera performance  

### 👍 Pros  
- Great low-light photography  
- Long battery life  
- Affordable under 5000 EGP  

### 👎 Cons  
- Limited storage  
- Average display brightness  

### 🔗 Purchase Link  
[Buy Now](https://jumia.com.eg/xyz-smartphone)
````

---

## 🏗️ Project Structure

```
ShopSmart-MultiAgent-AI/
│── app.py                 # Streamlit app entrypoint
│── requirements.txt       # Dependencies
│── src/
│   ├── shopping_agents.py # Defines CrewAI agents
│   ├── shopping_tasks.py  # Defines CrewAI tasks
│── .env.example           # API keys template
│── README.md              # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/alaaashraf24/ShopSmart-MultiAgent-AI.git
cd ShopSmart-MultiAgent-AI
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure API Keys

Create a `.env` file (or use Streamlit Secrets):

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 5️⃣ Run the App Locally

```bash
streamlit run app.py
```

---

## 🌐 Deployment

This project is deployed on **Streamlit Cloud**:
🔗 [Live Demo](https://shopsmart-ai-egypt-fhebc9k7udyy4qup6qwbor.streamlit.app/)

---

## 🛠️ Tech Stack

* **Python 3.10+**
* [Streamlit](https://streamlit.io/) – Web UI
* [CrewAI](https://github.com/joaomdmoura/crewAI) – Multi-agent orchestration
* [LangChain Google GenAI](https://pypi.org/project/langchain-google-genai/) – Gemini LLM integration
* [Tavily API](https://www.tavily.com/) – Web search engine
* [CrewAI Tools](https://github.com/joaomdmoura/crewAI-tools) – Web scraping utilities

---

## 📌 Key Learnings & Highlights

* Designed a **multi-agent AI pipeline** with CrewAI (Agents + Tasks + Orchestration)
* Integrated **Google Gemini LLM** for structured reasoning & natural language generation
* Used **Tavily API** for web search and **ScrapeWebsiteTool** for extracting product data
* Deployed a **production-ready AI assistant** on Streamlit Cloud
* Applied **prompt engineering** and **LLM chaining** for reliable structured outputs

---

## 📄 License

This project is licensed under the MIT License.

---
this full version in your portfolio?
```
