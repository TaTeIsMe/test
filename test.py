import requests
from datetime import datetime, timedelta, timezone

# --- CONFIG ---
OWNER = "TaTeIsMe"
REPO = "test"
TOKEN = ""

# --- GET TODAY'S DATE RANGE IN UTC ---
today = datetime.now(timezone.utc).date()
tomorrow = today + timedelta(days=1)

since = f"{today}T00:00:00Z"
until = f"{tomorrow}T00:00:00Z"

# --- BUILD URL ---
url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"
params = {
    "since": since,
    "until": until
}

headers = {
    "Accept": "application/vnd.github+json"
}

if TOKEN:
    headers["Authorization"] = f"Bearer {TOKEN}"

# --- SEND REQUEST ---
response = requests.get(url, params=params, headers=headers)

output = ""

# --- CHECK & PRINT RESULT ---
if response.status_code == 200:
    commits = response.json()
    for c in commits:
        message = c["commit"]["message"].split("\n")[0]
        author = c["commit"]["author"]["name"]
        output= output + f"\n {author}: {message}"
else:
    print("Error:", response.status_code, response.text)
