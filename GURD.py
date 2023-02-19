import os
import requests
import zipfile

def backup_github_repos(username, token, backup_dir):
    # Get a list of all the repositories for the specified GitHub user
    url = f"https://api.github.com/users/username_youwantto_clone/repos"
    headers = {
        "Authorization": f"Token {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to get the repositories for user {username}. Response: {response.content}")
    repos = response.json()

    # Clone each repository into the backup directory
    for repo in repos:
        repo_name = repo["name"]
        repo_url = repo["clone_url"]
        repo_path = os.path.join(backup_dir, repo_name)
        os.system(f"git clone {repo_url} {repo_path}")

def compress_backup(backup_dir, zip_file):
    # Compress the backup directory to a .zip file
    with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED) as zip_fp:
        for root, dirs, files in os.walk(backup_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zip_fp.write(file_path)

if __name__ == "__main__":
    # Replace <GITHUB_ACCESS_TOKEN> with your GitHub access token
    username = "your_username"
    token = "your_token"
    backup_dir = "backup_path"
    backup_github_repos(username, token, backup_dir)

    # Compress the backup directory
    zip_file = "path_to_zip_file"
    compress_backup(backup_dir, zip_file)
