#!/usr/bin/env python3
"""
File: pynsgr/commands/nsgr_job.py

Copyright 2023 OSB and other contributors
"""

import getopt
import os
import sys
import xml.etree.ElementTree as ET

import pynsgr.client as CipresClient
import requests


def nsgr_job(argv):
    """
    nsgr_job OPTIONS

    Where OPTIONS are:

    -h
        help
    -c
        path to config file

        By default, it looks in the users's home directory (~) for .nsgrest.conf, then for nsgrest.conf (without a dot)

    -l
        list all the user's jobs

    -j JOBHANDLE
        choose a job to act upon.  If no other action (like download) is selected, shows the job's status.

    -d results_directory
        download job results to specified directory.  Directory (but not intermediate directories) will
        be created if it doesn't exist.

        Use with -j to specify the job.

    -v
        verbose (use with -l to get a verbose job listing)

    -r
        remove a job.  Deletes input and output data and all info about the job.  Cancels
        the job if it's waiting to run or running.

    For example:
        nsgr_job -l
            list the user's jobs
        nsgr_job -j JOBHANDLE
            shows status of the job whose jobhandle is JOBHANDLE
        nsgr_job -j JOBHANDLE -d
            download's results of the job whose jobhandle is JOBHANDLE
        nsgr_job -j JOBHANDLE -r
            cancel and remove the specified job.
    """
    conf_filepath = None
    jobHandle = None
    verbose = False
    action = "status"
    resultsdir = None
    try:
        options, remainder = getopt.getopt(argv[1:], "j:hld:vrc:")
    except getopt.GetoptError as ge:
        print(ge)
        return 1
    for opt, arg in options:
        if opt in ("-j"):
            jobHandle = arg
        elif opt in ("-c"):
            conf_filepath = arg
        elif opt in ("-h"):
            print((nsgr_job.__doc__))
            return 0
        if opt in ("-l"):
            action = "list"
        elif opt in ("-d"):
            action = "download"
            resultsdir = arg
        elif opt in ("-r"):
            action = "remove"
        elif opt in ("-v"):
            verbose = True

    properties = CipresClient.Application(conf_filepath).getProperties()
    client = CipresClient.Client(
        properties.APPNAME,
        properties.APPID,
        properties.USERNAME,
        properties.PASSWORD,
        properties.URL,
    )

    """
        Instead of creating the Client as above, UMBRELLA Applications would supply info about the end user in endUserHeaders,
        as in the example below.  You must instantiate a separate client for each end user (it is very lightweight; it's fine
        to create a new client each time you make a request).

        client = CipresClient.Client(properties.APPNAME, properties.APPID, properties.USERNAME, properties.PASSWORD, properties.URL,
            endUserHeaders = {'cipres-eu' : 'terri100', 'cipres-eu-email' : 'terri100@yahoooo.com'} )
    """

    if properties.VERBOSE:
        print("Setting CipresClient.verbose")
        CipresClient.verbose = True

    if action != "list" and not jobHandle:
        print((nsgr_job.__doc__))
        return 1
    try:
        if action == "list":
            jobs = client.listJobs()
            for job in jobs:
                if verbose:
                    job.show(messages=True)
                else:
                    job.show(messages=False)
            return 0
        if action == "status":
            job = client.getJobStatus(jobHandle)
            job.show(messages=True)
            return 0
        if action == "remove":
            job = client.getJobStatus(jobHandle)
            job.delete()
            return 0
        if action == "download":
            job = client.getJobStatus(jobHandle)
            if not os.path.exists(resultsdir):
                os.mkdir(resultsdir)
            if job.isDone():
                print("Downloading final results to %s" % (os.path.abspath(resultsdir)))
                job.downloadResults(directory=resultsdir, final=True)
            else:
                print(
                    "Job isn't finished. Downloading working dir files to %s"
                    % (os.path.abspath(resultsdir))
                )
                job.downloadResults(directory=resultsdir, final=False)
            return 0
        print((nsgr_job.__doc__))
        return 1
    except CipresClient.ValidationError as ve:
        print(ve.asString())
        return 2
    except CipresClient.CipresError as ce:
        print("CIPRES ERROR: %s" % (ce))
        return 2
    except requests.exceptions.RequestException as e:
        print("CONNECTION ERROR: %s" % (e))
        return 2
    except ET.ParseError as pe:
        print("Unexpected response cannot be parsed.  Parsing error message: %s" % (pe))
        return 2
    return 0


# required because console scripts cannot take argument lists
def main():
    """Main runner"""
    sys.exit(nsgr_job(sys.argv))


if __name__ == "__main__":
    main()
