from dulwich.repo import Repo
import os
import time

def init_git_repo(path):
    print(f"Initializing repository at {path}...")
    if not os.path.exists(os.path.join(path, '.git')):
        repo = Repo.init(path)
    else:
        repo = Repo(path)
    
    # Add files
    print("Adding files to index...")
    # Get all files except .git and other ignorable stuff
    ignore_list = ['.git', 'hr_data.db', 'hr_model.pkl', '__pycache__']
    files_to_add = []
    for root, dirs, files in os.walk(path):
        # Filter out ignored directories
        dirs[:] = [d for d in dirs if d not in ignore_list]
        for f in files:
            if f not in ignore_list:
                rel_path = os.path.relpath(os.path.join(root, f), path)
                files_to_add.append(rel_path.encode('utf-8'))
    
    repo.stage(files_to_add)
    
    # Commit
    print("Committing changes...")
    conf = repo.get_config()
    conf.set(('user',), 'name', 'Antigravity AI')
    conf.set(('user',), 'email', 'assistant@antigravity.ai')
    conf.write_to_path()
    
    repo.do_commit(b"Initial commit: HR Analytics Platform", committer=b"Antigravity AI <assistant@antigravity.ai>")
    print("Commit complete!")

if __name__ == "__main__":
    init_git_repo(".")
