"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a href="/pylint" class="nav-link navbarcustomfontcolor cent' in response.data
    assert b'<a href="/aaa" class="nav-link navbarcustomfontcolor">AAA testing</a>' in response.data
    assert b'<a href="/oops" class="nav-link navbarcustomfontcolor">OOPs</a>' in response.data
    assert b'<a href="/solid" class="nav-link navbarcustomfontcolor">SOLID</a>' in response.data


def test_request_home(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"IS601 Project2" in response.data


def test_pylint_page(client):
    """This makes the pylint page"""
    response = client.get("/pylint")
    assert response.status_code == 200
    assert b"Lets read about Pylint" in response.data


def test_aaa_page(client):
    """This makes the AAA page"""
    response = client.get("/aaa")
    assert response.status_code == 200
    assert b"Lets read about AAA testing" in response.data


def test_oops_page(client):
    """This makes the OOPs page"""
    response = client.get("/oops")
    assert response.status_code == 200
    assert b"Lets read about OOPs concepts" in response.data


def test_solid_page(client):
    """This makes the SOLID page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b"Lets read about SOLID" in response.data
