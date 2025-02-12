def test_get_user_pets(client_fixture, db_user_pets_setup):
    user_id = db_user_pets_setup
    response = client_fixture.simulate_get(f'/users/{user_id}/pets')
    assert response.status_code == 200
    user_pets = response.json
    assert user_pets[0]['name'] == "Buddy"
    assert user_pets[0]['species'] == "Dog"

def test_post_user_pets(client_fixture, db_user_pets_setup):
    user_id = db_user_pets_setup
    new_pet_data = {'name': 'Garfield', 'species': 'Fat Cat'}
    response = client_fixture.simulate_post(f'/users/{user_id}/pets', json=new_pet_data)
    assert response.status_code == 201
    user_pets = response.json
    assert user_pets['name'] == "Garfield"
    assert user_pets['species'] == "Fat Cat"