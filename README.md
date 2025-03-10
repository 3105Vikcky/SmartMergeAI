# SmartMergeAI Console Based

## 🚀 Overview
SmartMergeAI is an AI-powered automation tool designed to analyze and manage GitHub Pull Requests (PRs) efficiently. It leverages machine learning to predict PR merge success, ensuring smoother CI/CD workflows and reducing manual review effort.

## 🔥 Features
- **PR Analysis using AI**: Evaluates PRs based on past data and coding patterns.
- **Predictive Model**: Uses RAG  to predict PR merge success.
- **Auto-Merge Logic**: Defines conditions for automated merging based on model predictions.
- **Command-Line Interface (CLI)**: Enables easy interaction with SmartMergeAI.



## 🎯 Getting Started

### Create virtual Environment Activate it.

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Setup Environment Variables
Create a `.env` file and add your GitHub API token & OpenAI Key:
```
GITHUB_TOKEN=<your_github_token>
OPEN_AI_KEY=<your_openai_key>
```


### Run project by 
Go to CMD navigate Project Folder and write 'python -m smartmerge_ai.main'
<br>
After that Enter OwnerRepo <br>
           Enter RepoName <br>


## 📌 Future Enhancements
- Support for new repositories with **no past PR data**.
- Improved **deep learning models** for PR analysis.
- Integration with **GitHub Actions** for real-time PR monitoring.

## 🤝 Contributing
Contributions are welcome! Please submit a pull request or open an issue.



