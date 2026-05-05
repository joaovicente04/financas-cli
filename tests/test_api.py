import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import get_dollar_rate

def test_get_dollar_rate(monkeypatch):
    # Simula resposta da API
    class MockResponse:
        def json(self):
            return {
                "USDBRL": {
                    "bid": "5.00"
                }
            }

    def mock_get(*args, **kwargs):
        return MockResponse()

    # Substitui requests.get pelo mock
    import requests
    monkeypatch.setattr(requests, "get", mock_get)

    rate = get_dollar_rate()

    assert rate == 5.0