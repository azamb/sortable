# Matching products and listings.

Hi! this is my solution to sortable's coding challenge: http://sortable.com/challenge/

# To run this solution (python 2.7):

1. git clone git@github.com:chuo06/sortable.git
2. python matching.py

# Notes:
1. In an effort to increase precision, listings are indexed by manufacturer.
Therefore, products and listings must have a matching manufacturer in order
to be considered a potential match.

2. In a effort to detect incorrect matches, I have also implemented a simple
anomaly detection script that compares price differences among the matches
found for particular product.

3. Some flaws: matching algorithm is very simple and can use some work
to increase recall.
