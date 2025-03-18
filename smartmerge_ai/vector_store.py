
import os
import json
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Paths for ChromaDB storage
CLOSED_PR_DB_PATH = r"C:\Users\Admin\Desktop\SMARTAI\SmartMergeAI\data\Embeddings\closed_pr"
OPEN_PR_DB_PATH = r"C:\Users\Admin\Desktop\SMARTAI\SmartMergeAI\data\Embeddings\open_pr"


# Load PR Data
def load_pr_data(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)



# Function to truncate long text fields
def truncate_text(text, max_length=300):
    return text[:max_length] + "..." if len(text) > max_length else text

def format_closed_prs(closed_prs):
    formatted_prs = []
    for pr in closed_prs:
        file_changes = " | ".join(
            [f"{fc.get('Filename', 'Unknown')} ({fc.get('Status', 'Unknown')})" for fc in pr.get("File Changes", [])]
        )
        comments = " | ".join(
            [f"{c.get('User', 'Unknown')}: {truncate_text(c.get('Body', ''))}" for c in pr.get("New Comments", [])]
        )
        
        formatted_prs.append(
            f"PR Number: {pr.get('PR Number', 'N/A')}, Title: {truncate_text(pr.get('Title', 'No Title'))}, State: {pr.get('State', 'Unknown')}, "
            f"Author: {pr.get('Author', 'Unknown')}, Created Date: {pr.get('Created Date', 'Unknown')}, "
            f"Merged Date: {pr.get('Merged Date', 'N/A')}, Base Branch: {pr.get('Base Branch', 'Unknown')}, "
            f"Head Branch: {pr.get('Head Branch', 'Unknown')}, Merge Conflict: {pr.get('Merge Conflict', 'Unknown')}, "
            f"File Changes: {truncate_text(file_changes)}, Comments: {truncate_text(comments)}"
        )
    return formatted_prs


# Split large text into smaller chunks
def chunk_data(data, chunk_size=500):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=50)
    return splitter.split_text("\n".join(data))

# Initialize RAG-based retrieval system with chunked data
def initialize_retriever(closed_pr_texts):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large", openai_api_key=OPENAI_API_KEY)
    chunked_texts = chunk_data(closed_pr_texts)
    vector_store = Chroma.from_texts(chunked_texts, embeddings)
    return vector_store.as_retriever()



def initialize_and_persist_chromadb(closed_pr_file, open_pr_file):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large", openai_api_key=OPENAI_API_KEY)

    # Load and format PRs
    print("Loading PR data")
    closed_prs = format_closed_prs(load_pr_data(closed_pr_file))
    open_prs = format_closed_prs(load_pr_data(open_pr_file))

    print(f" Loaded {len(closed_prs)} closed PRs and {len(open_prs)} open PRs.")

    # Split into smaller chunks
    print(" Chunking PR data...")
    closed_chunks = chunk_data(closed_prs)
    open_chunks = chunk_data(open_prs)

    print(f" Created {len(closed_chunks)} chunks for closed PRs and {len(open_chunks)} for open PRs.")

    # Store in ChromaDB
    print("Storing embeddings in ChromaDB...")
    closed_db = Chroma.from_texts(closed_chunks, embeddings, persist_directory=CLOSED_PR_DB_PATH)
    open_db = Chroma.from_texts(open_chunks, embeddings, persist_directory=OPEN_PR_DB_PATH)

    closed_db.persist()
    open_db.persist()
    print("✅ ChromaDB storage complete!")

if __name__ == "__main__":
    closed_pr_json = r"C:\Users\Admin\Desktop\SMARTAI\SmartMergeAI\data\raw\closed_pr\wheel_all_closed_prs.json"
    open_pr_json = r"C:\Users\Admin\Desktop\SMARTAI\SmartMergeAI\data\raw\open_pr\wheel_all_open_prs.json"

    initialize_and_persist_chromadb(closed_pr_json, open_pr_json)
