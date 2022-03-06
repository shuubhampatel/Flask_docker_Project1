"""This test the flask page"""


def test_flask_page(client):
    """This makes the flask page"""
    response = client.get("/flask")
    assert response.status_code == 200
    assert b"Lets read about Python/ Flask" in response.data
