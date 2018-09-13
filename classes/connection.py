import requests
import json

class Connection:
  """Functions wrapping the GitHub API"""
  def __init__(self, token):
    """ Authorizes the GitHub API calls and sets the user's GitHub url

    Args:
      token: The authorization token
    """
    self.token = token
    r = requests.get("https://api.github.com/user", headers={"Authorization": "token " + token})
    self.url = r.json()['html_url']

  def create_repo(self, repo_name, repo_description):
    """Creates a new repo on GitHub

    Args:
      repo_name: The name of the new repo
      repo_description: The new repo's description

    Return:
      The result of the POST request
    """
    r = requests.post(
      "https://api.github.com/user/repos", 
      data = json.dumps({"name": repo_name, "description": repo_description}), 
      headers = {"Authorization": "token " + self.token}
    )

    if r.status_code == 201:
      return True

    return False

  def get_url(self):
    """Returns the user's GitHub url"""
    return self.url