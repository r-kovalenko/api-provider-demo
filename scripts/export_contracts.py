import json
from pathlib import Path

from app.main import v1, v2

destination = Path(__file__).resolve().parents[1] / "contracts"
destination.mkdir(exist_ok=True)
for version, app in [("v1", v1), ("v2", v2)]:
    (destination / f"{version}.json").write_text(
        json.dumps(app.openapi(), indent=2) + "\n", encoding="utf-8"
    )
