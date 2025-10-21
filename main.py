def generate_summary(file_path, query):
    import os 
    from dotenv import load_dotenv
    from langchain_community.document_loaders import PyPDFLoader, TextLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain_community.vectorstores import FAISS
    from langchain.prompts import ChatPromptTemplate
    from langchain_groq import ChatGroq

    load_dotenv() 
    
    groq_api_key = os.getenv("GROQ_API_KEY")

    # Load document
    if str(file_path).endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path)
    documents = loader.load()

    # Split
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(documents)

    # Embeddings & FAISS
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    retriever = vectorstore.as_retriever()

    # Prompt
    prompt = ChatPromptTemplate.from_template("""
    You are a helpful AI summarizer.
    Summarize the following text focusing on **definitions, examples, and key insights.**

    Context:
    {context}

    Task:
    Summarize this text concisely.
    """)

    # LLM
    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.3)

    # RAG chain
    def format_docs(docs):
        return "\n\n".join([d.page_content for d in docs])
    rag_chain = (
        {"context": retriever | format_docs}
        | prompt
        | llm
    )

    return rag_chain.invoke(query)
