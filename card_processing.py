import multiprocessing as mp
from tqdm import tqdm
from typing import Optional, Union
import hashlib

CORES = mp.cpu_count()


def check_card(main_card: int, hash: str, bins: tuple, last_numbers: str) -> Union[str, bool]:
    for card in bins:
        card = f'{card}{main_card:06d}{last_numbers}'
        if hashlib.sha3_224(card.encode()).hexdigest() == hash:
            return card
    return False


def processing_card(hash: str, bins: list, last_numbers: str, pools=CORES) -> Optional[str]:
    arguments = []
    for i in range(1000000):
        arguments.append((i, hash, bins, last_numbers))
    with mp.Pool(processes=pools) as p:
        for res in p.starmap(check_card, tqdm(arguments, desc='Процесс :', ncols=120)):
            if res:
                p.terminate()
                return res
    return None
