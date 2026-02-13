import os


class Config:
    ENV = os.getenv("ENV", "dev")

    BASE_URLS = {
        "dev": "https://dev-api.myapp.com",
        "qa": "https://qa-api.myapp.com",
        "prod": "https://api.myapp.com"
    }

    BASE_URL = BASE_URLS.get(ENV)
