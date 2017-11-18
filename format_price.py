import argparse
import re


def format_price(price):
    price = str(price)
    step = 3
    fractal_len = 2
    point_position = -1
    if re.search(r'\S*([,\.])\S*', price):
        point_position = re.search(r'\S*(?P<pp>[,\.])\S*', price).start('pp')
    if point_position+1:
        whole_part = price[:point_position]
        frac_part = price[point_position + 1:][:fractal_len].rstrip('0')
    else:
        whole_part = price
        frac_part = None
    out_price = ''
    for position, symbol in enumerate(whole_part[::-1]):
        if position % step != 0:
            out_price += symbol
        else:
            out_price += ' {}'.format(symbol)
    whole_part = out_price[::-1].strip()
    if frac_part:
        return '{}.{}'.format(whole_part, frac_part)
    else:
        return whole_part


def create_parser():
    parser = argparse.ArgumentParser(description='number convert')
    parser.add_argument('number', help='number')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    price = args.number
    print(format_price(price))
