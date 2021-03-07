import requests
import json

userID = input("Enter GitHub ID: ")

def getRepos(userID):
    count = 0
    repos = []
    url = "https://api.github.com/users/" + userID + "/repos"
    request = requests.get(url)
    data = request.json()
    
    for repo in data:
        urlCommits = "https://api.github.com/repos/" + userID + "/" + repo["name"] + "/commits"
        requestCommits = requests.get(urlCommits)
        count += 1
        commits = len(requestCommits.json())
        repos.append({"Repo": repo["name"], "Commits": commits})
        print("Repo: " + repo["name"] + " Number of commits: " + str(commits))
        if count == 10:
            break  

    git_info = {
        "id": userID,
        "repoCount": count,
        "repos": repos
    }
    
    return git_info

getRepos(userID)
