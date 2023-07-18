# pynsgr

Python interface to the [NeuroScience Gateway REST interface](http://www.nsgportal.org/guide.html), based on the previously developed [pycipres](https://svn2.sdsc.edu/repo/scigap/trunk/rest/python_cipres/).

## Quick start guide

1. Install this package locally

```
git clone https://github.com/OpenSourceBrain/pynsgr
cd pynsgr
pip install .
```

2. Sign in and register for an NSG account [here](https://www.nsgportal.org/gest/reg.php).

1. Update ~/nsgrest.conf with:

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
