def luhn_algorithm(card_number: str) -> bool:
    """
    Функция для проверить нормер карты по алгоритме Luhn
    :param card_number: номер катры
    :return: результат проверки
    """
    tmp = list(map(int, card_number))[::-1]
    for i in range(1, len(tmp), 2):
        tmp[i] *= 2
        if tmp[i] > 9:
            tmp[i] = tmp[i] % 10 + tmp[i] // 10
    return sum(tmp) % 10 == 0

