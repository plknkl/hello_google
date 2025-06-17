from typing import Protocol
from hello_google.models import QueryResult


class IWebQuery(Protocol):
    def query(self, path: str) -> QueryResult:
        ...