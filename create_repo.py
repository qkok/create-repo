from modules.auth import is_authed, set_auth
from modules.local import create_repo
from classes.connection import Connection

# checks whether auth file with token is present
token = is_authed()

if not token:
  # saves the token to a file
  token = set_auth()

# create a github api connection
connection = Connection(token)

repo_name = input("Repo name: ")
repo_description = input("Repo description: ")

# create a github repo
if connection.create_repo(repo_name, repo_description):
  # create a local repo and add the github repos as remote
  create_repo(repo_name, connection.get_url())
  