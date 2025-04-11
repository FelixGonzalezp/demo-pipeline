from django.test import TestCase, Client
from myapp.views import ping



#Test del endpoint ping
class PingTest(TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_endpoint_ping_responde_ping_pong(self):
        response = self.client.get('/ping/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"ping": "pung"})

# Create your tests here.
