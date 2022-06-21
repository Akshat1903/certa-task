import json
import requests
import base64
import sys
import os

def check_or_create_creds():
    creds_path = os.path.join(os.getcwd(), 'creds.json')
    exist = os.path.exists(creds_path)
    if not exist:
        temp_github_json = {"client_id": "", "client_secret": ""}
        with open(creds_path, "w") as outfile:
            outfile.write(json.dumps(temp_github_json, indent = 4))

    with open(creds_path, "r") as f:
        variables = json.load(f)

    return variables

def authenticate():
    creds = check_or_create_creds()
    try:
        c_id = creds["client_id"]
        c_sec = creds["client_secret"]
    except:
        print("Invalid creds file !!")
        sys.exit()

    if not c_id or not c_sec:
        print("Proper credentials not provided !!")
        sys.exit()

    auth_url = "https://accounts.spotify.com/api/token"
    auth = requests.post(
        auth_url,
        headers = {
            "Authorization": "Basic " + base64.b64encode(("%s:%s" % (c_id, c_sec)).encode('utf-8')).decode('utf-8')
        },
        data = {
            "grant_type": "client_credentials"
        }
    )

    if auth.status_code == 400:
        print("Invalid client credentials, please reset it !!")
        sys.exit()

    access_token = auth.json()["access_token"]

    return access_token


