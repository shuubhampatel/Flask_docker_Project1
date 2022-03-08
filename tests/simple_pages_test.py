"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a href="/git" class="nav-link navbarcustomfontcolor">Git</a>' in response.data
    assert b'<a href="/docker" class="nav-link navbarcustomfontcolor">Docker</a>' in response.data
    assert b'<a href="/flask" class="nav-link navbarcustomfontcolor">Python/ ' in response.data
    assert b'<a href="/cicd" class="nav-link navbarcustomfontcolor">CI/CD</a>' in response.data


def test_request_example(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Home Page" in response.data


def test_git_page(client):
    """This makes the git page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Lets read about Git" in response.data


def test_docker_page(client):
    """This makes the docker page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Lets read about Docker" in response.data


def test_flask_page(client):
    """This makes the flask page"""
    response = client.get("/flask")
    assert response.status_code == 200
    assert b"Lets read about Python/ Flask" in response.data


def test_cicd_page(client):
    """This makes the ci/cd page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"Lets read about CI/CD" in response.data
