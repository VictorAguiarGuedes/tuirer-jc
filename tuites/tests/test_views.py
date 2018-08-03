from django.test import TestCase

class TestPostTuiteView(TestCase):
    def setUp(self):
        super().setUp()
        self.view_url = reverse('tuites:postar')

    def test_status_code_200(self):
        response = self.client.get(self.view_url)