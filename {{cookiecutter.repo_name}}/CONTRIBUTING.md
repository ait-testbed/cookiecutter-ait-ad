# Contributing to {{ cookiecutter.project_name }}

Everyone taking part follows the [Code of Conduct](https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}/blob/main/CODE_OF_CONDUCT.md).

## Branches

* `main`: released code only
* `development`: integration branch, target for all PRs
* Feature branches: `feature/<name>`, bugfix branches: `fix/<name>`, created from `development`

## Workflow

1. Open or pick an issue.
2. Branch from `development`.
3. Set up the dev environment:

   ```bash
   uv run --dev prek install
   ```

4. Make your change, add tests.
5. Run the checks:

   ```bash
   uv run --dev prek run -a
   uv run --dev pytest
   ```

6. Open a PR against `development` and fill in the PR template.

## Releases

See the [release process](https://{{ cookiecutter.github_org }}.github.io/{{ cookiecutter.repo_name }}/latest/release/).
