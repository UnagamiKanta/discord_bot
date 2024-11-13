def is_mkissue(text):
    return '!mkissue' in text

def get_issue_info(text):
    cmd = text.split(' ')
    issue_info = {"repository": "", "title":"" , "body":"", "assignee":"", "labels":[]}

    for c in cmd:
        if c.startswith('repo='):
            issue_info["repository"] = c.split('=')[1]
        if c.startswith('title='):
            issue_info["title"] = c.split('=')[1]
        elif c.startswith('body='):
            issue_info["body"] = c.split('=')[1]
        elif c.startswith('assignee='):
            issue_info["assignee"] = c.split('=')[1]
        elif c.startswith('labels='):
            issue_info["labels"] = c.split('=')[1].split(',')

    return issue_info
        

def is_clsissue(text):
    return '!clsissue' in text

def is_getrepos(text):
    return '!repos' in text
