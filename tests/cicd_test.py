"""This test the ci/cd page"""


def test_cicd_page(client):
    """This makes the ci/cd page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"Lets read about CI/CD" in response.data
