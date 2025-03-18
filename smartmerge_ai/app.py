from fastapi import FastAPI, HTTPException
from smartmerge_ai.Extract_Open_PR import fetch_all_open_prs
from smartmerge_ai.Extract_Closed_PR import fetch_all_closed_prs
from smartmerge_ai.vector_store import load_pr_data
from smartmerge_ai.ragLLM import evaluate_open_pr

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to SmartMergeAI API"}


@app.get("/process_prs/{repo_owner}/{repo_name}")
def process_prs(repo_owner: str, repo_name: str):
    """
    Fetches open & closed PRs and evaluates them automatically.
    """
    try:
        # Fetch PR data
        fetch_all_closed_prs(repo_owner, repo_name)
        fetch_all_open_prs(repo_owner, repo_name)

        # Load PR data
        closed_prs = load_pr_data(
            f"data/raw/closed_pr/{repo_name}_all_closed_prs.json")
        open_prs = load_pr_data(
            f"data/raw/open_pr/{repo_name}_all_open_prs.json")

        # Evaluate PRs using RAG model
        merge_predictions = evaluate_open_pr(closed_prs, open_prs)

        return {
            "message": "PRs processed successfully",
            "merge_predictions": merge_predictions
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))