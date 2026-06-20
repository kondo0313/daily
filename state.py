import sys, os, json, urllib.request

GIST_ID = os.environ["GIST_ID"]
TOKEN   = os.environ["GIST_TOKEN"]
FILE    = "system-state.json"
API     = f"https://api.github.com/gists/{GIST_ID}"

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json",
    "Content-Type": "application/json",
}

def get():
    req = urllib.request.Request(API, headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        data = json.load(r)
    content = data["files"][FILE]["content"]
    print(content)

def set_state(body):
    payload = json.dumps({"files": {FILE: {"content": body}}}).encode()
    req = urllib.request.Request(API, data=payload, headers=HEADERS, method="PATCH")
    with urllib.request.urlopen(req) as r:
        json.load(r)
    print("ok")

if __name__ == "__main__":
    if sys.argv[1] == "get":
        get()
    elif sys.argv[1] == "set":
        set_state(sys.argv[2])
    else:
        print("usage: python state.py get | python state.py set '<json>'")
