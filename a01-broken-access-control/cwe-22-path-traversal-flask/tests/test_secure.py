import pytest
from app_secure import create_app

TRAVERSAL_PAYLOADS = [
    "/download/../.env",
    "/download/../../app_vulnerable.py",
    "/download/../../../config.json",
    "/download/%2e%2e/%2e%2e/.env",
    "/download/%2e%2e/app_vulnerable.py",
    "/download/..//..//config.json",
    "/download/%252e%252e/%252e%252e/.env",
    "/download/....//..//..//pyproject.toml",
]


@pytest.mark.parametrize("payload", TRAVERSAL_PAYLOADS, ids=str)
def test_path_traversal_blocked(payload):
    app = create_app()
    client = app.test_client()

    response = client.get(payload)

    assert response.status_code in (
        403,
        404,
    ), f"La requête {payload} aurait dû être bloquée."


def test_valid_file_allowed(tmp_path):
    safe_file = tmp_path / "allowed.txt"
    safe_file.write_text("OK")

    app = create_app(files_dir=str(tmp_path))  # on injecte tmp_path ici
    client = app.test_client()

    res = client.get("/download/allowed.txt")
    assert res.status_code == 200
    assert b"OK" in res.data


def test_security_logging(caplog):
    """Le logging doit s’activer en cas de tentative de traversal."""

    app = create_app()
    client = app.test_client()

    with caplog.at_level("WARNING"):
        client.get("/download/../../evil.txt")

    assert any(
        "[SECURITY]" in msg for msg in caplog.messages
    ), "Aucun log de sécurité détecté !"
