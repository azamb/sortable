#!/usr/bin/python
# -*- coding: utf-8 -*-

import json


def find_price_anomalies(results):
    '''Loop through results found by matching.py to find
    product with bad matches based on large price differences
    among the matched listings.

    Params:
        results (list): list of dictionaries containing all matches found.

    Returns:
        suspect_products (list): List of products that may have bad matches.
    '''
    suspect_products = []
    price_delta = 200.0

    for result in results:
        listings = result['listings']
        if len(listings) > 1:
            prices = [
                round(float(listing['price']), 2) for listing in listings
            ]

            prices.sort()
            min_price = prices[0]

            for price in prices[1:]:
                if price - min_price >= price_delta:
                    suspect_products.append(result)
                    break

    return suspect_products


def read_source():
    '''Read source file.

    Returns:
        results (list): list of result dictionaries.
    '''
    with open('results.txt') as results_file:
        return json.load(results_file)

if __name__ == '__main__':
    results = read_source()
    suspects = find_price_anomalies(results)

    with open('tests/suspects.json', 'w') as suspects_file:
        json.dump(suspects, suspects_file, indent=4)
