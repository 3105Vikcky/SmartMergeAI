 # Handles LLM interactions for generating merge conflict resolutions (RAG)
import openai
from .config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def resolve_merge_conflict(pr_number, conflict_text):
    """
    Compose a prompt including conflict text and retrieve similar cases,
    then call the LLM to generate a resolution.
    """
    # In a full implementation, you would retrieve similar past PRs from vector_store/retriever.
    similar_context = "Similar past conflict resolution context goes here."
    
    prompt = f"""
    You are an expert GitHub merge conflict resolution assistant.

    ### New Merge Conflict (PR #{pr_number}):
    {conflict_text}

    ### Context from similar past conflicts:
    {similar_context}

    Please suggest an optimal merge resolution with explanation.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a GitHub merge conflict expert."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response["choices"][0]["message"]["content"]
