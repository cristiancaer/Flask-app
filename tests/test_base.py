
from flask_testing import TestCase
from flask import current_app,url_for
from main import app

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])
    
    def test_index_redirect(self):
        res=self.client.get(url_for('index'))
        self.assertRedirects(res,url_for('hello'))
    def test_hello_get(self):
        res=self.client.get(url_for('hello'))
        self.assert200(res)
    def test_hello_post(self):

        res=self.client.post(url_for('hello'))
        self.assert405(res)
    def test_aut_exist(self):
        self.assertIn('auth',current_app.blueprints)
    def test_auth_login_get(self):
        res=self.client.get(url_for('auth.login'))
        self.assert_200(res)
    def test_auth_log_post(self):
        log={'user':'user',
             'password':'password'
            }
        res=self.client.post(url_for('auth.login'),data=log)
        self.assertRedirects(res,url_for('index'))
    def test_auth_login_tempate(self):
        self.client.get(url_for('auth.login'))
        self.assertTemplateUsed('login.html')