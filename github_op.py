from github import Github, GithubException
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")

github = Github(GITHUB_API_TOKEN)
organization_name = "tanochan-sakonyan"
try:
    org = github.get_organization(organization_name)
except GithubException as e:
    print(f"Error accessing organization: {e}")
    exit(1)

def get_all_repos():
    print(org)
    repos = org.get_repos() 
    repo_list = []
    for repo in repos:
        print(repo.full_name)   
        repo_list.append(repo.full_name)
    return repo_list

def  get_repo(repo_name):
    try:
        repo = org.get_repo(repo_name)
    except GithubException as e:
        print(f"Error accessing repository: {e}")
        return None

def create_issue(issue_info):
    repo_name = issue_info["repository"]    
    title     = issue_info["title"]
    body      = issue_info["body"]
    assignee  = issue_info["assignee"]
    labels    = issue_info["labels"]

    repo = github.get_repo(repo_name) 
    #リポジトリが存在しない場合
    if not repo:
        return False   

    try:
        issue = repo.create_issue(title=title, body=body, assignee=assignee, labels=labels)
        return issue
    
    except GithubException as e:
        print(f"Error creating issue: {e}")
        return False


def cls_issue(repo_name, issue_title):
    repo = github.get_repo(repo_name)
    #リポジトリが存在しない場合
    if not repo:
        return False
    
    for issue in repo.get_issues():
        if issue.title == issue_title:
            issue.edit(state="closed")
            return True
        
    return False