from typing import Callable
from hello_google.models import QueryResult

IWebQuery = Callable[[str], QueryResult]
