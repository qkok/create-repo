from modules.auth import is_authed, set_auth
from modules.local import create_repo
from classes.connection import Connection

token = is_authed()

if not token:
  token = set_auth()

connection = Connection(token)

repo_name = input("Repo name: ")
repo_description = input("Repo description: ")

if connection.create_repo(repo_name, repo_description):
  create_repo(repo_name, connection.get_url())
  