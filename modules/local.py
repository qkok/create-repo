import os

def create_repo(repo_name, url):
  """Creates a local repo and sets the GitHub repo as its remote

  Args:
    repo_name: The name of the new repo
    url: The url of the user's GitHub
  """
  os.system("mkdir " + repo_name)
  os.system("git init " + repo_name)
  os.system("git -C " + repo_name + " remote add origin " + url + "/" + repo_name)