# 🛠️ Makes it a package
# Define the __all__ variable
"""
SmartMergeAI Package
Version: 0.1.0
"""

from .Extract_Open_PR import fetch_all_open_prs
from .Extract_Closed_PR import fetch_all_closed_prs
from .vector_store import load_pr_data
from .vector_store import initialize_and_persist_chromadb
from .vector_store import format_closed_prs
from .vector_store import initialize_retriever
from .vector_store import truncate_text
from .ragLLM import evaluate_open_pr



__all__ = ["fetch_all_open_prs", "fetch_all_closed_prs","load_pr_data","format_closed_prs","initialize_retriever"
           , "evaluate_open_pr","truncate_text","initialize_and_persist_chromadb"]


__version__ = "0.1.0"
