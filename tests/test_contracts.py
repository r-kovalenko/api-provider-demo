import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.main import app, v1, v2

client = TestClient(app)


@pytest.mark.parametrize("version,field", [("v1", "name"), ("v2", "full_name")])
def test_versioned_customer_response(version, field):
    response = client.get(f"/{version}/customers/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, field: "Demo Customer"}


@pytest.mark.parametrize("version", ["v1", "v2"])
def test_unknown_customer_is_not_found(version):
    assert client.get(f"/{version}/customers/99").status_code == 404


@pytest.mark.parametrize("version,api", [("v1", v1), ("v2", v2)])
def test_checked_in_contract_matches_implementation(version, api):
    path = Path(__file__).resolve().parents[1] / "contracts" / f"{version}.json"
    assert json.loads(path.read_text()) == api.openapi()
