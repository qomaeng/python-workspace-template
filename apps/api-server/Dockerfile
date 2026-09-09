FROM python:3.14-slim-bookworm AS builder

WORKDIR /app

RUN pip install --no-cache-dir "uv==0.12.10"

COPY pyproject.toml uv.lock ./
COPY apps/api-server/pyproject.toml ./apps/api-server/pyproject.toml
COPY pkgs/config/pyproject.toml ./pkgs/config/pyproject.toml
COPY pkgs/contract/pyproject.toml ./pkgs/contract/pyproject.toml
COPY pkgs/core/pyproject.toml ./pkgs/core/pyproject.toml
COPY pkgs/error/pyproject.toml ./pkgs/error/pyproject.toml
COPY pkgs/model/pyproject.toml ./pkgs/model/pyproject.toml

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync \
    --frozen \
    --package api-server \
    --no-dev \
    --no-install-workspace

COPY apps/api-server ./apps/api-server
COPY pkgs ./pkgs

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync \
    --frozen \
    --package api-server \
    --no-dev


FROM python:3.14-slim-bookworm AS runtime

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/apps/api-server ./apps/api-server
COPY --from=builder /app/pkgs ./pkgs

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1

CMD ["python", "-m", "api_server"]
