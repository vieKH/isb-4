import json


SETTINGS = {
    'hash': 'f56ab81d14e7c55304dff878c3f61f2d96c8ef1f56aff163320e67df',
    "bin": ["477932", "427714", "431417", "477714", "475791", "458450", "477964", "479087", "426101", "419540", "428905"
            , "428906", "458443", "458411", "415482"],
    'last_number': '7819',
    'card_number': 'files/card_number.txt',
    'csv_statistics': 'files/statistics.csv',
    'png_statistics': 'files/statistics.png'
}


if __name__ == "__main__":
    with open('settings.json', 'w') as fp:
        json.dump(SETTINGS, fp)
