import os
import configparser
import requests


def accept(competition):
    parser = configparser.ConfigParser()
    parser.read(os.path.expanduser("~/.kaggle-cli/config"))
    username = parser["user"]["username"]
    password = parser["user"]["password"]

    base_url = "https://www.kaggle.com"

    with requests.Session() as s:
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "UserName": username,
            "Password": password,
            "RememberMe": False,
            "JavaScriptEnabled": True,
        }
        login_url = f"{base_url}/account/login"
        res1 = s.post(login_url, data=data, headers=headers)

        accept_url = f"{base_url}/c/{competition}/rules/accept.json?doAccept=True"
        res2 = s.post(accept_url, data=data)
