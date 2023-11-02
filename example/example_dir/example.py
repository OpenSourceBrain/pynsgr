"""
Example python script to run on NSGR

File: example.py

Copyright 2023 OSB contributors
"""


from netpyne import specs
from netpyne import sim
from netpyne import __version__ as version

import sys
import pkg_resources

if __name__ == "__main__":
    print("Running example script to list Python packages...")

    with open("output.txt", "w") as f:
        print(f"Python version is: {sys.version}", file=f)
        print("Installed packages on NSG:", file=f)
        dists = [str(d).replace(" ", "==") for d in pkg_resources.working_set]
        for i in dists:
            print(i, file=f)

    for k in sys.modules.keys():
        if "matplotlib" in k:
            print(f"matplotlib still loaded: {k}")

    print(f"Args are: {sys.argv}")
    if sys.argv.count("-nogui") > 0:
        print("nogui found")
    print("Done!")
