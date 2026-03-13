from fastapi.testclient import TestClient
from app.main import app

Test= TestClient()

def test_home():
    res= client.get("/")
    assert.res.status_code==200