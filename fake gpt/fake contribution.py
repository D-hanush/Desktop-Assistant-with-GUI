import os
import time
import random

def generate_fake_contributions(repo_path):
    # Create a new git repository or initialize an existing one
    if not os.path.exists(os.path.join(repo_path, '.git')):
        os.system(f'git init {repo_path}')

    os.chdir(repo_path)

    # Generate random commits with fake messages
    for i in range(random.randint(50, 100)):
        os.system('git config --local user.email "D-hanush@github.com"')
        os.system('git config --local user.name "D-hanush"')
        os.system('git add .')
        commit_message = f"D-hanush commit {i}: {random.choice(['added', 'fixed', 'improved', 'updated'])} some awesome code"
        os.system(f'git commit -m "{commit_message}"')
        time.sleep(random.uniform(300, 600))  # Vary the time between commits

    # Push the commits to the remote repository
    os.system('git push -u origin master')

if __name__ == '__main__':
    repo_path = input("Enter the path to your local GitHub repository (e.g., /path/to/Desktop-Assistant-with-GUI): ")
    generate_fake_contributions(repo_path)
    print("Fake contributions generated! Go check out your awesome-looking contribution graph!")
