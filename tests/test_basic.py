from hello_google.main import query_google

def test_google():
    response = query_google()
    assert response.status_code == 200