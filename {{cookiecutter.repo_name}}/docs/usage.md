# Usage

{% if cookiecutter.use_cli -%}
```bash
uv run {{ cookiecutter.cli_name }} --help
```
{%- else -%}
```python
import {{ cookiecutter.package_name }}
```
{%- endif %}
