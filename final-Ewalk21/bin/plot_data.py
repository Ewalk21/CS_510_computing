#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import sys
import cmath

def main(local_argv):
#    try:
        filename = local_argv[1]
        df = pd.read_csv(filename,usecols=[2])
        name = filename.replace("csv","png")
        plt.figure(figsize=(12, 12))
        plt.imshow(df, cmap=plt.cm.jet)   #colormap = inferno,magma,plasma,viridis,gist_rainbow
        plt.colorbar()
        plt.xticks(())
        plt.yticks(())
        plt.savefig(name)

#    except Exception:
#        print("invalid input, input must a CSV file")


if __name__ == "__main__":
    main(sys.argv)