import PyPDF2
import io

import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer

import streamlit as st
import google.generativeai as genai

EMBED_MODEL = "all-MiniLM-L6-v2"

def process_docs(uploaded_files, collection):
    for i, uploaded_file in enumerate(uploaded_files):
        document = extract_text_from_pdf(uploaded_file)
        collection.add(
            documents=[document],
            ids=[f"id{i}"]
        )

def extract_text_from_pdf(pdf):
    raw_content = pdf.read()
    pdf_file = io.BytesIO(raw_content)
    reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()
    return text

def get_prompt(query, retrieving_content):
    if isinstance(retrieving_content, str):
        escaped = retrieving_content.replace("'", "").replace('"', "").replace("\n", " ")
    else:
        escaped = " ".join(retrieving_content).replace("'", "").replace('"', "").replace("\n", " ")
    prompt = ("""Você é um bot prestativo e informativo que responde perguntas usando o texto do trecho de referência incluído abaixo. \
    Certifique-se de responder com uma frase completa, sendo abrangente e incluindo todas as informações de fundo relevantes. \
    No entanto, você está falando com um público não técnico, então certifique-se de explicar conceitos complicados de forma simples e \
    mantenha um tom amigável e conversacional. \
    Se o trecho for irrelevante para a resposta, você pode ignorá-lo.
    PERGUNTA: '{query}'
    TRECHOS: '{retrieving_content}'

    RESPOSTA:
    """).format(query=query, retrieving_content=escaped)

    return prompt


def send_to_gemini(question, retrieving_content):
    prompt = get_prompt(question, retrieving_content)

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)

    return response.text

def main(uploaded_files, question):
    chroma_client = chromadb.Client(Settings(allow_reset=True))
    chroma_client.reset()
    embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBED_MODEL)
    collection = chroma_client.create_collection(name="resumes",
                                                 embedding_function=embedding_function,
                                                 metadata={"hnsw:space": "cosine"})
    process_docs(uploaded_files, collection)
    retrieving_content = collection.query(query_texts=[question], n_results=3)
    return(send_to_gemini(question, retrieving_content['documents'][0]))

if __name__ == "__main__":
    st.title("Análise de Currículos")

    uploaded_files = st.file_uploader("Upload de Currículos", accept_multiple_files=True, type=["pdf"])
    question = st.text_input("Perguntas sobre os candidatos:")

    if st.button("Gerar Resposta"):
        if uploaded_files and question:            
            st.write("Resposta gerada para a pergunta: ", question)
            result = main(uploaded_files, question)
            st.write(result)
        else:
            st.warning("Por favor, faça o upload dos currículos e insira uma pergunta.")

