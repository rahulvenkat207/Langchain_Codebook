import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Define paths
current_dir = "C:/C1X-intern/Langchain_study/4_Rag"  
file_path = os.path.join(current_dir, "books", "odyssey.txt")
persistent_directory = os.path.join(current_dir, "db", "chroma_db")  # Path to manually created directory

# Check if vector store is already initialized
if not os.listdir(persistent_directory):  # If empty, initialize
    print("Persistent directory is empty. Initializing vector store...")

    # Ensure the text file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist. Please check the path.")

    loader = TextLoader(file_path,encoding="utf-8")
    documents = loader.load()

    # Splitting text
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0, separator="\n")
    docs = text_splitter.split_documents(documents)

    # Creating embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # Storing vector store in `persistent_directory`
    db = Chroma.from_documents(docs, embeddings, persist_directory=persistent_directory)

    # Save vector store
    db.persist()
    print(f"Vector store successfully created and saved in: {persistent_directory}")

else:
    print(f"Vector store already exists at: {persistent_directory}")
