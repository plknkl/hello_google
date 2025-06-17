from hello_google.adapters.usecases import query_web
from hello_google.models import QueryResult

def main():
    response: QueryResult = query_web("https://www.google.com")
    print(f"Status code: {response.code}")
    print(f"First 100 chars of content: {response.message[:100]}")
     
if __name__ == "__main__":
    main()