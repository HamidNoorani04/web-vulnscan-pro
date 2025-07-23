import json
import requests

def save_report(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def login_session(login_url, username, password):
    session = requests.Session()
    data = {"username": username, "password": password}
    session.post(login_url, data=data) 
    return session
