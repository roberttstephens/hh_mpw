Determine the miles per week for a hal higdon program.

I don't anticipate this to be reusable, but it can serve as an example of some common python practices.

 - Argparse
 - Using the requests library
 - Parse html with lxml
 - Using setup.py
 - Regex

## Installation instructions

    pip install git+https://github.com/roberttstephens/hh_mpw.git


## Usage

    usage: hh_mpw [-h] url
    
    Determine the miles per week for a hal higdon program.
    
    positional arguments:
      url         The url to check
    
    optional arguments:
      -h, --help  show this help message and exit

## Example

    hh_mpw 'http://www.halhigdon.com/training/51131/Half-Marathon-Novice-1-Training-Program'
