# {{ cookiecutter.project_name }}

[![CI](https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}/actions/workflows/python-app.yml/badge.svg)](https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}/actions/workflows/python-app.yml)
[![Docs](https://img.shields.io/badge/docs-latest-blue)](https://{{ cookiecutter.github_org }}.github.io/{{ cookiecutter.repo_name }}/latest/)
{%- if cookiecutter.use_pypi %}
[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.dist_name }})](https://pypi.org/project/{{ cookiecutter.dist_name }}/)
{%- endif %}
[![License: EUPL-1.2](https://img.shields.io/badge/license-EUPL--1.2-blue)](LICENSE.md)

{{ cookiecutter.description }}

<!-- ![Overview](docs/images/overview.png) -->

## Requirements

* Python >= {{ cookiecutter.python_version }}
* [uv](https://docs.astral.sh/uv/)

## Setup

With uv:

```bash
git clone https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}.git
cd {{ cookiecutter.repo_name }}
{% if cookiecutter.use_cli %}uv run {{ cookiecutter.cli_name }} --help{% else %}uv run python -c "import {{ cookiecutter.package_name }}; print({{ cookiecutter.package_name }}.__version__)"{% endif %}
```
{%- if cookiecutter.use_pypi %}

With pip:

```bash
pip install {{ cookiecutter.dist_name }}
```
{%- endif %}
{%- if cookiecutter.use_docker %}

With Docker:

```bash
docker pull ghcr.io/{{ cookiecutter.__image_name }}:latest
```
{%- endif %}

## Usage

```bash
{% if cookiecutter.use_cli %}uv run {{ cookiecutter.cli_name }} --help{% else %}uv run python -c "import {{ cookiecutter.package_name }}; print({{ cookiecutter.package_name }}.__version__)"{% endif %}
```

See the [documentation](https://{{ cookiecutter.github_org }}.github.io/{{ cookiecutter.repo_name }}/latest/) for details.

## Developer setup

```bash
uv run --dev prek install
uv run --dev pytest
```

Serve the docs locally:

```bash
uv run --dev mkdocs serve
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the git workflow.
Everyone taking part follows the [Code of Conduct](CODE_OF_CONDUCT.md).

## Security

See [SECURITY.md](SECURITY.md).

## License

[EUPL-1.2](LICENSE.md)
