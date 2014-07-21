#!/usr/bin/env python3
"""
Determine the miles per week for a hal higdon program.
"""
import argparse
import lxml
from lxml import html
from lxml.cssselect import CSSSelector
import re
import requests

def get_miles(string):
    """
    Get the number of miles in a string.
    """
    # Matches '1 m'
    pattern = re.compile(r'^(\d+\.?(\d+)?) m[^in]')
    match = pattern.match(string)
    if match:
        return match.groups()[0]

def hh_mpw(url):
    """
    Get the miles per week for a hal higdon program in a list format.
    """
    mpw = list()
    r = requests.get(url)
    tree = lxml.html.fromstring(r.content)
    row_sel = CSSSelector("table.table-training tr")
    column_sel = CSSSelector('td')
    rows = row_sel(tree)
    # The first row just lists the days of the week.
    for row in rows[1::]:
        columns = column_sel(row)
        # The first column is the week number.
        week_miles = sum(list(map(float, list(filter(None, [get_miles(c.text_content()) for c in columns[1:]])))))
        mpw[columns[0].text_content()] = week_miles
    return mpw

def main():
    """
    Determine the miles per week for a hal higdon program.
    """
    parser = argparse.ArgumentParser(
        description='Determine the miles per week for a hal higdon program.'
    )
    parser.add_argument('url', help='The url to check')
    args = parser.parse_args()

    mpw = hh_mpw(args.url)
    if mpw:
        for key, value in mpw:
            print(key, value, sep='\t')


if __name__ == '__main__':
    main()
