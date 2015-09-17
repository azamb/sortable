#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

def read_source():
    '''Read source file.

    Returns:
        results (list): list of result dictionaries.
    '''
    with open('results.json') as results_file:
        return json.load(results_file)

def is_anomaly(result):
    pass

def eval_listings(listings):
    for index, listing in enumerate(listings):
        others = list(listings)
        others.pop(index)


def find_anomalies(results):
    for result in results:
        eval_listings(results['listings'])



if __name__ == '__main__':
    results = read_source()
    find_anomalies(results)

    from pudb import set_trace
    set_trace()


