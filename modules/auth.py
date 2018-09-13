import os

def is_authed():
  """Checks whether an auth file containing the GiHub authorization token exists"""
  try:
    auth_file = open(os.path.dirname(os.path.realpath(__file__)) + "/../auth", "r")
    return auth_file.readline()
  except IOError:
    return False

def set_auth():
  """Prompt the user for their GitHub authorization token and saves it to the auth file"""
  token = input("Authoriztion token: ")
  auth_file = open("auth", "w")
  auth_file.write(token)
  return token