"""This test the docker page"""


def test_docker_page(client):
    """This makes the docker page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Lets read about Docker" in response.data
