import os 
import requests 
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ["REGS_API_KEY"]
BASE = "https://api.regulations.gov/v4"

def get(path, params=None):
    resp = requests.get(f"{BASE}/{path}", headers={"X-Api-Key": API_KEY}, 
                        params=params, timeout=30)
    print("Requests left this hour:", resp.headers.get("X-RateLimit-Remaining"))
    resp.raise_for_status()
    return resp.json()

if __name__ == "__main__":
    data = get("documents", {"filter[docketId]": "FAA-2018-1084"})
    print(data["meta"])

