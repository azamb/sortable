#!/usr/bin/python
# -*- coding: utf-8 -*-

# product_name = $manufacturer_$family_$model
# Some have family, some don't
# Some listings don't have a brand
# Some product brands not in listings i.e: Contax

# Maybe create index of listings by brand and cluster listings with same brands and similar titles

# First pass - > check if manufacturers match
import json
# import codecs

def read_source():
    '''
    TODO write docstring
    '''
    products = []
    listings = {}

    with open('products.txt') as products_file:
    # with codecs.open('products.txt', encoding='ascii') as products_file:
        for product in products_file:
            products.append(json.loads(product))

    with open('listings.txt') as listings_file:
    # with codecs.open('listings.txt', encoding='utf-8') as listings_file:
        for listing in listings_file:
            listing_dict = json.loads(listing)
            manufacturer = listing_dict.get('manufacturer', 'brandless').lower()
            if manufacturer in listings:
                listings[manufacturer].append(listing_dict)
            else:
                listings[manufacturer] = [listing_dict]

    from pudb import set_trace
    set_trace()
    return products, listings

def listing_is_product(listing, product):
    '''
    TODO write docstring
    '''
    try:
        if listing['manufacturer']:
             if listing['manufacturer'].lower() != product['manufacturer'].lower():
                return False
             # manufacturers match
             #
             model, family = product['model'].lower(), product['family'].lower()
             listing_title = listings['title'].lower()
             if model in listing_title and family in listing_title:
                return True
             return False
        else:
            # no_manufacturer algo
            print('This listing has no manufacturer information.')
    except:
        from pudb import set_trace
        set_trace()


if __name__ == '__main__':
    products, listings = read_source()


    from pudb import set_trace
    set_trace()
