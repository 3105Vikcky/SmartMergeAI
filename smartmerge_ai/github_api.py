# 🔗 Fetches PR past data from GitHub API
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
BASE_URL = "https://api.github.com"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}

def fetch_pr_data(repo_owner, repo_name, max_prs=100):
    """Fetch past PR data from GitHub API and store it in JSON format."""
    url = f"{BASE_URL}/repos/{repo_owner}/{repo_name}/pulls?state=all&per_page=100"
    pr_data = []
    
    while url and len(pr_data) < max_prs:
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print(f"Error fetching PRs: {response.json()}")
            return
        
        pr_data.extend(response.json())
        url = response.links.get('next', {}).get('url')  # Handle pagination
        
    if len(pr_data)<=0:
        print("No PR  generated yet")
    else:
        with open(f"data/raw/{repo_name}_prs.json", "w") as file:
            json.dump(pr_data, file, indent=4)
        print(f" {len(pr_data)} PRs saved to data/raw/{repo_name}_prs.json")

# Give the repo Owner_name and  repo_name 
if __name__ == "__main__":
    
    repo_owner =str(input("Enter a Repo_owner : "))           
    repo_name =str(input("Enter a Repo_name: "))                         
    fetch_pr_data(repo_owner, repo_name)
