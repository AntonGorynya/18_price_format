import argparse
import itertools
import re


def format_price(price):
    price = str(price)
    step = 3
    fractal_len = 2
    start_position = 2
    point_position = -1
    if re.search(r'\S*([,\.])\S*', price):
        point_position = re.search(r'\S*(?P<pp>[,\.])\S*', price).start('pp')
    if point_position+1:
        whole_part = price[:point_position]
        frac_part = price[point_position + 1:][:fractal_len].rstrip('0')
    else:
        whole_part = price
        frac_part = None
    whole_part = list(whole_part)[::-1]
    for position in itertools.islice(itertools.count(),
                                     start_position,
                                     len(whole_part)-1,
                                     step):
        whole_part[position] = ' {}'.format(whole_part[position])
    whole_part = ''.join(whole_part[::-1])
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
