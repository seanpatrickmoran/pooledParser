#! /usr/bin/env python3

import os, subprocess
from multiprocessing import Pool
from multiprocessing import cpu_count
from subprocess import call
from getdir import get


def run_get(pwd_dir):
    feed_dir = ''
    try:
        if os.path.isdir(pwd_dir):
            feed_dir = pwd_dir
            print('passes')
    except FileNotFoundError:
        feed_dir = subprocess.call("pwd {}".format(pwd_dir), shell=True)
        print('fails')
    batchlist = []
    for file in os.listdir(feed_dir):
        if file.startswith("JQ_") and file.endswith("K.txt"):
            batchlist.append("{}/{}".format(feed_dir,file))
    N = cpu_count()
    with Pool(N) as p:
        p.map(get.call_and_write, batchlist)
    chomp = list()
    for X in batchlist:
        chomp.append(''.join([X[:-4],'.OUTPUT.txt']))
    prescript = ' '.join(chomp)
    print("cat {} > {}/JQ_OUT.txt".format(prescript,feed_dir))
    script = "cat {} > {}/JQ_OUT.txt".format(prescript,feed_dir)
    call(script, shell=True)

"""
PATH fixed here


"""