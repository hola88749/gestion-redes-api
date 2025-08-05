import unittest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"

class TestAPI(unittest.TestCase):

    def test_post_dispositivo(self):
        payload = {"name": "Router", "job": "Switch"}
        res = requests.post(BASE_URL, json=payload)
        self.assertEqual(res.status_code, 201)

    def test_get_dispositivos(self):
        res = requests.get(BASE_URL)
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.json(), list)

    def test_put_dispositivo(self):
        payload = {"name": "RouterX", "job": "Firewall"}
        res = requests.put(f"{BASE_URL}/1", json=payload)
        self.assertEqual(res.status_code, 200)

    def test_delete_dispositivo(self):
        res = requests.delete(f"{BASE_URL}/1")
        self.assertIn(res.status_code, [200, 204])

if __name__ == '__main__':
    unittest.main()
