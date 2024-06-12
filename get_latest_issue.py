import sys

from github import Github
# Authentication is defined via github.Auth
from github import Auth



token = sys.argv[1]
repositry = sys.argv[2]
# using an access token
auth = Auth.Token(token)
# First create a Github instance:
# Public Web Github
g = Github(auth=auth)
repo = g.get_repo(repositry)
open_issues = repo.get_issues(state='open')
issue = open_issues[0]

attachment_url = issue.body.split("(")[1].split(")")[0]
issue_num = issue.number
issue_title = issue.title

f = open("output_context.sh", "a")
f.write(f'echo \"::set-output name=issue_num::{issue_num}\"\n')
f.write(f'echo \"::set-output name=issue_title::{issue_title}\"\n')
f.write(f'echo \"::set-output name=attachment_url::{attachment_url}\"\n')

f.close()

