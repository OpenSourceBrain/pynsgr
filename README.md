# pynsgr

[![GitHub CI](https://github.com/OpenSourceBrain/pynsgr/actions/workflows/ci.yml/badge.svg)](https://github.com/OpenSourceBrain/pynsgr/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/pynsgr)](https://pypi.org/project/pynsgr/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pynsgr)](https://pypi.org/project/pynsgr/)
[![GitHub](https://img.shields.io/github/license/OpenSourceBrain/pynsgr)](https://github.com/OpenSourceBrain/pynsgr/blob/master/LICENSE.lesser)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/OpenSourceBrain/pynsgr)](https://github.com/OpenSourceBrain/pynsgr/pulls)
[![GitHub issues](https://img.shields.io/github/issues/OpenSourceBrain/pynsgr)](https://github.com/OpenSourceBrain/pynsgr/issues)

Python interface to the [NeuroScience Gateway REST interface](http://www.nsgportal.org/guide.html), based on the previously developed [pycipres](https://svn2.sdsc.edu/repo/scigap/trunk/rest/python_cipres/).

## Quick start guide

1. Install this package locally

```
pip install pynsgr
```


or from source:

```
git clone https://github.com/OpenSourceBrain/pynsgr
cd pynsgr
pip install .
```

2. Sign in and register for an NSG account [here](https://www.nsgportal.org/gest/reg.php).

3. Update `~/nsgrest.conf` with:

```
URL=https://nsgr.sdsc.edu:8443/cipresrest/v1
USERNAME=<YOUR_USERNAME>
PASSWORD=<YOUR_PASSWORD>
APPID=<YOUR_APPID>
APPNAME=PY_EXPANSE
```

4. Try listing your jobs

```
 nsgr_job -l
```
