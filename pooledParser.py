#! /usr/bin/env python3

import subprocess
import argparse
from getdir import dMass_Call
from scrapedir import scrape


def pooledParser():
    argue = argparse.ArgumentParser()
    argue.add_argument("--command",dest="command", choices=("scrape","chomp","get"), default="instruct",
                       help="command to pass: scrape, get, chomp")
    argue.add_argument("--i",dest="input_arg")
    args = argue.parse_args()
    if args.command == 'scrape':
        scrape.scrape(args.input_arg)
    elif args.command == 'chomp':
        subprocess.call("./chomp/JQ_SCRIPT.sh {}".format(args.input_arg),shell=True)
    elif args.command == 'get':
        dMass_Call.run_get(args.input_arg)
    else:
        print('args.')


pooledParser()
