# Development

```bash
uv run --dev prek install
```

Run hooks and tests:

```bash
uv run --dev prek run -a
uv run --dev pytest -n auto --cov --cov-report=term-missing
```

Serve the docs locally:

```bash
uv run --dev mkdocs serve
```

Preview versioned docs (mike) locally:

```bash
uv run --dev mike serve
```
