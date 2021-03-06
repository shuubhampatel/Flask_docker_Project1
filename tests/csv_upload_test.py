"""csv file upload test"""
import os
from app.songs.forms import csv_upload
import csv
from app.db.models import User, Song
from app import db


def test_csv_upload(client, add_user, application):
    with application.app_context():
        user = User('test@test.com', 'test1234')
        filepath = 'tests/csvtest.csv'
        with open(filepath) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                testvar = row
            assert testvar == {'Artist': 'xyz', 'Genre': 'pop', 'Name': 'abc', 'Year': '2022'}
