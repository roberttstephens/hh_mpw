Determine the miles per week for a hal higdon program.

I don't anticipate this to be reusable, but it can serve as an example of some common python practices/language features.

 - Argparse
 - Using the requests library
 - Parse html with lxml
 - Using setup.py
 - Regex
 - List comprehensions
 - Slices

## Requirements
This requires python3 and will _NOT_ run under python 2.

## Installation instructions

    pip install git+https://github.com/roberttstephens/hh_mpw.git


## Usage

    usage: hh_mpw [-h] [-p PACE] url
    
    Determine the miles per week for a hal higdon program.
    
    positional arguments:
      url                   The url to check
    
    optional arguments:
      -h, --help            show this help message and exit
      -p PACE, --pace PACE  Your average pace in minutes per mile

## Examples

    hh_mpw 'http://www.halhigdon.com/training/51131/Half-Marathon-Novice-1-Training-Program'
    hh_mpw 'http://www.halhigdon.com/training/51131/Half-Marathon-Novice-1-Training-Program' -p 8
