def test_root(client_fixture):
    response = client_fixture.simulate_get('/')
    assert response.status_code == 200
    assert response.json == {'message': 'Welcome to Falcon API'}
