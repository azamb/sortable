#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

# List of products that may have bad matches.
suspect_products = []


def find_price_anomalies(results, price_gap):
    '''
        TODO docstring
    '''
    for result in results:
        listings = result['listings']
        prices = [
            round(float(listing['price']), 2) for listing in listings
        ]
        prices.sort()
        buckets = [[prices[0]]]

        for price in prices[1:]:
            if abs(price - buckets[-1][-1]) <= price_gap:
                buckets[-1].append(price)
            else:
                buckets.append([price])

        if len(buckets) > 2:
            suspect_products.append(result)


def read_source():
    '''Read source file.

    Returns:
        results (list): list of result dictionaries.
    '''
    with open('results.json') as results_file:
        return json.load(results_file)


if __name__ == '__main__':
    results = read_source()
    find_price_anomalies(results, 200.00)

    with open('suspects.json', 'w') as suspects_file:
        json.dump(suspect_products, suspects_file, indent=4)
