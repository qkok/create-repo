def is_authed():
  try:
    auth_file = open("auth", "r")
    return auth_file.readline()
  except IOError:
    return False

def set_auth():
  token = input("Authoriztion token: ")
  auth_file = open("auth", "w")
  auth_file.write(token)
  return token