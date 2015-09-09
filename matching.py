# product_name = $manufacturer_$family_$model
# Some have family, some don't
# Some listings don't have a brand
# Some product brands not in listings i.e: Contax

# Maybe create index of listings by brand and cluster listings with same brands and similar titles

# First pass - > check if manufacturers match
import json

def read_source():
    '''
    Reads txt source files and returns lists of products and listings
    '''
    products = []
    listings = []
    with open('products.txt') as products_file:
        for product in products_file:
            # TODO lowercase each value in product dict
            # prod = json.loads(product)
            # prod
            products.append(json.loads(product))

    with open('listings.txt') as listings_file:
        for listing in listings_file:
            listings.append(json.loads(listing))

    return products, listings

def listing_is_product(listing, product):
    '''
    Returns True if listing and product match. False otherwise.
    '''
    if listing['manufacturer']:
         if listing['manufacturer'].lower() != product['manufacturer'].lower():
            return False
        # brands match


    else:
        # no_manufacturer algo
        pass







if __name__ == '__main__':
    products, listings = read_source()


    from pudb import set_trace
    set_trace()
