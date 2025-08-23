# This script uses Git to commit and push changes to a GitHub repository
# Run this script after making changes to your project

import subprocess

def update_github_repo(commit_message="Update project details"):
    try:
        # Stage all changes
        subprocess.run(["git", "add", "."], check=True)
        # Commit changes
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        # Push to remote repository
        subprocess.run(["git", "push"], check=True)
        print("Repository updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_github_repo()