# Repository Maintainer Checklist

Baseline for a clean, publishable Python repo for ait-testbed repository maintainers. Generate a new repo with this cookiecutter template, see [README.md](README.md).

## Top-level files

- [ ] `README.md`: one-paragraph description, logo/diagram, requirements (Python version, system libs), install (uv, Docker if shipped), quickstart, dev setup, link to docs, contributing, license, security
- [ ] `LICENSE` (or `LICENSE.md`): matches `license` in `pyproject.toml`
- [ ] `SECURITY.md`: supported versions table, reporting contact (aecid@ait.ac.at)
- [ ] `CODE_OF_CONDUCT.md`: link to the [PyPA Code of Conduct](https://www.pypa.io/en/latest/code-of-conduct/)
- [ ] `CONTRIBUTING.md` (or a docs page linked from README): branching model, PR target branch, how to run hooks and tests
- [ ] `.gitignore`, `.dockerignore` (if there is a Dockerfile)
- [ ] No stray files committed: logs, `*.pem`, `.env`, etc.

## Python and uv

- [ ] `.python-version` consistent with `requires-python` and the CI Python version
- [ ] `uv.lock` committed and up to date (`uv lock --check` in CI)
- [ ] Dev tooling in `[dependency-groups] dev`, optional features in `[project.optional-dependencies]`
- [ ] Setup is `uv run` (syncs the environment on first use), documented in README
- [ ] Runtime deps do not contain test or type-stub packages (`pytest-mock` etc.)

## pyproject.toml metadata

- [ ] `name`, `description`, `readme`, `requires-python`
- [ ] `authors` / `maintainers`
- [ ] `license` (SPDX string, e.g. `license = "GPL-3.0-only"`) and `license-files`
- [ ] `keywords`
- [ ] `[project.urls]`: Homepage, Documentation, Repository, Issues, Changelog
- [ ] Version: single source (`dynamic = ["version"]` from a module attr, or  git tags
- [ ] `[project.scripts]` entry points
- [ ] Tool config centralised here where possible (mypy, pytest, coverage)

## Code quality

- [ ] `.pre-commit-config.yaml` run via prek: whitespace/EOF, check-yaml/toml, large files, merge conflicts, autoflake, isort, autopep8/flake8 (or ruff), mypy, docformatter, bandit, deptry
- [ ] use `prek autoupdate`
- [ ] Consistent line length 110  
- [ ] Tests under `tests/`, runnable with `uv run pytest`, coverage reported

## .github/

- [ ] `dependabot.yml`: `uv` ecosystem, plus `github-actions` and (if there is a Dockerfile) `docker` ecosystems, weekly
- [ ] `ISSUE_TEMPLATE/`: bug report, feature request, `config.yml` with `blank_issues_enabled: false` 
- [ ] `pull_request_template.md`

## Workflows

- [ ] CI (`python-app.yml`): on push/PR to `main` and `development`, uv with cache, `prek run -a`, `pytest`
- [ ] Python version matrix if multiple versions are supported
- [ ] Docs (`publish-docs.yml`): build on push and release, deploy to `gh-pages` (mike for MkDocs)
- [ ] PyPI publish on release via trusted publishing (`id-token: write`, `pypa/gh-action-pypi-publish`), build with `uv build`
- [ ] Actions pinned to current major versions or SHAs
- [ ] CodeQL or other security scanning (optional)

## Docs and GitHub Pages

- [ ] MkDocs config committed (`mkdocs.yml`)
- [ ] Versioned docs: `latest` alias for releases, branch builds for `main` / `development`, root redirects to default version
- [ ] Pages enabled on `gh-pages` branch
- [ ] minimum Sections: installation, configuration, usage, development, contribution, release process

## GitHub repo settings

- [ ] About: description, website (Pages URL), topics
- [ ] Branch protection on `main`: required checks, PR reviews, no force push, no deletion
- [ ] Branch protection on `development`: required checks, PR reviews, no force push, but deletion allowed (the release merge deletes it, `recreate-development-branch.yml` recreates it)
- [ ] "Automatically delete head branches" enabled
- [ ] Default PR branch `development` if using git-flow
- [ ] Dependabot alerts, secret scanning enabled
- [ ] Releases with semantic versioning tags (`vX.Y.Z`) and generated notes
