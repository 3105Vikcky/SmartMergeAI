# 🔄 Cleans & structures PR data for ML
import json
import os
import re
import pandas as pd

def load_pr_data(file_path):
    """Load raw PR data from JSON file."""
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return []
    
    with open(file_path, "r") as file:
        return json.load(file)

def clean_text(text):
    """Remove special characters, URLs, and extra spaces from PR titles and descriptions."""
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    return text.lower()

def extract_features(pr):
    """Extract relevant features from PR data."""
    keywords = ["fix", "bug", "feature", "refactor"]
    title = clean_text(pr.get("title", ""))
    description = clean_text(pr.get("body", ""))
    
    return {
        "id": pr.get("id"),
        "title_length": len(title.split()),
        "description_length": len(description.split()),
        "num_keywords": sum(1 for word in keywords if word in title or word in description),
        "state": pr.get("state"),
        "merged": pr.get("merged", False),
        "created_at": pr.get("created_at"),
        "comments": pr.get("comments", 0),
        "reviews": pr.get("review_comments", 0),
        "approval_count": pr.get("review_comments", 0),  # Placeholder for approvals
        "change_request_count": 0,  # Placeholder for requested changes
        "changed_files": pr.get("changed_files", 0),
        "lines_added": pr.get("additions", 0),
        "lines_deleted": pr.get("deletions", 0)
    }

def process_pr_data(raw_data):
    """Process raw PR data and extract features."""
    return [extract_features(pr) for pr in raw_data]

def save_processed_data_csv(data, output_path):
    """Save processed PR data as a CSV file."""
    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Processed PR data saved to {output_path}")

# Example Usage
if __name__ == "__main__":
    input_file = "data/raw/LocalRepo_prs.json"  # Replace with actual file path
    output_file = "data/processed/Hello-World_cleaned.csv"
    
    raw_prs = load_pr_data(input_file)
    cleaned_prs = process_pr_data(raw_prs)
    save_processed_data_csv(cleaned_prs, output_file)
