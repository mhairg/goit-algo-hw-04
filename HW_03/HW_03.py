# HW_03.py

import sys
import pathlib
import colorama


def display_parent_directory(path):
    """
    Return the formatted representation of the directory to be displayed
    as the root for the directory tree.
    :param path: Path to the directory to be displayed with its content.
    :return: Formatted directory name.
    """
    return f'{colorama.Fore.BLUE}{path.name}/{colorama.Style.RESET_ALL}'


def display_directory_content(path: str | pathlib.Path, indent=0) \
        -> str | None:
    """
    Return the formatted representation of the directory and its content.
    :param path: Path to the directory to be displayed with its content.
    :param indent: Prefix to be used for indenting data objects based on
    their type.
    :return:
    """
    items = sorted(pathlib.Path(path).iterdir(),
                   key=lambda p: (not p.is_dir(), p.name.casefold()))
    output = ''

    for el in items:
        if el.is_dir():
            output += (f'  {'  ' * indent}{colorama.Fore.GREEN}'
                       f'{el.name}/{colorama.Style.RESET_ALL}\n')
            output += display_directory_content(el, indent + 1)
        else:
            output += (f'  {'  ' * indent}{colorama.Fore.YELLOW}'
                       f'{el.name}{colorama.Style.RESET_ALL}\n')
    return output


def main() -> str:
    """
    Verify the validity of the path passed as the command-line argument
    and the presence of the directory ot interest, and print a
    formatted, tree-like representation of its content.
    :return: The directory tree or an error message.
    """
    try:
        path_obj = pathlib.Path(sys.argv[1])
        if not path_obj.exists():
            return f'The path is invalid: {path_obj}'
        elif not path_obj.is_dir():
            return f'The data object is not a directory: {path_obj.name}'
        else:
            return (f'{display_parent_directory(path_obj)}\n'
                    f'{display_directory_content(path_obj)}')
    except IndexError:
        return 'The path is missing.'


if __name__ == "__main__":
    print(main())
