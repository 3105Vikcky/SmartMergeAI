  # ⚙️ Configuration settings (GitHub API keys, repo details)
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")
# Add any other configuration constants
