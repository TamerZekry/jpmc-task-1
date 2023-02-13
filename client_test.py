import unittest
import client


class TestClient(unittest.TestCase):
    def test_getRatio(self):
        self.assertEqual(client.getRatio(1, 1), 1)
        self.assertEqual(client.getRatio(1, 2), 0.5)
        self.assertEqual(client.getRatio(1, 3), 0.3333333333333333)
        self.assertEqual(client.getRatio(1, 0), None)
        self.assertEqual(client.getRatio(0, 1), 0)


if __name__ == '__main__':
    unittest.main()
