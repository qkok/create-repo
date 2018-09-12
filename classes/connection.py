import requests
import json

class Connection:
  def __init__(self, token):
    self.token = token
    r = requests.get("https://api.github.com/user", headers={"Authorization": "token " + token})
    self.url = r.json()['html_url']

  def create_repo(self, repo_name, repo_description):
    r = requests.post(
      "https://api.github.com/user/repos", 
      data = json.dumps({"name": repo_name, "description": repo_description}), 
      headers = {"Authorization": "token " + self.token}
    )

    if r.status_code == 201:
      return True

    return False

  def get_url(self):
    return self.url