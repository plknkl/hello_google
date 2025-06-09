from hello_google.adapters.usecases import query_web

def test_google():
    response = query_web("https://www.google.com")
    assert response.code == "200"