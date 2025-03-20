import requests

CLIENT_ID = "your_client_id"
SECRET_KEY = "your_secret_key"
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

data = {
    "grant_type": "password",
    "username": "your_reddit_username",# replace it with your reddit username
    "password": "your_reddit_password"#replace with your password
}

headers = {"User-Agent": "mental-health-bot/0.1"}

res = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers)

TOKEN = res.json()["access_token"]
print(TOKEN)