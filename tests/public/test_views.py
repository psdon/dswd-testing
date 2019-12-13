def test_home(client):
    response = client.get("/")

    assert response.status_code == 200

    # assert b"pic.jpeg" in response.data
    assert b"You are at home" in response.data


def test_sign_in(client):
    response = client.get("/sign-in")

    assert response.status_code == 200
    assert b"Sign In Page" in response.data
