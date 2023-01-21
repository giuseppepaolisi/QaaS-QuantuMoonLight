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


class TestList(TestCase):
    def setUp(self):
        super().setUp()
        app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        tester = app.test_client(self)
        with app.app_context():
            db.create_all()
            user1 = User(
                email="mariorossi12@gmail.com",
                password="prosopagnosia",
                username="Antonio de Curtis ",
                name="Antonio",
                surname="De Curtis",
                token="43a75c20e78cef978267a3bdcdb0207dab62575c3c9da494a1cd344022abc8a326ca1a9b7ee3f533bb7ead73a5f9fe519691a7ad17643eecbe13d1c8c4adccd2"
            )
            user2 = User(
                email="giuseppeverdi@gmail.com",
                password="asperger",
                username="giuVerdiProXX",
                name="Giuseppe",
                surname="Verdi",
                token="43a75c20e78cef978267a3bdcdb0207dab62575c3c9da494a1cd344022abc8a326ca1a9b7ee3f533bb7ead73a5f9fe519691a7ad17643eecbe13d1c8c4adccd2"
            )
            art1 = Article(
                email_user="mariorossi12@gmail.com",
                title="BuonNatale",
                author = "Antonio de Curtis ",
                body="primobody",
                category="primaCat",
                data=datetime(2021, 12, 25),
                authorized=True,
                label="article"
            )
            art2 = Article(
                email_user="mariorossi12@gmail.com",
                title="BuonCapodanno",
                author="Antonio de Curtis ",
                body="secondoBody",
                category="secondaCat",
                data=datetime(2022, 1, 1),
                authorized = True,
                label = "article"
            )
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()
            db.session.add(art1)
            db.session.add(art2)
            db.session.commit()

    def test_listUser(self):
        """
        test the functionality of getting all registered users to the site
        """
        tester = app.test_client()
        with app.app_context():
            db.create_all()
        response = tester.post(
            "/gestione/",
            data=dict(scelta="listUser"),
        )
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertTrue(User.query.filter_by(email="mariorossi12@gmail.com").first())
        self.assertTrue(User.query.filter_by(email="giuseppeverdi@gmail.com").first())
        db.session.commit()

    def test_listArticlesUser(self):
        """
        test the functionality of getting articles written by a user
        """
        tester = app.test_client()
        with app.app_context():
            db.create_all()
        response = tester.post(
            "/gestione/",
            data=dict(
                scelta="listArticlesUser",
                email="mariorossi12@gmail.com",
            ),
        )
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertTrue(
            Article.query.filter_by(
                email_user="mariorossi12@gmail.com"
            ).limit(2)
        )
        db.session.commit()

    def test_listArticlesData(self):
        """
        tests the functionality of getting articles written between two dates
        """
        tester = app.test_client()
        with app.app_context():
            db.create_all()
        response = tester.post(
            "/gestione/",
            data=dict(
                scelta="listArticlesData",
                firstData="2021-12-20",
                secondData="2021-12-30",
            ),
        )
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertTrue(
            Article.query.filter(
                Article.data.between("2021-12-20", "2021-12-30")
            ).first()
        )
        db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.drop_all()
