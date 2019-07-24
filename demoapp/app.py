import requests

from chalice import Chalice


app = Chalice(app_name='demoapp')


def github_repos(username):
    formatted_repos = []

    if username:
        url = "https://api.github.com/users/{}/repos".format(username)

        r = requests.get(url)

        list_of_repos = r.json()

        for repo in list_of_repos:
            repo_object = {
              "name": repo["name"],
              "stars": repo["watchers"],
              "language": repo["language"],
            }

            formatted_repos.append(repo_object)
        
    return formatted_repos


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/user/{username}')
def github(username):
    return {"repos": github_repos(username)}

