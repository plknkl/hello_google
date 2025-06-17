import requests
from functools import partial
from hello_google.models import QueryResult
from hello_google.protocols import IWebQuery

def _query_google(url: str) -> QueryResult:
    response = requests.get(url)
    return QueryResult(response.text, str(response.status_code))

query_web: IWebQuery = partial(_query_google)
