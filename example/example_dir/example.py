"""
Example python script to run on NSGR

File: example.py

Copyright 2023 OSB contributors
"""


import sys
import pkg_resources

with open("output.txt", "w") as f:
    print(f"Python version: {sys.version}", file=f)
    print("Installed packages:", file=f)
    dists = [str(d).replace(" ", "==") for d in pkg_resources.working_set]
    for i in dists:
        print(i, file=f)
