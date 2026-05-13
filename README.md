# PaaS Test App


Small FastAPI service for validating deployer workflows.

## Endpoints

- `GET /` returns a stable placeholder payload with service name, version, and environment.
- `GET /health` returns the health contract used by `deployer.yml`.
- `GET /version` returns version metadata for deployment checks.

## Local Development

Use the virtual environment directly:

```bash
make install
make test
make run
```

Validate the deployer manifest from this directory:

```bash
make validate
```

Runtime variables:

- `APP_VERSION`, default `0.2.0`
- `APP_ENV`, default `local`
