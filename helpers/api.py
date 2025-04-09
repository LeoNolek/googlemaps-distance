import requests

class Api:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            return response
        except requests.RequestException as e:
            print(f"GET request failed: {e}")
            return None
        
    def post(self, endpoint, data=None, json=None, headers=None, params=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.post(url, data=data, json=json, headers=headers, params=params)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            return response
        except requests.RequestException as e:
            print(f"POST request failed: {e}")
            return None