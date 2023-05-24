import logging
import json
import csv

logger = logging.getLogger()
logger.setLevel('INFO')


def load_setting(settings_file: str) -> dict:
    try:
        with open(settings_file) as js:
            settings = json.load(js)
        logging.info('Усешно чтении настроек')
    except OSError as err:
        logging.warning(f' Ошибка при чтении настроек из файла {settings_file}\n{err}')
    return settings


def load_file(filename: str) -> str:
    try:
        with open(filename, "r") as f:
            text = f.read()
        logging.info(f'Файл {filename} успешно прочитан')
    except OSError as err:
        logging.warning(f'При чтении файла {filename} ошибка была:\n {err} ')
    return text


def write_file(text:str, filename: str) -> None:
    try:
        with open(filename, "w") as f:
            f.write(text)
        logging.info(f'Сохранить в файле {filename} успешно')
    except OSError as err:
        logging.warning(f'При сохранении в файле {filename} была ошибка :\n {err}')


def read_list(file_name: str) -> list:
    """
    Функция считывает кортеж из файла
    :param file_name: Путь к файлу
    :return: Кортеж
    """
    data = []
    try:
        with open(file_name, 'r') as f:
            data = f.readlines()
            data = list(map(int, data))
        logging.info("Данные успешно считаны")
    except OSError as err:
        logging.warning(f"{err} Не удалось считать данные")
    return data

def load_statistics(file_name: str) -> dict:
    """
    Функция считывает статистику из файла
    :param file_name: Имя файла
    :return: Словарь вида: (количество процессов: время)
    """
    try:
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            stats = list(reader)
        logging.info("Статистика успешно считана")
    except OSError as err:
        logging.warning(f"{err} Не удалось считать статистику")
    result = dict()
    for i in stats:
        processes, time = i
        result[int(processes)] = float(time)
    return result


def write_statistics(processes: int, time: float, file_name: str) -> None:
    """
    Функция записывает статистику в файл
    :param processes:
    :param time:
    :param file_name:
    :return: Функция ничего не возвращает
    """
    try:
        with open(file_name, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([processes, time])
        logging.info("Статистика успешно записана")
    except OSError as err:
        logging.warning(f"{err} Не удалось записать статистику")