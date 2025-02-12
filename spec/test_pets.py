def test_get_pets(client_fixture, db_user_pets_setup):
    response = client_fixture.simulate_get('/pets')
    assert response.status_code == 200
    pets = response.json
    assert len(pets) == 1
    assert pets[0]['name'] == "Buddy"
    assert pets[0]['species'] == "Dog"