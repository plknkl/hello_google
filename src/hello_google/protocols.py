# from typing import Callable
from typing import Protocol
from hello_google.models import QueryResult


# IWebQuery = Callable[[str], QueryResult]

class IWebQuery(Protocol):
    def query(self, path: str) -> QueryResult:
        ...