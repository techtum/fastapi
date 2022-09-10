from api import app
from fastapi.testclient import TestClient

cl = TestClient(app)
def test_get():
    rs = cl.get('/')
    assert(rs.status_code == 200)
    assert(rs.json() == {'msg': 'Hello, World.'})

if __name__ == '__main__':
    test_get()

