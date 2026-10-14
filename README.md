# api-provider-demo

Synthetic customer API with two versions. Version 2 replaces response field `name` with `full_name`, creating a deliberate breaking change. The provider MCP server is planned.

Part of [API Contract Copilot](https://github.com/r-kovalenko/api-contract-copilot). Features and tasks are tracked in the shared GitHub Project and this repository's issues.

## Run and test

Requires Python 3.12.

```sh
python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m ruff check .
python -m ruff format --check .
python -m pytest --cov=app
python -m uvicorn app.main:app --reload
```

The health endpoint is `/health`.

Versioned endpoints: `/v1/customers/1`, `/v2/customers/1`; only synthetic customer `1` exists. OpenAPI fixtures are in `contracts/`; migration context is in `docs/`. Regenerate fixtures from the repository root with `python -m scripts.export_contracts`. Tests verify fixture drift.

## CI and delivery

Pull requests run lint, formatting, pytest with coverage, and container build/smoke tests. Successful main-branch builds publish `ghcr.io/r-kovalenko/api-provider-demo:<commit-sha>`. No server deployment or paid model calls are configured. See [delivery details](https://github.com/r-kovalenko/api-contract-copilot/blob/main/docs/ci-cd.md).

Build locally: `docker build -t api-provider-demo .`, then `docker run --rm -p 8000:8000 api-provider-demo`.

Public visibility does not grant an open-source license; owner selection is pending.

## Coding and security

Project skills are in `.agents/skills/`; repository guidance is in [AGENTS.md](AGENTS.md). Follow the [OWASP control baseline](docs/security.md) and [GitHub environment-secret guide](docs/secrets.md). Required CI includes Gitleaks, Bandit, dependency audits, and CodeQL analysis before image publication.
