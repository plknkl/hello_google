from hello_google.models import QueryResult
from hello_google.protocols import IWebQuery
from hello_google.adapters.usecases import WebQuery


def main():
    web_client: IWebQuery = WebQuery()
    result: QueryResult = web_client.query("http://www.google.com")
    print(result.code)
    print(result.message)
     
if __name__ == "__main__":
    main()