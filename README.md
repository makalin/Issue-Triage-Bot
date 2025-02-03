# Issue Triage Bot

The **Issue Triage Bot** is a Python script that automatically labels and assigns GitHub issues based on keywords or patterns in the issue title and description. It helps streamline issue management by reducing manual effort in categorizing and assigning tasks.

## Features
- Automatically assigns labels and users based on predefined keywords.
- Uses GitHub's API via **PyGitHub** to fetch and update issues.
- Helps maintain an organized and efficient issue tracking workflow.

## Installation

### Prerequisites
- Python 3.x
- A GitHub **Personal Access Token (PAT)** with repository access.

### Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/makalin/issue-triage-bot.git
   cd issue-triage-bot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Configure the bot by updating `itbot.py`:
   - Replace `GITHUB_TOKEN` with your **personal access token**.
   - Set `REPO_NAME` to your target repository.
   - Modify the `KEYWORDS` dictionary to match your desired keywords, labels, and assignees.

## Usage
Run the script to process existing issues:
```sh
python itbot.py
```

## Configuration
Edit `itbot.py` to define:
- **GITHUB_TOKEN**: Your personal access token.
- **REPO_NAME**: The repository to monitor.
- **KEYWORDS**: A dictionary mapping keywords to labels and assignees.

Example `KEYWORDS` mapping:
```python
KEYWORDS = {
    "bug": {"label": "bug", "assignee": "developer1"},
    "feature": {"label": "enhancement", "assignee": "developer2"},
    "documentation": {"label": "docs", "assignee": "technical-writer"}
}
```

## Automating with GitHub Actions
To automate issue triaging, create a GitHub Actions workflow:

1. Add a `.github/workflows/triage.yml` file with the following content:
```yaml
name: Issue Triage Bot
on:
  issues:
    types: [opened, edited]
jobs:
  triage:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run Issue Triage Bot
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: python itbot.py
```

2. Commit and push this workflow file to your repository.
3. The bot will now run automatically whenever an issue is opened or edited.

## License
This project is licensed under the MIT License.

## Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request to improve the bot.
