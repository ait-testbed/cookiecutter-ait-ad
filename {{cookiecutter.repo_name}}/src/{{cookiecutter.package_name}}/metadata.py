"""Package metadata, single source of truth for the version."""
__authors__ = ["{{ cookiecutter.author_name }}"]
__contact__ = "{{ cookiecutter.author_email }}"
__copyright__ = 'Copyright {% now "local", "%Y" %}, AIT Austrian Institute of Technology GmbH'
__date__ = '{% now "local", "%Y/%m/%d" %}'
__deprecated__ = False
__email__ = "{{ cookiecutter.author_email }}"
__license__ = 'EUPL-1.2'
__maintainer__ = "{{ cookiecutter.author_name }}"
__status__ = 'Development'
__version__ = '0.1.0'
__version_string__ = (
    f'(Austrian Institute of Technology)\t'
    f'Version: {__version__}')
__all__ = [
    '__authors__',
    '__contact__',
    '__copyright__',
    '__date__',
    '__deprecated__',
    '__email__',
    '__website__',
    '__license__',
    '__maintainer__',
    '__status__',
    '__version__',
    '__version_string__']
