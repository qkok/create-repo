import os

def create_repo(repo_name, url):
  os.system("mkdir " + repo_name)
  os.system("git init " + repo_name)
  os.system("git -C " + repo_name + " remote add origin " + url + "/" + repo_name)
  print("Remote added") 