#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import codecs

products = []
listings = {}
results = []


def read_source():
    '''Read source files.

    Returns:
        products (list): list of product dictionaries.
        listings (dict): listings dictionary indexed by manufacturer.
    '''
    with codecs.open('products.txt', encoding='ascii') as products_file:
        for product in products_file:
            products.append(json.loads(product))

    with codecs.open('listings.txt', encoding='utf-8') as listings_file:
        for _listing in listings_file:
            listing = json.loads(_listing)
            manufacturer = listing['manufacturer'].lower() or u'brandless'

            if manufacturer in listings:
                listings[manufacturer].append(listing)
            else:
                listings[manufacturer] = [listing]

    return products, listings


def listing_is_product(listing, product):
    '''Simple Matching Algorithm.

    Params:
        listing (dict): listing from listings.txt
        product (dict): product from products.txt

    Returns:
        bool: True if listing and product match, False otherwise.
    '''
    title = listing['title'].lower().replace('-', '')
    family = product.get('family', '').lower().replace('-', '')
    model = product['model'].lower().replace('-', '')

    if model in title:
        if family and family in title:
            return True
    return False


def find_results():
    '''
    TODO Write docstring
    '''
    _results = {}

    for product in products:
        _listings = listings.get(product['manufacturer'].lower(), [])
        for _listing in _listings:
            if listing_is_product(_listing, product):
                if _results.get(product['product_name']):
                    _results[product['product_name']].append(_listing)
                else:
                    _results[product['product_name']] = [_listing]

    for product_name in _results:
        results.append(
            {'product_name': product_name, 'listings': _results[product_name]}
        )


if __name__ == '__main__':
    read_source()
    find_results()
    with open('results.json', 'w') as results_file:
        json.dump(results, results_file, indent=4)
