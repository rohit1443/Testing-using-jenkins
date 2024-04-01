import unittest
import requests

class TestWebsiteLoading(unittest.TestCase):
    "Class to unit check the loading of atg.world website"

    def test_website_loading(self):
        "Unit test to check if the atgw.wworld website loads properly"
        
        print("Testing if atg.world website loads...")

        website_url = "https://atgm.worldm"
        response = requests.get(website_url)
        
        self.assertEqual(response.status_code, 200, f"Failed to load website: {website_url}")

        print("Website loading test completed.")

if __name__ == '__main__':
    unittest.main()
