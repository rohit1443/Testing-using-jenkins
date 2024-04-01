import requests
import unittest

website_url = "https://atgm.world"  # Corrected the domain name

class TestWebsiteLoading(unittest.TestCase):

    def test_website_loading(self):
        print("Testing if atgm.world website loads...")
        response = requests.get(https://atg.world/)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
