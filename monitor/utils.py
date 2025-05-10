# monitor/utils.py
import requests

def check_leakcheck(email):
    url = "https://leakcheck.io/api/public"
    params = {
        "key": "free",
        "check": email
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        if data.get("success") and data.get("found"):
            return True, data.get("sources", [])
        return False, []
    except Exception as e:
        return None, str(e)
