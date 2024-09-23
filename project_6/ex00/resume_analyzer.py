
import os
import PyPDF2
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer

EMBED_MODEL = "all-MiniLM-L6-v2"

def interactive_query_loop(collection):
    while True:
        query = input("\nConsulta: ")
        if query.lower() == 'sair':
            break

        results = collection.query(query_texts=[query], n_results=3)
        print("\nResultados:")
        for document, metadata, distances in zip(results['documents'][0], results['metadatas'][0], results['distances'][0]):
            print(f"Distance: {distances}")
            print(f"Documento: {metadata['source']}")
            print(f"Trecho: {document[:200]}...") # Apenas os 200 primeiros caracteres
            print()

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

def process_pdfs(path):
    pdf_texts = {}
    files = os.listdir(path)
    print(f'Encontrados {len(files)} arquivos PDF no diretório.')
    for i, filename in enumerate(files):
        if filename.endswith('.pdf'):
            print(f'Processando PDF {i}/{len(files)}: {filename}')
            file_path = os.path.join(path, filename)
            text = extract_text_from_pdf(file_path)
            pdf_texts[filename] = text
            print(f'- Documento {file_path} processado e armazenado.')
    return pdf_texts

def process_pdf_directory(pdf_directory, collection):
    texts = process_pdfs(pdf_directory)

    for filename, text in texts.items():
        collection.add(
            documents=[text],
            metadatas=[{"source": filename}],
            ids=[filename]
        )


def main():
    persist_directory = "./chroma_data"
    pdf_directory = "./pdfs"

    chroma_client = chromadb.PersistentClient(path=persist_directory)
    embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBED_MODEL)
    collection = chroma_client.create_collection(name="resumes",
                                                 embedding_function=embedding_function,
                                                 metadata={"hnsw:space": "cosine"})
    process_pdf_directory(pdf_directory, collection)
    interactive_query_loop(collection)

if __name__ == "__main__":
    main()
