from github import Github

# Configuration
GITHUB_TOKEN = "your_github_personal_access_token"
REPO_NAME = "your_username/your_repo_name"

# Define keywords and corresponding labels/assignees
KEYWORDS = {
    # Bugs and Errors
    "bug": {"label": "bug", "assignee": "developer1"},
    "error": {"label": "bug", "assignee": "developer1"},
    "crash": {"label": "bug", "assignee": "developer1"},
    "fix": {"label": "bug", "assignee": "developer1"},

    # Features and Enhancements
    "feature": {"label": "enhancement", "assignee": "developer2"},
    "improvement": {"label": "enhancement", "assignee": "developer2"},
    "enhancement": {"label": "enhancement", "assignee": "developer2"},
    "request": {"label": "enhancement", "assignee": "developer2"},

    # Documentation
    "documentation": {"label": "docs", "assignee": "technical-writer"},
    "doc": {"label": "docs", "assignee": "technical-writer"},
    "wiki": {"label": "docs", "assignee": "technical-writer"},
    "guide": {"label": "docs", "assignee": "technical-writer"},

    # Priority and Urgency
    "urgent": {"label": "high-priority", "assignee": "developer1"},
    "critical": {"label": "high-priority", "assignee": "developer1"},
    "priority": {"label": "high-priority", "assignee": "developer1"},
    "asap": {"label": "high-priority", "assignee": "developer1"},

    # Testing
    "test": {"label": "testing", "assignee": "tester1"},
    "testing": {"label": "testing", "assignee": "tester1"},
    "qa": {"label": "testing", "assignee": "tester1"},
    "quality": {"label": "testing", "assignee": "tester1"},

    # Design and UI/UX
    "design": {"label": "ui/ux", "assignee": "designer1"},
    "ui": {"label": "ui/ux", "assignee": "designer1"},
    "ux": {"label": "ui/ux", "assignee": "designer1"},
    "interface": {"label": "ui/ux", "assignee": "designer1"},

    # Performance
    "performance": {"label": "performance", "assignee": "developer3"},
    "slow": {"label": "performance", "assignee": "developer3"},
    "optimization": {"label": "performance", "assignee": "developer3"},
    "speed": {"label": "performance", "assignee": "developer3"},

    # Security
    "security": {"label": "security", "assignee": "security-team"},
    "vulnerability": {"label": "security", "assignee": "security-team"},
    "hack": {"label": "security", "assignee": "security-team"},
    "breach": {"label": "security", "assignee": "security-team"},

    # Backend
    "backend": {"label": "backend", "assignee": "backend-dev"},
    "server": {"label": "backend", "assignee": "backend-dev"},
    "api": {"label": "backend", "assignee": "backend-dev"},
    "database": {"label": "backend", "assignee": "backend-dev"},

    # Frontend
    "frontend": {"label": "frontend", "assignee": "frontend-dev"},
    "client": {"label": "frontend", "assignee": "frontend-dev"},
    "browser": {"label": "frontend", "assignee": "frontend-dev"},
    "css": {"label": "frontend", "assignee": "frontend-dev"},
    "javascript": {"label": "frontend", "assignee": "frontend-dev"},

    # Mobile
    "mobile": {"label": "mobile", "assignee": "mobile-dev"},
    "ios": {"label": "mobile", "assignee": "mobile-dev"},
    "android": {"label": "mobile", "assignee": "mobile-dev"},
    "app": {"label": "mobile", "assignee": "mobile-dev"},

    # Infrastructure
    "infrastructure": {"label": "infra", "assignee": "devops"},
    "devops": {"label": "infra", "assignee": "devops"},
    "deployment": {"label": "infra", "assignee": "devops"},
    "serverless": {"label": "infra", "assignee": "devops"},
    "kubernetes": {"label": "infra", "assignee": "devops"},
    "docker": {"label": "infra", "assignee": "devops"},
}

# Initialize GitHub client
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

def triage_issues():
    # Fetch all open issues
    issues = repo.get_issues(state="open")

    for issue in issues:
        print(f"Processing issue: #{issue.number} - {issue.title}")

        # Check title and body for keywords
        content = f"{issue.title} {issue.body}".lower()

        # Apply labels and assignees based on keywords
        for keyword, actions in KEYWORDS.items():
            if keyword in content:
                # Add label if not already present
                if actions["label"] not in [label.name for label in issue.labels]:
                    issue.add_to_labels(actions["label"])
                    print(f"Added label: {actions['label']}")

                # Assign issue if not already assigned
                if actions["assignee"] and not issue.assignee:
                    assignee = g.get_user(actions["assignee"])
                    issue.add_to_assignees(assignee)
                    print(f"Assigned to: {actions['assignee']}")

if __name__ == "__main__":
    triage_issues()