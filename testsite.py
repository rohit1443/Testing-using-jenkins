import requests
import pytest

def test_website_load():
    url = 'https://www.atg.world'
    print(f"Connecting to {url}...")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print("Website loaded successfully.")
    except requests.RequestException as e:
        pytest.fail(f"Failed to load website: {e}")

if __name__ == "__main__":
    pytest.main([__file__])
