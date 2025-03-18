import uvicorn
import sys
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from textwrap import fill
from smartmerge_ai.Extract_Open_PR import fetch_all_open_prs
from smartmerge_ai.Extract_Closed_PR import fetch_all_closed_prs
from smartmerge_ai.vector_store import load_pr_data
from smartmerge_ai.ragLLM import evaluate_open_pr

console = Console()


def format_text(text, width=80):
    """Formats text to a readable paragraph style"""
    return fill(text, width=width)


def run_cli():
    """Runs the CLI version of SmartMergeAI"""
    console.print("\n[bold yellow]🚀 SmartMergeAI CLI[/bold yellow]\n")

    console.print("[cyan]📌 Fetch PR Data[/cyan]\n")

    repo_owner = console.input("[green]Enter repo Owner:[/green] ").strip()
    repo_name = console.input("[green]Enter repo Name:[/green] ").strip()

    console.print("\n[blue]Fetching PR data...[/blue]\n")

    # Fetch PR Data
    fetch_all_closed_prs(repo_owner, repo_name)  # Fetch closed PR data
    fetch_all_open_prs(repo_owner, repo_name)  # Fetch open PR data

    console.print("\n[cyan]📊 Loading PR Data...[/cyan]\n")

    closed_prs = load_pr_data(
        rf"SmartMergeAI/data/raw/closed_pr/{repo_name}_all_closed_prs.json")
    open_prs = load_pr_data(rf"SmartMergeAI/data/raw/open_pr/{repo_name}_all_open_prs.json")

    console.print(
        "\n[bold green]🤖 Evaluating PRs using RAG-based AI...[/bold green]\n")

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

        table.add_row(str(pr_number), str(
            merge_percentage), formatted_response)

    console.print(table)

    console.print("\n[bold green]✅ Analysis Complete![/bold green]\n")


def run_fastapi():
    """Runs the FastAPI server"""
    console.print("\n[bold cyan]🚀 Starting FastAPI Server...[/bold cyan]\n")
    uvicorn.run("smartmerge_ai.app:app",
                host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    console.print(
        "\n[bold magenta]Run as (1) CLI or (2) FastAPI?[/bold magenta]\n")
    choice = console.input("[green]Enter your choice (1/2): [/green]").strip()

    if choice == "1":
        run_cli()
    elif choice == "2":
        run_fastapi()
    else:
        console.print("\n[red]❌ Invalid choice. Exiting.[/red]\n")
        sys.exit(1)















 







