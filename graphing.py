import logging
import matplotlib.pyplot as plt

logger = logging.getLogger()
logger.setLevel('INFO')


def graphing_and_save(data: dict, filename: str) -> None:
    """
    Фукция для создать график, потом сохранить результаты в файле.
    :param data: Данных
    :param filename: Путь файла
    :return: None.
    """
    fig = plt.figure(figsize=(30, 5))
    plt.ylabel('Time for working, s')
    plt.xlabel('Processes')
    plt.title('Graph')
    pools, work_times = data.keys(), data.values()
    plt.bar(pools, work_times, color='teal', width=0.5)
    plt.savefig(filename)
    logging.info(f'Результаты сохранит в пути "{filename}" успешно')