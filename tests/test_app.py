import os
import pytest

# Set env vars before importing the app
os.environ.setdefault("APP_NAME",    "TestApp")
os.environ.setdefault("APP_ENV",     "testing")
os.environ.setdefault("APP_VERSION", "0.0.1")
os.environ.setdefault("APP_PORT",    "5000")
os.environ.setdefault("APP_AUTHOR",  "Tester")
os.environ.setdefault("SECRET_KEY",  "test-secret")

from app import app  # noqa: E402

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

# ── / ─────────────────────────────────────────────────────────────────────────

class TestIndexRoute:

    def test_returns_200(self, client):
        res = client.get("/")
        assert res.status_code == 200

    def test_content_type_is_html(self, client):
        res = client.get("/")
        assert "text/html" in res.content_type

    def test_app_name_displayed(self, client):
        res = client.get("/")
        assert b"TestApp" in res.data

    def test_app_version_displayed(self, client):
        res = client.get("/")
        assert b"0.0.1" in res.data

    def test_app_env_displayed(self, client):
        res = client.get("/")
        assert b"testing" in res.data

    def test_app_author_displayed(self, client):
        res = client.get("/")
        assert b"Tester" in res.data


# ── /health ───────────────────────────────────────────────────────────────────

class TestHealthRoute:

    def test_returns_200(self, client):
        res = client.get("/health")
        assert res.status_code == 200

    def test_content_type_is_json(self, client):
        res = client.get("/health")
        assert res.content_type == "application/json"

    def test_status_is_ok(self, client):
        res = client.get("/health")
        data = res.get_json()
        assert data["status"] == "ok"

    def test_returns_app_name(self, client):
        res = client.get("/health")
        data = res.get_json()
        assert data["app"] == "TestApp"

    def test_returns_version(self, client):
        res = client.get("/health")
        data = res.get_json()
        assert data["version"] == "0.0.1"


# ── env variable overrides ────────────────────────────────────────────────────

class TestEnvOverrides:

    def test_custom_app_name_reflected(self, monkeypatch):
        monkeypatch.setenv("APP_NAME", "OverriddenApp")
        # Re-import to pick up new env value
        import importlib
        import app as app_module
        importlib.reload(app_module)
        assert app_module.APP_NAME == "OverriddenApp"

    def test_custom_secret_key_reflected(self, monkeypatch):
        monkeypatch.setenv("SECRET_KEY", "new-secret-xyz")
        import importlib
        import app as app_module
        importlib.reload(app_module)
        assert app_module.SECRET_KEY == "new-secret-xyz"

    def test_port_is_integer(self):
        from app import APP_PORT
        assert isinstance(APP_PORT, int)