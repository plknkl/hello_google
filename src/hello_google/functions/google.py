import requests

def query_google():
    response = requests.get("https://www.google.com")
    return response