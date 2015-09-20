#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import codecs


def listing_is_product(listing, product):
    '''Simple Matching Algorithm.

    Params:
        listing (dict): listing from listings.txt
        product (dict): product from products.txt

    Returns:
        bool: True if family and model are in title, False otherwise.
    '''
    def clean(input):
        return input.lower().replace('-', '')

    title = clean(listing['title'])
    family = clean(product.get('family', ''))
    model = clean(product['model'])

    if model in title:
        if family and family in title:
            return True
    return False


def get_results(products, listings):
    '''Loop through products and listings to find matches.

    Params:
        products (list): list of product dictionaries read from products.txt
        listings (dict): listings dictionary indexed by manufacturer

    Returns:
        results (list): list of dictionaries containing all matches found.
    '''
    matches = {}
    results = []

    for product in products:
        _listings = listings.get(product['manufacturer'].lower(), [])
        for listing in _listings:
            if listing_is_product(listing, product):
                if matches.get(product['product_name']):
                    matches[product['product_name']].append(listing)
                else:
                    matches[product['product_name']] = [listing]

    for product_name in matches:
        results.append(
            {'product_name': product_name, 'listings': matches[product_name]}
        )

    return results


def read_source():
    '''Read source files.

    Returns:
        products (list): list of product dictionaries.
        listings (dict): listings dictionary indexed by manufacturer.
    '''
    products = []
    listings = {}

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

if __name__ == '__main__':
    products, listings = read_source()
    results = get_results(products, listings)
    with open('results.txt', 'w') as results_file:
        json.dump(results, results_file, indent=4)
