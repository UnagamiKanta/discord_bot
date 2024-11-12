from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from github_op import get_all_repos, create_issue
from util import get_issue_info

def test_create_issue():
    info = get_issue_info("!mkissue repo=tanochan-sakonyan/backend title=test body=test text assignee= assignee labels=bug")
    print(info)
    issue = create_issue(info)
    print(issue)

test_create_issue()