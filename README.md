# create-repo

Creates a new repository locally and on GitHub and sets the remote destination

# Getting Started

## Dependencies

* [Python 3](https://www.python.org/)
* [Git](https://git-scm.com/)
* JSON-library
  ```
  pip install json
  ```
* requests-library
  ```
  pip install requests
  ```

## Installing

* Clone or download the project files to your local machine

## Execution

* Create a GitHub [authentication token](https://github.com/settings/tokens/new)
* Run `create-repo.py` from the directory in which you would like to create the repo, eg.
  ```
  C:\Users\User>py C:\Scripts\create-repo\create-repo.py
  ```
* The first execution will prompt for the GitHub authentication token
* Enter the repo name
* Enter the repo description
* A new GitHub and local repo will be created. The local repo's remote destination (origin) will be set to the GitHub repo's address
