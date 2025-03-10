 # Retrieves similar past conflicts from the vector database based on embeddings
from langchain_community.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

from .vector_store import format_closed_prs
from .vector_store import initialize_retriever
from .vector_store import truncate_text

#Load openai KEY
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Define RAG-based prompt
def generate_prompt(open_pr):
    return (
        f"Analyze the following open PR based on past closed PRs and provide a merge recommendation.\n\n"
        f"Open PR Details:\n"
        f"PR Number: {open_pr['PR Number']}, Title: {truncate_text(open_pr['Title'])}, State: {open_pr['State']}, "
        f"Author: {open_pr['Author']}, Created Date: {open_pr['Created Date']}, "
        f"Base Branch: {open_pr['Base Branch']}, Head Branch: {open_pr['Head Branch']}, Merge Conflict: {open_pr['Merge Conflict']}, "
        f"File Changes: {truncate_text(str(open_pr['File Changes']))}\n\n"
        f"- If a merge conflict exists, assess if it can be resolved based on past cases.\n"
        f"- Provide insights on risks, necessary fixes, and best practices before merging."
    )

def extract_merge_percentage(response_text):
    """
    Parses the AI response to assign a merge confidence percentage.
    """
    response_text = response_text.lower()

    # Define confidence scores based on keywords
    scores = {
        "ready to merge": 90,
        "safe to merge": 85,
        "minor issues": 75,
        "requires small changes": 70,
        "needs review": 60,
        "possible conflicts": 50,
        "merge conflicts exist": 40,
        "requires significant changes": 30,
        "not recommended": 20,
        "do not merge": 10
    }

    # Find the highest matching score
    for keyword, score in scores.items():
        if keyword in response_text:
            return score

    # Default to 50% if no clear match
    return 50  

def evaluate_open_pr(closed_prs, open_prs):
    closed_pr_texts = format_closed_prs(closed_prs)
    retriever = initialize_retriever(closed_pr_texts)
    llm = ChatOpenAI(model_name="gpt-4o", openai_api_key=OPENAI_API_KEY)
    rag_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

    results = {}
    for open_pr in open_prs:
        prompt = generate_prompt(open_pr)
        response = llm.invoke([
            {"role": "system", "content": "You are an AI that evaluates PRs and provides a merge recommendation."},
            {"role": "user", "content": prompt}
        ])

        response_text = response.content
        merge_confidence = extract_merge_percentage(response_text)

        results[open_pr['PR Number']] = {
            "response": response_text,
            "merge_percentage": f"{merge_confidence}%"
        }

    return results