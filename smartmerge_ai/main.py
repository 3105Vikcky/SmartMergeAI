# Main File of SmartMergeAI 
from smartmerge_ai.Extract_Open_PR import fetch_all_open_prs
from smartmerge_ai.Extract_Closed_PR import fetch_all_closed_prs
from .vector_store import load_pr_data
from .ragLLM import evaluate_open_pr


def main():
    print("SmartMergeAI CLI")
    print()
    print("Fetch PR data :  ")
    print()
    repo_owner=str(input("Enter repo Onwer :  "))
    
    repo_name=str(input("Enter repo Name :  "))
    #pr_number=str(input("Enter pr_number"))


    # It fetchese the PR data on given repo
    fetch_all_closed_prs(repo_owner, repo_name)  # Fetches all closed PR Data on given repo
    fetch_all_open_prs(repo_owner, repo_name)  # Fetches all closed PR Data on given repo
    
    
    #Next load PR and provide merge_prediction through RAG
    closed_prs = load_pr_data(rf"data/raw/closed_pr/{repo_name}_all_closed_prs.json")
    open_prs = load_pr_data(rf"data/raw/open_pr/{repo_name}_all_open_prs.json")
   
    
    merge_predictions = evaluate_open_pr(closed_prs, open_prs)
    
    for pr_number, prediction in merge_predictions.items():
        print(f"PR {pr_number}: {prediction}")
        
if __name__ == "__main__":
    main()



