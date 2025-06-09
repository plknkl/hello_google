from hello_google.functions.google import query_google

def main():
    response = query_google()
    print(f"Status code: {response.status_code}")
    print(f"First 100 chars of content: {response.text[:100]}")

if __name__ == "__main__":
    main()
