# -*- coding: utf-8 -*-
""" This module contains input processors for items loaders. """


from string import ascii_letters, digits
from re import match, sub
from time import strptime
from unicodedata import normalize
from datetime import datetime


NOTHING = ''
SEPERATOR = '-'
MULTIPLE_SEPERATORS = '%s{2,}' % SEPERATOR
BLANK_EDGES = r'^-|-$'

AUTHOR = r'(?P<author>^.+?)(?= on)'
DATE = r'(?:.*)(?P<date>\d{2}\.\d{2}\.\d{4})'
PRICE = r'(?P<price>(\d+\.)*\d+,\d{2})'


def parse_author(author_and_date):
    return match(AUTHOR, author_and_date).group('author')

def parse_date(author_and_date):
    return datetime(*strptime(match(DATE, author_and_date).group('date'), '%d.%m.%Y')[0:6])

def trim_edges(input_string):
    return sub(BLANK_EDGES, NOTHING, input_string)

def squeeze_seperators(input_string):
    return sub(MULTIPLE_SEPERATORS, SEPERATOR, input_string)

def slugify(dirty_string):
    return NOTHING.join([c if c in ascii_letters + digits else SEPERATOR for c in dirty_string])

def asciify(unicode_string):
    return normalize('NFKD', unicode_string).encode('ASCII', 'ignore')

def force_lower(input_string):
    return input_string.lower()

def parse_price(raw_price):
    return float(match(PRICE, raw_price).group('price').replace('.', NOTHING).replace(',', '.'))

def strip_edges(input_string):
    return input_string.strip()

def parse_stock(input_string):
    return bool('stock' in input_string)

def parse_rating(rating_string):
    return int(rating_string[0])

if __name__ == '__main__':
    """ Test the module. """
    print(parse_date('lklk lrjkvfvfv.. on  hkfr 02.12.2344'))
