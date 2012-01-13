AFF saved query converter
=========================

This converter takes a saved query file from American FactFinder and generates
a deep link URL corresponding to that query.

There are two versions of the converter:

* One is a small Web application using the web.py framework.
* The other is a command-line Python script.

Command-line script
-------------------

The command-line script (convert_aff.py) just takes the filename of a .aff 
query file as its sole argument and prints a URL to standard output.

Web application
---------------

The Web application (deep_link.py) takes a POST-ed .aff query file and outputs
a page with the corresponding URL in a link.

It also includes a basic requirements.txt (i.e., pip freeze) file and a
configuration file for [ep.io](http://ep.io/) hosting (epio.ini).

Questions?
----------

Email: justin at justinmyers dot net
