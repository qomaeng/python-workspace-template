# Python Workspace Template

## Commands

### Install

Install all workspace packages and dependencies:

```bash
uv sync --all-packages [--dev] [-U] [--refresh]
```

### Add Dependencies

Add a dependency to a workspace package:

```bash
uv add --package <PACKAGE> <DEPENDENCY>
```

Add a development dependency:

```bash
uv add --package <PACKAGE> --dev <DEPENDENCY>
```

Examples:

```bash
uv add --package api-server fastapi
uv add --package api-server --dev pytest
```

After adding a dependency, manage its version constraint in the root `pyproject.toml`:

```toml
[tool.uv]
constraint-dependencies = [
  "fastapi>=0.141.1,<1",
]
```

Workspace packages should generally declare the dependency without duplicating version constraints. Keep shared version policy in the root `constraint-dependencies`.

### Start

Run a command for a workspace package:

```bash
uv run --package <PACKAGE> <COMMAND>
```

### Lint / Fix / Format

```bash
# Lint
uv run ruff check
uv run ruff format --check

# Fix
uv run ruff check --fix

# Format
uv run ruff format

# Type check
uv run basedpyright
```

### Test / Coverage

```bash
# Test
uv run pytest

# Test with coverage
uv run coverage run -m pytest

# Generate HTML coverage report
uv run coverage html
```

Open the coverage report:

```bash
xdg-open htmlcov/index.html       # Linux
open htmlcov/index.html           # macOS
Start-Process htmlcov/index.html  # PowerShell
```
