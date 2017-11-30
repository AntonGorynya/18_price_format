import argparse
import itertools
import re


def format_price(price):
    price = str(price)
    point_position = -1
    if re.search(r'\S*([,\.])\S*', price):
        point_position = re.search(r'\S*(?P<pp>[,\.])\S*', price).start('pp')
    if point_position+1:
        price = float(price.replace(',', '.'))
    price = float(price)
    price = '{:,.2f}'.format(price).replace(',', ' ').replace('.00', '')
    return price


def create_parser():
    parser = argparse.ArgumentParser(description='number convert')
    parser.add_argument('number', help='number')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    price = args.number
    print(format_price(price))
