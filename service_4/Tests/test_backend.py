import unittest
from flask import url_for 
from flask_testing import TestCase
from application import app, db, routes
from application.models import Teams
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(
            SQLACADEMY_DATABASE_URI = getenv('TEST_SFIA2_PROJECT_DB_URI'),
            SECRET_KEY = getenv('TEST_SECRET_KEY'),
            WTF_CSRF_ENABLED = False,
            DEBUG = True
        )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

    

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestModels(TestBase):
    def test_repr(self):
        team = Teams(teamname = 'ABCDE FC')
        print(repr(team))


class testData(TestBase):
    def test_team(self):
        assert routes.teamname('Boom', 'Xhakalaka') == 'Boom Xhakalaka'
        assert routes.teamname('Pique', 'Control') == 'Pique Control'
        assert routes.teamname('Bacuna', 'Matata' ) == 'Bacuna Matata'