#!/usr/bin/env python
import cgi
from convert_aff import convert_aff
import web

cgi.maxlen = 1048576 * 1  # no files more than 1 MB

urls = (
    r'/', 'upload',
)
app = web.application(urls, globals())
app.internalerror = web.debugerror
application = app.wsgifunc()

class upload:
    def GET(self):
        return """<!DOCTYPE html>
        <html>
            <head>
                <title>Census bookmark generator</title>
                <meta http-equiv="Content-Type" content="text/html;charset=ISO-8859-1" />
            </head>
            <body>
                <form method="POST" enctype="multipart/form-data" action="">
                    <label for="aff">AFF (query) file:</label>
                    <input type="file" name="aff" />
                    <br /><br />
                    <input type="submit" value="Go" />
                </form>
            </body>
        </html>"""
    
    def POST(self):
        try:
            data = web.input(aff={})
        except ValueError:
            return "File too large"
        
        url = convert_aff(data['aff'].file)
        
        return """<!DOCTYPE html>
        <html>
            <head>
                <title>Census bookmark generator</title>
                <meta http-equiv="Content-Type" content="text/html;charset=ISO-8859-1" />
            </head>
            <body>
                <p>Here's your link: <a href="%(url)s">%(url)s</a></p>
                <p><a href="/">Again?</a></p>
            </body>
        </html>""" % {'url': url}

if __name__ == "__main__":
    app.run()

