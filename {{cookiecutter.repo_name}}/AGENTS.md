# AGENTS.md

Rules for AI coding agents working in this repository. Humans: see [CONTRIBUTING.md](CONTRIBUTING.md).

This is the single source of agent instructions. `CLAUDE.md` and `GEMINI.md` only import it; edit this file, not them.

## Project

{{ cookiecutter.project_name }}: {{ cookiecutter.description }}

- Python >= {{ cookiecutter.python_version }}, managed with [uv](https://docs.astral.sh/uv/). License EUPL-1.2.
- `src/{{ cookiecutter.package_name }}/`: the package (src layout). {% if cookiecutter.use_cli %}`cli.py` is the `{{ cookiecutter.cli_name }}` entry point, {% endif %}`metadata.py` holds `__version__`.
- `tests/`: pytest tests.
- `docs/`: MkDocs site (`mkdocs.yml`), versioned with mike and published to GitHub Pages.
- `.github/workflows/`: CI, docs{% if cookiecutter.use_pypi %}, PyPI publishing{% endif %}{% if cookiecutter.use_docker %}, Docker image{% endif %} and the `development` branch recreation.

## Commands

Always go through `uv run`, which syncs the environment itself. Do not use `pip`, `uv pip` or a manually activated venv.

```bash
uv run --dev prek run -a                                       # all hooks: lint, format, types, security, deptry
uv run --dev pytest -n auto --cov --cov-report=term-missing    # tests
uv run --dev pytest tests/test_metadata.py::test_version_is_set   # one test
uv run --dev mkdocs build --strict                             # docs
{%- if cookiecutter.use_cli %}
uv run {{ cookiecutter.cli_name }} --help                                # run the CLI
{%- endif %}
```

Before calling a change done, the hooks and the tests must pass. CI runs exactly these, plus `uv lock --check`, on every Python version from {{ cookiecutter.python_version }} up.

## Code rules

- Line length 110. Formatting and imports are fixed by autopep8, isort and autoflake; run the hooks instead of formatting by hand.
- mypy runs `--strict` on `src/`: every function gets full type hints, no untyped `Any` leaks.
- flake8 and bandit must pass. No blanket `# noqa` or `# type: ignore`; if one is unavoidable, name the code (`# noqa: E501`) and say why.
- Module docstrings come first in the file (`check-docstring-first`); docformatter formats them.
- Use `logging` with `logger.warning`, not `logger.warn`.
- Keep the src layout and the existing structure. Do not add new top-level packages, config files or tools without being asked.

## Dependencies

- Runtime dependencies go in `[project] dependencies` in `pyproject.toml`, dev tools in `[dependency-groups] dev`, optional features in `[project.optional-dependencies]`.
- Add them with `uv add <pkg>` / `uv add --dev <pkg>`, never by editing `uv.lock`. Commit the updated `uv.lock`.
- deptry checks that every import is declared and every declared dependency is used. Do not add a dependency for something the standard library or an existing dependency already does.
- Never put test tools or type stubs in runtime dependencies.

## Tests

- Every behaviour change or bug fix comes with a test in `tests/`.
- Tests must not need network access, credentials or files outside the repo.

## Versioning and releases

- The version lives only in `src/{{ cookiecutter.package_name }}/metadata.py` (`__version__`). Do not hard-code it anywhere else.
- Do not bump the version, create tags or releases unless asked. The release process is in `docs/release.md`.

## Git

- git-flow: `main` holds released code, `development` is the integration branch. Branch from `development` as `feature/<name>` or `fix/<name>`; PRs target `development`.
- Do not commit to `main` or `development` directly, do not force-push, do not rewrite published history.
- Fill in `.github/pull_request_template.md` for PRs.

## Documentation

- User-visible changes (CLI options, configuration, installation) update `README.md` and the matching page in `docs/` in the same change.
- New docs pages must be added to `nav` in `mkdocs.yml`.

## Security

- This project is under development: security issues are handled as public bug reports (`SECURITY.md`).
- Never commit secrets, keys, `.env` files or logs (see `.gitignore`).
