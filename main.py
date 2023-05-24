from bonus_funcions import load_setting, load_file,  write_file, load_statistics, write_statistics, read_list
from card_processing import processing_card
from luhn import luhn_algorithm
from graphing import graphing_and_save
import time
import logging
import argparse

SETTINGS_FILE = 'settings.json'
logger = logging.getLogger()
logger.setLevel('INFO')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-cus', '--custom', type=str,
                        help='Использует пользовательсткий файл с настройками, необходимо указать путь к файлу')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-crd', '--card_number_enumeration', type=int,
                       help='Ищет номер карты с помощью хеша, необходимо указать количество процессов')
    group.add_argument('-sta', '--statistics',
                       help='Получается статистику подбирая номер карты на разном количестве процессов')
    group.add_argument('-lun', '--luhn_algorithm', help='Проверяет валидность номера карты с помощью алгоритма Луна')
    group.add_argument('-vis', '--visualize_statistics', help='Создает гистограмму по имеющейся статистике')
    args = parser.parse_args()
    if args.custom:
        settings = load_setting(args.custom)
    else:
        settings = load_setting(SETTINGS_FILE)
    if settings:
        if args.card_number_enumeration:
            hash = load_file(settings['hash'])
            bins = read_list(settings['bin'])
            last_four_numbers = load_file(settings['last_number'])
            card_number = processing_card(hash, bins, last_four_numbers, args.card_number_enumeration)
            if card_number:
                logging.info(f"Номер карты успешно найден: {card_number}")
                write_file(str(card_number), settings['card_number'])
            else:
                logging.info("Не удалось найти номер карты")
        elif args.statistics:
            hash = load_file(settings['hash'])
            bins = read_list(settings['bin'])
            last_four_numbers = load_file(settings['last_number'])
            for i in range(1, 21):
                t1 = time.time()
                processing_card(hash, bins, last_four_numbers, i)
                t2 = time.time()
                write_statistics(i, t2 - t1, settings['csv_statistics'])
            logging.info("Статистика успешно посчитана")
        elif args.luhn_algorithm:
            card_number = load_file(settings['card_number'])
            if luhn_algorithm(card_number):
                logging.info("Номер карты действителен")
            else:
                logging.info("Номер карты не действителен")
        elif args.visualize_statistics:
            graphing_and_save(load_statistics(settings['csv_statistics']), settings['png_statistics'])
            logging.info("Гистограмма успешно создана")
