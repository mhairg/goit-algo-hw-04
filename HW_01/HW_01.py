# HW_01.py

import pathlib


def total_salary(path: str) -> tuple:
    """
    Calculate and print the total and average salary values based on the
    data read from the file, or an error message.
    :param path: Path to the data file.
    :return: Tuple with the sum of salaries and average salary.
    """
    if not pathlib.Path(path).is_file(): # not isinstance(path, str) or
        print(f'ПОМИЛКА. Шлях до файлу або формат файлу невалідні: {path}')
        return 0, 0

    try:
        with open(path, encoding='UTF-8') as file:
            salaries = 0
            names = []
            for line in file:
                try:
                    name, salary = line.split(',')
                    salaries += float(salary)
                    names.append(name)
                except ValueError:
                    print(f'ПОМИЛКА. Дані в рядку невалідні (пропущено): '
                          f'{line}')
                    continue
            try:
                avg_salary = salaries / len(names)
            except ZeroDivisionError:
                print(f'ПОМИЛКА. Файл пустий: {file}')
                avg_salary = 0
        return salaries, avg_salary
    except FileNotFoundError:
        print(f'ПОМИЛКА. Файл не знайдено: {path}')
        return 0, 0


try:
    total, average = total_salary('salary_file.txt')
    print(f"Загальна сума заробітної плати: {total}\n"
          f"Середня заробітна плата: {average}")
except TypeError:
    print(f'ПОМИЛКА. Шлях до файлу не вказано')