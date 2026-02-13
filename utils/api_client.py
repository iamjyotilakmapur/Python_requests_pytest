import requests
from config.config import Config


class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = {
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=self.headers)
        return response

    def post(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.post(url, json=data, headers=self.headers)
        return response
    
    def put(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.put(url, json=data, headers=self.headers)
        return response
    
    def delete(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.delete(url, json=data, headers=self.headers)
        return response
