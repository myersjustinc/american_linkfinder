American LinkFinder
===================

This converter takes a saved query file from the U.S. Census Bureau's American
FactFinder and generates a deep link URL corresponding to that query.

There are two versions of the converter:

* One is a small Web application using the web.py framework.
* The other is a command-line Python script.

Command-line script
-------------------

The command-line script (convert_aff.py) just takes the filename of a .aff 
query file as its sole argument and prints a URL to standard output.

Usage: `./convert_aff.py <foo.aff>`

Web application
---------------

The Web application (deep_link.py) takes a POST-ed .aff query file and outputs
a page with the corresponding URL in a link.

It also includes a basic requirements.txt (i.e., pip freeze) file and
configuration files for [Heroku](http://www.heroku.com/) hosting.

If you have the [web.py](http://webpy.org/) framework installed, you can run 
this application locally: `./deep_link.py` should print a local URL you can 
use to access it in your Web browser of choice.

Hosted version
--------------

Of course, if you'd rather not fiddle with any of those, there's a version 
up at [link-aff.herokuapp.com](http://link-aff.herokuapp.com/).

Questions?
----------

Email: justin at justinmyers dot net

Revision history
----------------

April 18, 2012:

* Switched from ep.io to Heroku (including provided configuration files) due to
  ep.io closing up shop

Feb. 25, 2012:

* Updated documentation with a bit more usage information

Jan. 13, 2012: 

* Added support for product IDs with cat-group-spec-id attributes
* Moved conversion code into one module instead of duplicating it in 
  command-line and web.py versions
* Moved from Gist to proper GitHub repo
