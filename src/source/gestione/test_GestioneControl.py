import datetime
from datetime import datetime
from unittest import TestCase
import urllib.parse

from sqlalchemy_utils import database_exists, create_database

from src import app, db
from src.source.model.models import User, Article

params = urllib.parse.quote_plus('Driver={ODBC Driver 18 for SQL Server};Server=tcp:server-sql-qml.database.windows.net,1433;Database=test_db;Uid=rootQML;Pwd=R00t*quantum;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
class TestUser(TestCase):
    def setUp(self):
        super().setUp()
        app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        tester = app.test_client(self)
        with app.app_context():
            db.create_all()
            user = User(
                email="mariorossi12@gmail.com",
                password="prosopagnosia",
                username="Antonio de Curtis ",
                name="Antonio",
                surname="De Curtis",
                token="43a75c20e78cef978267a3bdcdb0207dab62575c3c9da494a1cd344022abc8a326ca1a9b7ee3f533bb7ead73a5f9fe519691a7ad17643eecbe13d1c8c4adccd2"
            )
            db.session.add(user)
            db.session.commit()

    def test_removeUser(self):
        """
        test the removeUser functionality, checking first that the account exists,
        then delete it and verify that it was deleted correctly
        """
        tester = app.test_client(self)
        with app.app_context():
            db.create_all()
            self.assertTrue(
                User.query.filter_by(email="mariorossi12@gmail.com").first()
            )
            response = tester.post(
                "/removeUser/",
                data=dict(email="mariorossi12@gmail.com"),
            )
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)
            self.assertFalse(
                User.query.filter_by(email="mariorossi12@gmail.com").first()
            )
            db.session.commit()

    def test_modifyUser(self):
        """
        test the modifyUser functionality, checking first that the account exists,
        then modify it and verify that it has been modified correctly
        """
        tester = app.test_client()
        with app.app_context():
            db.create_all()
        self.assertTrue(
            User.query.filter_by(email="mariorossi12@gmail.com").first()
        )
        response = tester.post(
            "/ModifyUserByAdmin/",
            data=dict(
                email="mariorossi12@gmail.com",
                token="43a75c20e78cef978267a3bdcdb0207dab62575c3c9da494a1cd344022abc8a326ca1a9b7ee3f533bb7ead73a5f9fe519691a7ad17643eecbe13d1c8c4adccZZ"
            ),
        )
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertTrue(
            User.query.filter_by(
                email="mariorossi12@gmail.com",
                token="43a75c20e78cef978267a3bdcdb0207dab62575c3c9da494a1cd344022abc8a326ca1a9b7ee3f533bb7ead73a5f9fe519691a7ad17643eecbe13d1c8c4adccZZ"
            ).first()
        )
        db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.drop_all()
