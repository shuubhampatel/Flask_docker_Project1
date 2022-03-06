"""This test the git page"""


def test_git_page(client):
    """This makes the git page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Lets read about Git" in response.data
