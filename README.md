# SmartMergeAI Console Based

## 🚀 Overview
SmartMergeAI is an AI-powered automation tool designed to analyze and manage GitHub Pull Requests (PRs) efficiently. It leverages machine learning to predict PR merge success, ensuring smoother CI/CD workflows and reducing manual review effort.

## 🔥 Features
- **PR Analysis using AI**: Evaluates PRs based on past data and coding patterns.
- **GitHub API Integration**: Fetches historical PRs, approvals, comments, and CI/CD results.
- **Predictive Model**: Uses NLP and ML models to predict PR merge success.
- **Auto-Merge Logic**: Defines conditions for automated merging based on model predictions.
- **Command-Line Interface (CLI)**: Enables easy interaction with SmartMergeAI.

## 📂 Project Structure
```
SmartMergeAI/
│── smartmerge_ai/
│   ├── cli.py              # CLI for fetching data, training, and predicting PR merges
│   ├── config.py           # Configuration settings (GitHub API keys, repo details)
│   ├── github_api.py       # Fetches PR past data from GitHub API
│   ├── data_processor.py   # Cleans & structures PR data for ML
│   ├── model.py            # Loads & trains AI model for PR analysis
│   ├── train.py            # Training script for SmartMergeAI model
│   ├── predict.py          # Predicts if a PR should be merged
│   ├── merge_logic.py      # Defines conditions for auto-merging PRs
│   ├── utils.py            # Helper functions (logging, formatting)
│
│── data/                   # PR Data Storage
│   ├── raw/                # Raw PR data from GitHub API
│   ├── processed/          # Cleaned and structured data for model training
│   ├── datasets.py         # Preprocesses & structures PR data
│
│── model/                  # Machine Learning Model
│   ├── train.py            # Trains AI model on past PR data
│   ├── test.py             # Tests model accuracy on validation set
│   ├── saved_model/        # Stores trained models
│
│── tests/                  # Unit tests
│   ├── test_github_api.py  # Tests GitHub API integration
│   ├── test_model.py       # Tests model predictions
│   ├── test_cli.py         # Tests CLI commands
│
│── .env                    # GitHub API Token & config
│── requirements.txt        # Dependencies
│── README.md               # Project documentation
│── setup.py                # CLI setup script
```

## 🎯 Getting Started

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Setup Environment Variables
Create a `.env` file and add your GitHub API token:
```
GITHUB_TOKEN=<your_github_token>
```

### 3️⃣ Fetch PR Past Data
```bash
python smartmerge_ai/cli.py fetch --repo <repo-name>
```

### 4️⃣ Train the AI Model
```bash
python smartmerge_ai/train.py
```

### 5️⃣ Predict Merge Outcome for a PR
```bash
python smartmerge_ai/predict.py --pr <PR-ID>
```

## 📌 Future Enhancements
- Support for new repositories with **no past PR data**.
- Improved **deep learning models** for PR analysis.
- Integration with **GitHub Actions** for real-time PR monitoring.

## 🤝 Contributing
Contributions are welcome! Please submit a pull request or open an issue.

## 📜 License
64 Squares License. See `LICENSE` for details.

