#!/usr/bin/env python3
"""
File: pynsgr/commands/nsgr_submit.py

Copyright 2023 OSB and other contributors
"""

import os
import sys
import xml.etree.ElementTree as ET

import pynsgr.client as CipresClient
import requests


def nsgr_submit(argv):
    """
    nsgr_submit TEMPLATE_DIRECTORY validate|run [results_directory]

    Where TEMPLATE_DIRECTORY is the name of a directory that contains the job's input data files and
    two property files named testInput.properties and testParam.properties.

    -c
        path to config file

        By default, it looks in the users's home directory (~) for .nsgrest.conf, then for nsgrest.conf (without a dot)

    validate
        Ask's the REST API whether the job is valid.  If valid, prints to stdout, the command line that
        would be run on the execution host if the job were submitted to run.  If invalid, prints an
        error message that explains which fields have errors.

    run
        Submits the job to the REST API, waits for it to complete, and downloads the results to
        a subdirectory of the current directory whose name is the jobhandle (i.e, starts with "NGBW-"))

    [results_directory]
        Absolute or relative path of a directory to which results will be downloaded.  If the directory
        doesn't exist, nsgr_submit will create it. Intermediate directories, however, will not be created.
        If results_directory isn't specified, the default is directory name is ./jobhandle where jobhandle
        is the CIPRES assigned job handle, a long guid, starting with "NGBW-".
    """

    if not argv or len(argv) < 3:
        print(nsgr_submit.__doc__)
        return 1

    # get config file path and remove from list
    try:
        c_path = argv.index("-c")
        argv.pop(c_path)
        conf_filepath = argv[c_path]
        argv.pop(c_path)
    except ValueError:
        conf_filepath = None

    template = argv[1]
    action = argv[2]
    if not os.path.isdir(template):
        print("%s is not a valid TEMPLATE_DIRECTORY" % (template))
        print(nsgr_submit.__doc__)
        return 1
    if action != "validate" and action != "run":
        print("second argument must be either validate or run")
        print(nsgr_submit.__doc__)
        return 1
    resultsdir = None
    if len(argv) > 3:
        resultsdir = argv[3]

    properties = CipresClient.Application(conf_filepath).getProperties()
    client = CipresClient.Client(
        properties.APPNAME,
        properties.APPID,
        properties.USERNAME,
        properties.PASSWORD,
        properties.URL,
    )

    """
        Instead of creating the Client as above, UMBRELLA Applications would supply info about the end user in endUserHeaders, like this.
        You must instantiate a separate client for each end user (it is very lightweight; it's fine to create a new client for each
        request).

        client = CipresClient.Client(properties.APPNAME, properties.APPID, properties.USERNAME, properties.PASSWORD, properties.URL,
            endUserHeaders = {'cipres-eu' : 'terri100', 'cipres-eu-email' : 'terri100@yahoooo.com'} )
    """

    if properties.VERBOSE:
        CipresClient.verbose = True
    try:
        if action == "validate":
            job = client.validateJobTemplate(template)
            job.show()
        else:
            job = client.submitJobTemplate(template)
            job.show(messages="true")
            print("Waiting for job to complete ...")
            job.waitForCompletion()
            if not resultsdir:
                resultsdir = job.jobHandle
            if not os.path.exists(resultsdir):
                os.mkdir(resultsdir)
            print("Downloading results to %s" % (os.path.abspath(resultsdir)))
            job.downloadResults(directory=resultsdir)
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
    sys.exit(nsgr_submit(sys.argv))


if __name__ == "__main__":
    main()
