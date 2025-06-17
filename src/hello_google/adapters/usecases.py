import httpx
# from functools import partial
from hello_google.models import QueryResult

# def _query_google(url: str) -> QueryResult:
#     response = requests.get(url)
#     return QueryResult(response.text, str(response.status_code))

# query_web: IWebQuery = partial(_query_google)

class WebQuery:
    def __init__(self) -> None:
        pass

    def query(self, path: str) -> QueryResult:
        response = httpx.get(path)
        return QueryResult(response.text[:40], str(response.status_code))