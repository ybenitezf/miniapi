
def test_api(client):
    rv = client.get('/')
    assert {'message': 'Hello !'} == rv.json
