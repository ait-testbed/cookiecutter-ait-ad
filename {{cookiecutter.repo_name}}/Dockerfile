FROM ghcr.io/astral-sh/uv:0.11.32 AS uv

FROM python:{{ cookiecutter.python_version }}-slim

WORKDIR /app

# Install into the system site-packages instead of a .venv,
# so the CLI works without activating anything.
ENV UV_PROJECT_ENVIRONMENT=/usr/local

COPY --from=uv /uv /usr/local/bin/uv

COPY pyproject.toml uv.lock README.md LICENSE.md ./

# --locked fails the build if uv.lock is stale.
# --no-install-project keeps this layer cached when only project code changes.
RUN uv sync --locked --no-dev --no-install-project

COPY ./src ./src

RUN uv sync --locked --no-dev

{% if cookiecutter.use_cli %}CMD ["{{ cookiecutter.cli_name }}", "--help"]{% else %}CMD ["python", "-c", "import {{ cookiecutter.package_name }}; print({{ cookiecutter.package_name }}.__version__)"]{% endif %}
