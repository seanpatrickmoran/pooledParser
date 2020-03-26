#! /usr/bin/env python3

import os
from multiprocessing import Pool
from multiprocessing import cpu_count
from subprocess import call
from getdir import get


def run_get(pwd_dir):
    batchlist = []
    for file in os.listdir(pwd_dir):
        if file.startswith("JQ_") and file.endswith("K.txt"):
            batchlist.append(file)
    N = cpu_count()
    with Pool(N) as p:
        p.map(get.call_and_write, batchlist)


    chomp = list()
    for X in batchlist:
        chomp.append(''.join([X[:-4],'.OUTPUT.txt']))
    prescript = ' '.join(chomp)
    print("cat {} > JQ_OUT.txt".format(prescript))
    script = "cat {} > JQ_OUT.txt".format(prescript)
    call(script, shell=True)
