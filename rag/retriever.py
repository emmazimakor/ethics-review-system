from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_community.vectorstores import Chroma
from prompt_builder import build_prompt

CHROMA_DIR = "chroma_db"
MODEL_NAME = "llama3.2:3b"

embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)
llm = OllamaLLM(model=MODEL_NAME)

def generate_report(proposal_string: str, risk_floor: str) -> str:
    retriever = vectorstore.as_retriever(search_kwargs={"k": 6})
    docs = retriever.get_relevant_documents(proposal_string)
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = build_prompt(proposal_string, context, risk_floor)
    response = llm.invoke(prompt)
    return response
