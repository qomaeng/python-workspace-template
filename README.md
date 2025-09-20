# Python Workspace Template

## Commands

- Install (package, dependencies)

```bash
$ uv sync --all-packages [--group dev]
```

- Start

```bash
$ uv run --package <PACKAGE> <COMMAND>
```

- lint/fix/format

```bash
$ uv run ruff check <PACKAGE_DIR>
$ uv run ruff format --check <PACKAGE_DIR>

$ uv run ruff check -fix <PACKAGE_DIR>

$ uv run ruff format <PACKAGE_DIR>
$ uv run black <PACKAGE_DIR>
```
