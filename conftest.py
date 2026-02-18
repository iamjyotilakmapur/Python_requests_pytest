import pytest
from datetime import datetime
import json
import os
from utils.config import Config

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Folder name must match exactly
    report_dir = "Reports"
    os.makedirs(report_dir, exist_ok=True)  # make sure folder exists

    # Timestamp format
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Set the htmlpath for the report
    config.option.htmlpath = os.path.join(report_dir, f"Report_{now}.html")

@pytest_fixture
def load_user_data():
    json_file_path = os.path.join(os.path.dirname(__file__),"data","test_data.json")
    with open(json_file_path) as json_file:
        data = json.file(json_file)
    return data

def pytest_configure():
    print(f"Running tests in environment: {Config.ENV}")
    print(f"Base URL: {Config.BASE_URL}")



