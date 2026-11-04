# cookiecutter-ait-ad

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for AIT Python repositories: uv, EUPL-1.2, MkDocs + mike, GitHub workflows, prek/pre-commit, Code of Conduct.

* [repository_checklist.md](repository_checklist.md): what a repo needs
* [{{cookiecutter.repo_name}}/]({{cookiecutter.repo_name}}/): the template

## Usage

Requires cookiecutter >= 2.2, e.g. via `uvx`:

```bash
uvx cookiecutter gh:ait-testbed/cookiecutter-ait-ad
```

Answer the prompts. Without prompts:

```bash
uvx cookiecutter --no-input gh:ait-testbed/cookiecutter-ait-ad \
  project_name=MyProject description="A tool that parses log files." use_pypi=yes
```

The project is created in `./<repo_name>`, which must not exist yet. Afterwards `uv lock` runs if uv is installed. Values must not contain `\` or `"`.

## Variables

| Variable | Default | |
| --- | --- | --- |
| `project_name` | `MyProject` | display name |
| `description` | (required) | one sentence |
| `repo_name` | `project_name` | GitHub repository and output directory name |
| `github_org` | `ait-testbed` | |
| `dist_name` | `project_name` lowercased | PyPI name |
| `package_name` | `dist_name` with `-` replaced by `_` | import name |
| `use_cli` | yes | adds `cli.py`, the `[project.scripts]` entry point and CLI usage docs |
| `cli_name` | `dist_name` | console script, only used with `use_cli` |
| `python_version` | `3.14` (same as `uv init`) | minimum supported, one of 3.10 to 3.14 |
| `author_name`, `author_email` | `aecid`, `aecid@ait.ac.at` | maintainer |
| `use_pypi` | no | adds `python-publish.yml`, the PyPI badge and `pip install` docs |
| `use_docker` | no | adds `Dockerfile`, `.dockerignore`, `docker.yml`, the `docker` Dependabot entry and `docker pull` docs |

The image name is derived as lowercased `github_org/repo_name`.

Existing repo: generate into a scratch directory, copy only the missing files and diff the rest.

## After generating

Work through this once per new repo. `<org>/<repo>` is `github_org/repo_name`.

### Push the code

- [ ] Create an empty repo `<org>/<repo>` on GitHub (no README, license or `.gitignore`, the template has them)
- [ ] Push `main` and create `development` from it (`uv.lock` is already generated, commit it):

  ```bash
  cd <repo>
  git init -b main
  git add -A
  git commit -m "Initial commit from cookiecutter-ait-ad"
  git remote add origin git@github.com:<org>/<repo>.git
  git push -u origin main
  git push origin main:development
  ```

- [ ] Install the hooks locally: `uv run --dev prek install`
- [ ] Check the first CI run ("Python application") and docs run ("Publish Docs") in the Actions tab

### Settings → General

- [ ] Default branch: `development` (PRs target it by default)
- [ ] Pull Requests: enable "Automatically delete head branches"
- [ ] Social preview: upload an image
- [ ] About (gear icon on the repo page): description, website `https://<org>.github.io/<repo>/latest/`, topics

### Settings → Rules → Rulesets (or Branches → branch protection)

- [ ] `main`: require a pull request with at least one approval, require status checks (the `build (3.x)` jobs, selectable after the first CI run), block force pushes, restrict deletions
- [ ] `development`: same, but allow deletion, since merging into `main` deletes it and `recreate-development-branch.yml` recreates it. Do not restrict creation, or the recreate workflow cannot push it

### Settings → Pages

- [ ] Source "Deploy from a branch", branch `gh-pages`, folder `/ (root)` (the branch exists after the first "Publish Docs" run)

### Settings → Advanced Security

- [ ] Dependabot alerts and Dependabot security updates
- [ ] Secret scanning and push protection
- [ ] Leave private vulnerability reporting off: security issues are reported as public bug reports (see `SECURITY.md`)

### Fill in the template TODOs

- [ ] `docs/configuration.md`, `docs/usage.md`, the overview image comment in `README.md`
- [ ] `keywords` in `pyproject.toml`

### PyPI (only with `use_pypi`)

- [ ] On pypi.org: add a trusted publisher (Your projects → Publishing, or a "pending publisher" if the project does not exist yet): owner `<org>`, repo `<repo>`, workflow `python-publish.yml`, environment `pypi`
- [ ] On GitHub: Settings → Environments → create `pypi`, optionally with required reviewers. GitHub would create it on the first run, but until it exists the VS Code GitHub Actions extension reports "Value 'pypi' is not valid"

### Docker (only with `use_docker`)

- [ ] After the first release: the image `ghcr.io/<org>/<repo>` (lowercased) is private by default. In the org's Packages tab, open it → Package settings → change visibility to public and check it is linked to the repo

PyPI and Docker publishing only run when a GitHub release is published. To make releases without publishing, disable "Upload Python Package" or "Create and publish a Docker image" in the Actions tab (workflow → ··· → Disable workflow).

### First release

- [ ] Publish it following `docs/release.md`, then check all release workflows succeeded in the Actions tab
- [ ] Run `uv run mike set-default --push latest` once, so the docs root redirects to the latest release
