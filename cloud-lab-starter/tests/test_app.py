from app.main import app


def client():
    app.testing = True
    return app.test_client()


def test_home():
    r = client().get("/")
    assert r.status_code == 200
    assert "message" in r.get_json()


def test_health():
    r = client().get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_add():
    r = client().get("/add?a=2&b=3")
    assert r.get_json()["result"] == 5


def test_add_bad_input():
    r = client().get("/add?a=x&b=3")
    assert r.status_code == 400
