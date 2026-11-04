"""Command line entry point."""
import argparse

from {{ cookiecutter.package_name }}.metadata import __version__


def main() -> None:
    parser = argparse.ArgumentParser(prog='{{ cookiecutter.cli_name }}', description="{{ cookiecutter.description }}")
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    parser.parse_args()


if __name__ == '__main__':
    main()
