# Python Workspace Template

## Commands

- Install (package, dependencies)

```bash
$ uv sync --all-packages [--dev] [--refresh]
```

- Start

```bash
$ uv run --package <PACKAGE> <COMMAND>
```

- lint/fix/format

```bash
# Lint check
$ uv run ruff check <PACKAGE_DIR>
$ uv run ruff format --check <PACKAGE_DIR>

# Lint fix
$ uv run ruff check -fix <PACKAGE_DIR>

# Format
$ uv run ruff format <PACKAGE_DIR>
$ uv run black <PACKAGE_DIR>
```

- test/coverage

```bash
$ uv run pytest                     # Test (only)
$ uv run coverage run -m pytest     # Test & Coverage
$ uv run coverage html              # Report coverage (HTML)

$ xdg-open htmlcov/index.html       # Linux
$ open htmlcov/index.html           # macOS
$ Start-Process htmlcov/index.html  # PowerShell
```
