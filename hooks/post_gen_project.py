"""Remove opt-out files and generate uv.lock."""
import shutil
import subprocess
from pathlib import Path

remove = []
if not {{ cookiecutter.use_docker }}:
    remove += ['Dockerfile', '.dockerignore', '.github/workflows/docker.yml']
if not {{ cookiecutter.use_cli }}:
    remove += ['src/{{ cookiecutter.package_name }}/cli.py']
if not {{ cookiecutter.use_pypi }}:
    remove += ['.github/workflows/python-publish.yml']
for path in remove:
    Path(path).unlink()

if shutil.which('uv'):
    subprocess.run(['uv', 'lock', '-q'], check=True)
    print('Generated uv.lock')
else:
    print("uv not found, run 'uv lock' manually")

print('Next steps: https://github.com/ait-testbed/cookiecutter-ait-ad#after-generating')
