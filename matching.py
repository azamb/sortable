#!/usr/bin/python
# -*- coding: utf-8 -*-

# product_name = $manufacturer_$family_$model
# Some have family, some don't
# Some listings don't have a brand
# Some product brands not in listings i.e: Contax

# TODO stem/strip model numbers from dashes and other symbols

import json
####################
# Data Structures
####################
products = []
listings = {}
results = {}

def read_source():
    '''
    TODO write docstring
    '''
    with open('products.txt') as products_file:
        for product in products_file:
            products.append(json.loads(product))

    with open('listings.txt') as listings_file:
        for listing in listings_file:
            listing_dict = json.loads(listing)
            manufacturer = listing_dict['manufacturer'].lower() or u'brandless'

            if manufacturer in listings:
                listings[manufacturer].append(listing_dict)
            else:
                listings[manufacturer] = [listing_dict]

    return products, listings

def listing_is_product(listing, product):
    '''
    TODO write docstring
    '''
    title = listing['title'].lower()
    family = product.get('family', '').lower()
    model = product['model'].lower()

    if model in title:
        if family and family in title:
            return True
    return False

def find_results():
    '''
    TODO Write docstring
    '''
    for product in products:
        _listings = listings.get(product['manufacturer'].lower(), [])
        for _listing in _listings:
            if listing_is_product(_listing, product):
                if results.get(product['product_name']):
                    results[product['product_name']].append(_listing)
                else:
                    results[product['product_name']] = [_listing]

# def write_results():
#     with open('results.json') as results_file:


if __name__ == '__main__':
    read_source()
    find_results()
    # write_results()

    # from pudb import set_trace
    # set_trace()
