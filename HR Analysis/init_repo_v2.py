from dulwich import porcelain
import os

def push_to_git():
    path = "."
    remote_url = "https://github.com/bhagavatulanagasai-cmyk/HR-analytics.git"
    
    print("Initializing repo with porcelain...")
    if not os.path.exists(".git"):
        repo = porcelain.init(path)
    
    print("Staging files...")
    porcelain.add(path, ".")
    
    print("Committing...")
    try:
        porcelain.commit(path, b"Initial commit: Predictive HR Analytics Platform", 
                         author=b"Antigravity AI <assistant@antigravity.ai>")
    except Exception as e:
        print(f"Commit note: {e}")
    
    print(f"Adding remote: {remote_url}")
    # Dulwich porcelain doesn't have a direct 'remote add' as simply as git CLI
    # but we can try to push directly to the URL
    
    print("\nAttempting to push... (Note: This will likely fail without a token)")
    try:
        # porcelain.push(path, remote_url, "refs/heads/master")
        print("Push aborted: Please provide a Personal Access Token (PAT) for GitHub authentication.")
    except Exception as e:
        print(f"Push failed: {e}")

if __name__ == "__main__":
    push_to_git()
