from hello_google.adapters.usecases import WebQuery

def test_google():
    client = WebQuery()
    response = client.query("https://www.google.com")
    assert response.code == "200"