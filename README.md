# pynsgr

[![GitHub CI](https://github.com/OpenSourceBrain/pynsgr/actions/workflows/ci.yml/badge.svg)](https://github.com/OpenSourceBrain/pynsgr/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/pynsgr)](https://pypi.org/project/pynsgr/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pynsgr)](https://pypi.org/project/pynsgr/)
[![GitHub](https://img.shields.io/github/license/OpenSourceBrain/pynsgr)](https://github.com/OpenSourceBrain/pynsgr/blob/master/LICENSE.lesser)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/OpenSourceBrain/pynsgr)](https://github.com/OpenSourceBrain/pynsgr/pulls)
[![GitHub issues](https://img.shields.io/github/issues/OpenSourceBrain/pynsgr)](https://github.com/OpenSourceBrain/pynsgr/issues)

Python interface to the [NeuroScience Gateway REST interface](http://www.nsgportal.org/guide.html), based on the previously developed [pycipres](https://svn2.sdsc.edu/repo/scigap/trunk/rest/python_cipres/).

## Quick start guide

### Creating an account on NSGR

Please head to the [NSGR web portal](https://nsgr.sdsc.edu:8443/restusers/login.action) to create an account.
Documentation there includes the list of [available tools](https://nsgr.sdsc.edu:8443/restusers/docs/tools) and other information.
A [tutorial](http://www.nsgportal.org/qs.html) is available, and so is a [complete user guide](http://www.nsgportal.org/guide.html).

Once you have created an account, you must create a new "application" to be able to use the REST API:

- login, click "Developer" > "Application management"
- click "create new application"
- fill in the form: please use the "DIRECT" authentication type

This will create the application for you and create an application ID for you to use (see below).

### Using this package

1. Install this package directly using `pip`:

```
pip install pynsgr
```

or from source (to get the latest development version, for example):

```
git clone https://github.com/OpenSourceBrain/pynsgr
cd pynsgr
pip install .
```

2. Update `~/nsgrest.conf` with your account and application information:

```
URL=https://nsgr.sdsc.edu:8443/cipresrest/v1
USERNAME=<YOUR_USERNAME>
PASSWORD=<YOUR_PASSWORD>
APPID=<YOUR_APPID>
APPNAME=PY_EXPANSE
```

3. Try listing your jobs

```
nsgr_job -l
```

4. Submit a job

```
nsgr_submit <directory> validate
nsgr_submit <directory> run
```

For more information on what the tools do, use the `-h` option:

````
nsgr_submit -h
nsgr_job -h
````

where `<directory>` contains the zipped code to run, and the two properties files.
See the `example` folder for an example of this and configuration files that are used.
