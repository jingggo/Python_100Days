"""
读写JSON文件

@Author:jyang
@Date:5/18/2019
"""

import json


def main():
    mydict = {
        'name': 'Phoebe',
        'age': 18,
        'qq': 233333,
        'friends': ['Joe', 'Rachel'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(mydict, f)
    except IOError as e:
        print(e)
    print('Data is saved.')


if __name__ == '__main__':
    main()
