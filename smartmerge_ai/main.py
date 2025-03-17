from smartmerge_ai.Extract_Open_PR import fetch_all_open_prs
from smartmerge_ai.Extract_Closed_PR import fetch_all_closed_prs
from .vector_store import load_pr_data
from .ragLLM import evaluate_open_pr
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from textwrap import fill

console = Console()

def format_text(text, width=80):
    """Formats text to a readable paragraph style"""
    return fill(text, width=width)

def main():
    console.print("\n[bold yellow]🚀 SmartMergeAI CLI[/bold yellow]\n")

    console.print("[cyan]📌 Fetch PR Data[/cyan]\n")
    
    repo_owner = console.input("[green]Enter repo Owner:[/green] ").strip()
    repo_name = console.input("[green]Enter repo Name:[/green] ").strip()

    console.print("\n[blue]Fetching PR data...[/blue]\n")
    
    # Fetch PR Data
    fetch_all_closed_prs(repo_owner, repo_name)  # Fetch closed PR data
    fetch_all_open_prs(repo_owner, repo_name)  # Fetch open PR data
    
    console.print("\n[cyan]📊 Loading PR Data...[/cyan]\n")
    
    closed_prs = load_pr_data(rf"data/raw/closed_pr/{repo_name}_all_closed_prs.json")
    open_prs = load_pr_data(rf"data/raw/open_pr/{repo_name}_all_open_prs.json")
   
    console.print("\n[bold green]🤖 Evaluating PRs using RAG-based AI...[/bold green]\n")
    
    merge_predictions = evaluate_open_pr(closed_prs, open_prs)
    
    # Display structured table output
    table = Table(title="🔹 PR Merge Predictions", show_lines=True)

    table.add_column("PR #", justify="center", style="cyan", no_wrap=True)
    table.add_column("Merge %", justify="center", style="green", no_wrap=True)
    table.add_column("Recommendation", justify="left", style="yellow")

    for pr_number, prediction in merge_predictions.items():
        response = prediction.get("response", "No response available")
        merge_percentage = prediction.get("merge_percentage", "N/A")
        
        formatted_response = format_text(response, width=60)
        
        table.add_row(str(pr_number), str(merge_percentage), formatted_response)

    console.print(table)

    console.print("\n[bold green]✅ Analysis Complete![/bold green]\n")

if __name__ == "__main__":
    main()








# # Main File of SmartMergeAI 
# from smartmerge_ai.Extract_Open_PR import fetch_all_open_prs
# from smartmerge_ai.Extract_Closed_PR import fetch_all_closed_prs
# from .vector_store import load_pr_data
# from .ragLLM import evaluate_open_pr


# def main():
#     print("SmartMergeAI CLI")
#     print()
#     print("Fetch PR data :  ")
#     print()
#     repo_owner=str(input("Enter repo Onwer :  "))
    
#     repo_name=str(input("Enter repo Name :  "))
    


#     # It fetchese the PR data on given repo
#     fetch_all_closed_prs(repo_owner, repo_name)  # Fetches all closed PR Data on given repo
#     fetch_all_open_prs(repo_owner, repo_name)  # Fetches all closed PR Data on given repo
    
    
#     #Next load PR and provide merge_prediction through RAG
#     closed_prs = load_pr_data(rf"data/raw/closed_pr/{repo_name}_all_closed_prs.json")
#     open_prs = load_pr_data(rf"data/raw/open_pr/{repo_name}_all_open_prs.json")
   
    
#     merge_predictions = evaluate_open_pr(closed_prs, open_prs)
    
#     for pr_number, prediction in merge_predictions.items():
#         print(f"PR {pr_number}: {prediction}")
        
# if __name__ == "__main__":
#     main()



