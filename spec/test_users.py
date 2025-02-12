def test_get_users(client_fixture):
    response = client_fixture.simulate_get('/users')
    assert response.status_code == 200
    users = response.json
    assert len(users) == 1  # Espera que exista um usuário
    assert users[0]['name'] == "John Doe"
    assert users[0]['email'] == "john.doe@example.com"


def test_post_user(client_fixture):
    new_user_data = {'name': 'Jane Doe', 'email': 'jane.doe@example.com'}
    response = client_fixture.simulate_post('/users', json=new_user_data)
    assert response.status_code == 201
    new_user = response.json
    assert new_user['name'] == 'Jane Doe'
    assert new_user['email'] == 'jane.doe@example.com'