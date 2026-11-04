"""Validate the answers before anything is generated."""
import re
import sys

values = {
    'project_name': r"""{{ cookiecutter.project_name }}""",
    'description': r"""{{ cookiecutter.description }}""",
    'repo_name': r"""{{ cookiecutter.repo_name }}""",
    'github_org': r"""{{ cookiecutter.github_org }}""",
    'dist_name': r"""{{ cookiecutter.dist_name }}""",
    'package_name': r"""{{ cookiecutter.package_name }}""",
    'cli_name': r"""{{ cookiecutter.cli_name }}""",
    'author_name': r"""{{ cookiecutter.author_name }}""",
    'author_email': r"""{{ cookiecutter.author_email }}""",
}

errors = []
for name, value in values.items():
    # values end up inside quoted TOML/YAML/Python strings
    if not value or '\\' in value or '"' in value:
        errors.append(f'{name} must not be empty or contain \\ or "')
# names end up in TOML keys, URLs, image names and shell commands, so restrict them
patterns = {
    'package_name': r'[a-z_][a-z0-9_]*',
    'dist_name': r'[A-Za-z0-9]([A-Za-z0-9._-]*[A-Za-z0-9])?',
    'cli_name': r'[A-Za-z0-9]([A-Za-z0-9._-]*[A-Za-z0-9])?',
    'repo_name': r'[A-Za-z0-9._-]+',
    'github_org': r'[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?',
}
for name, pattern in patterns.items():
    if not re.fullmatch(pattern, values[name]):
        errors.append(f"{name} '{values[name]}' must match {pattern}")

if errors:
    print('error: ' + '\nerror: '.join(errors), file=sys.stderr)
    sys.exit(1)
