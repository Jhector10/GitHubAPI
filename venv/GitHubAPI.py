import requests
import json

userID = input("Enter the GitHub username: ")

def GitHub(userID):
    request = requests.get('https://api.github.com/users/'+userID+'/repos')
    json = request.json()
    for i in range(0, len(json)):
        print("Project Number: ", i+1)
        print("Project Name: ", json[i]['name'])
        print("Project URL: ", json[i]['svn_url'],'\n')
