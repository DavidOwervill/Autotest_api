import requests
import pytest

def test_get_methods() -> None:
    response = requests.get("https://httpbin.org/get")
    print(response.status_code)
    print(response.json())
