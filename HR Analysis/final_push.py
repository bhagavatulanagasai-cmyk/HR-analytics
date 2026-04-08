from dulwich import porcelain
import sys

def push_with_token(token):
    path = "."
    # Format: https://<token>@github.com/<user>/<repo>.git
    remote_url = f"https://{token}@github.com/bhagavatulanagasai-cmyk/HR-analytics.git"
    
    print(f"Pushing to {remote_url.replace(token, '****')}...")
    try:
        porcelain.push(path, remote_url, b"refs/heads/master")
        print("✅ Push successful! Your code is now live on GitHub.")
    except Exception as e:
        print(f"❌ Push failed: {e}")
        print("\nTip: Make sure the token has 'repo' permissions and the repository URL is correct.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: py final_push.py <YOUR_GITHUB_TOKEN>")
    else:
        push_with_token(sys.argv[1])
