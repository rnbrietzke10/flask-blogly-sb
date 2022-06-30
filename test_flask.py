from unittest import TestCase

from app import app
from models import db, User

# Use test database blogly_user_test
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_user_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
# This is from demo code
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UserViewsTestCase(TestCase):
    """Test User Views"""

    def setUp(self):
        """
        Clear out any existing users
        Add new user
        """

        User.query.delete()

        new_user = User(first_name="Test", last_name="User", image_url='www.google.com')

        db.session.add(new_user)
        db.session.commit()

        self.user_id = new_user.id
        self.user = new_user


    def tearDown(self):
        """Clean up after test are run"""

        db.session.rollback()

    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get('/users')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Test User', html)

    def test_add_new_user_form(self):
        with app.test_client() as client:
            resp = client.get('/users/new')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<button class="btn add">Add</button>', html)


    def test_add_user(self):
        # '/users/new', methods=["POST"]
        with app.test_client() as client:
            user = {"firstName":"Test2", "lastName":"User2", 'imageUrl':'hello.jpg'}
            resp = client.post('/users/new', data=user, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Test2 User2", html)

    def test_user_detail_page(self):
        with app.test_client() as client:
            resp = client.get(f'/users/{self.user_id}')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h2>Test User</h2>', html)



