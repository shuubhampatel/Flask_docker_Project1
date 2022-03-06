"""This test the bootstrap page"""


def test_bootstrap_page(client):
    """This makes the bootstrap page"""
    response = client.get("/bootstrap")
    assert response.status_code == 200
    assert b"Lets read about Bootstrap" in response.data
