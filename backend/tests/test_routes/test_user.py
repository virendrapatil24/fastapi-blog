def test_create_user(client):
    response = client.post(
        "/v1/user/",
        json={"username": "testuser", "email": "test@test.com", "password": "PASSWORD"},
    )
    assert response.status_code == 201
    assert response.json() == {
        "email": "test@test.com",
        "username": "testuser",
        "is_active": True,
    }

    return
