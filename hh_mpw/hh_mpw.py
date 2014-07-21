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

def calculate_miles(string, pace):
    """
    Given '30 min tempo', and 10 (minutes per miles) return the miles.

    The math is set up like so

    10 minutes/1 mile = 30 minutes/d miles
    10d = 30
    d = 3
    """
    pattern = re.compile(r'^(\d+\.?(\d+)?) min tempo')
    match = pattern.match(string)
    if match:
        return float(match.groups()[0]) / pace
    return 0.0

def determine_miles(string, pace):
    """
    Get the number of miles in a string.
    """
    return parse_miles(string) or calculate_miles(string, pace)

def parse_miles(string):
    """
    Given '3 m run' return 3
    """
    pattern = re.compile(r'^(\d+\.?(\d+)?) m[^in]')
    match = pattern.match(string)
    if match:
        return float(match.groups()[0])
    return 0.0


def hh_mpw(url, pace):
    """
    Get the miles per week for a hal higdon program in a list format.
    """
    mpw = dict()
    r = requests.get(url)
    tree = lxml.html.fromstring(r.content)
    row_sel = CSSSelector("table.table-training tr")
    column_sel = CSSSelector('td')
    rows = row_sel(tree)
    # The first row just lists the days of the week.
    for row in rows[1::]:
        columns = column_sel(row)
        # The first column is the week number.
        week_miles = sum(list([determine_miles(c.text_content(), pace) for c in columns[1:]]))
        mpw[int(columns[0].text_content())] = week_miles
    return mpw

def main():
    """
    Determine the miles per week for a hal higdon program.
    """
    parser = argparse.ArgumentParser(
        description='Determine the miles per week for a hal higdon program.'
    )
    parser.add_argument('url', help='The url to check')
    parser.add_argument(
        '-p',
        '--pace',
        help='Your average pace in minutes per mile.',
        default=10.0,
        type=float,
    )
    args = parser.parse_args()

    mpw = hh_mpw(args.url, args.pace)
    if mpw:
        for key, value in mpw.items():
            print(key, value, sep='\t')
    else:
        print('No results. Are you sure you used a hal higdon url?')


if __name__ == '__main__':
    main()
