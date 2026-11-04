# Installation

Requires Python >= {{ cookiecutter.python_version }}.

## uv

```bash
git clone https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}.git
cd {{ cookiecutter.repo_name }}
{% if cookiecutter.use_cli %}uv run {{ cookiecutter.cli_name }} --help{% else %}uv run python -c "import {{ cookiecutter.package_name }}; print({{ cookiecutter.package_name }}.__version__)"{% endif %}
```
{%- if cookiecutter.use_pypi %}

## pip

```bash
pip install {{ cookiecutter.dist_name }}
```
{%- endif %}
{%- if cookiecutter.use_docker %}

## Docker

```bash
docker pull ghcr.io/{{ cookiecutter.__image_name }}:latest
```
{%- endif %}
