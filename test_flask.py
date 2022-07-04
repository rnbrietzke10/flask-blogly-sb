from unittest import TestCase

from app import app
from models import db, User, Post

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



class PostViewsTestCase(TestCase):
    """Test User Views"""

    def setUp(self):
        """
        Clear out any existing users
        Add new user
        """

        Post.query.delete()

        new_user = User(first_name="Test", last_name="User", image_url='www.google.com')
        db.session.add(new_user)
        db.session.commit()
        p1 = Post(title="Test Post", content="Testing post functionality", user_id=1)
        db.session.add(p1)
        db.session.commit()


        self.post_id = p1.id
        self.posts = p1


    def tearDown(self):
        """Clean up after test are run"""

        db.session.rollback()

    def test_list_posts(self):
        with app.test_client() as client:
            resp = client.get(f'/users/{1}')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Test Post', html)

    def test_add_new_post_form(self):
        with app.test_client() as client:
            resp = client.get(f'/users/{1}/posts/new')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<button class="btn add">Add</button>', html)


    def test_add_post(self):

        with app.test_client() as client:
            post = {"post-title":"Test2", "post-content":"Testing again", 'user_id':1}
            resp = client.post(f'/users/{1}/posts/new', data=post, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Test2", html)

    def test_post_detail_page(self):
        with app.test_client() as client:
            resp = client.get(f'/posts/{self.post_id}')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h2>Test Post</h2>', html)

