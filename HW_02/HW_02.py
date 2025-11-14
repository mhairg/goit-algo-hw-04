# HW_02.py

import pathlib


def get_cats_info(path: str) -> list:
    """
    Print a list of dictionaries with pet data based on the data read
    from the file, or an error message.
    :param path: Path to the data file.
    :return: List of dictionaries, each of which contains data for an
    individual pet.
    """
    cat_list = []

    if not pathlib.Path(path).is_file():
        print(f'Invalid file path or file format: {path}')
        return cat_list

    try:
        with open(path, encoding='UTF-8') as file:
            for line in file:
                try:
                    id_num, name, age = line.split(',')
                    cat_list.append({'id': id_num,
                                     'name': name,
                                     'age': age.strip()})
                except ValueError:
                    print(f'Invalid data in line (skipped): {line}')
                    continue
        return cat_list
    except FileNotFoundError:
        print(f'File not found: {path}')
        return cat_list


try:
    cats_info = get_cats_info('cats_file.txt')
    print(cats_info)
except TypeError:
    print(f'Path not specified')
