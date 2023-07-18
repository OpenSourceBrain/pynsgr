from setuptools import setup

setup(name='pynsgr',

    version='0.9.5',

    description='Neuroscience Gateway REST API Client - based on CIPRES REST API Client',

    long_description = open('README.md').read(),

    long_description_content_type="text/markdown",

    url='https://github.com/OpenSourceBrain/pynsgr',

    author='Terri Schwartz, Padraig Gleeson',

    author_email='terri@sdsc.edu',

    license='MIT',

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',

    ],

    keywords='NSGR xsede',


    install_requires=[
        "requests >= 2.5.3",
    ],

    scripts=[
        "bin/nsgr_submit",
        "bin/nsgr_job",
    ],

    packages=['pynsgr'],

    # It seems that with "setup.py sdist", MANIFEST.in controls which extra files are
    # put into the sdist archive.  However those extra files won't be installed to user's
    # system unless we have include_package_data=True here.
    include_package_data=True,

    zip_safe=False)
