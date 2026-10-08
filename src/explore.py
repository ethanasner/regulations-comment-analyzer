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

def list_documents(docket_id):
    data = get("documents", {"filter[docketId]": docket_id})
    documents = []
    for doc in data["data"]:
        attrs = doc["attributes"]
        documents.append({
            "id": doc["id"],
            "type": attrs["documentType"],
            "title": attrs["title"],
            "object_id": attrs["objectId"],
            "comment_end_date": attrs["commentEndDate"],
        })
    return documents

if __name__ == "__main__":
    docs = list_documents("FAA-2018-1084")
    for d in docs:
        print(d)
   