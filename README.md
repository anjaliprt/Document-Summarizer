# 📝 RAG DOCUMENT SUMMARIZER

This project is a simple **Text Summarizer App** using **LangChain**, **FAISS**, **HuggingFace embeddings**, and **Groq LLM** in a RAG (Retrieval-Augmented Generation) setup.  
It uses **LangChain** for document loading and splitting, and **Streamlit** for the UI.

---

## 🚀 Features
- Upload **PDF or TXT files** via the sidebar.
- Enter custom queries for summarization.
- Summaries are generated using a **RAG chain**, combining document embeddings with a Groq LLM.
- Clean, interactive **Streamlit interface**.

---

## 🔑 Requirements
- Python 3.9+
- GROQ API token 

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```
## ⚙️ Installation

- Clone this repository or copy the project files.
- Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate   # Windows
```
- Install dependencies:

```
pip install -r requirements.txt
```
  
## ▶️ Running the App
Run Streamlit UI:  

```
streamlit run streamlit_app.py
```

## 📖 Usage

Upload your PDF or TXT document using the sidebar.

Enter your summarization query (default focuses on definitions and examples).

Click "Generate Summary" to view the result on the main area.

## 🛠 Tech Stack

LangChain
 – document loading & text splitting

Transformers
 – summarization model

Streamlit
 – user interface

dotenv
 – environment variables

