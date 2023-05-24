import json


settings = {
    'hash': 'files/hash.txt',
    'bin': 'files/bin.txt',
    'last_number': 'files/last_number.txt',
    'card_number': 'files/card_number.txt',
    'csv_statistics': 'files/statistics.csv',
    'png_statistics': 'files/statistics.png'
}


if __name__ == "__main__":
    with open('settings.json', 'w') as fp:
        json.dump(settings, fp)