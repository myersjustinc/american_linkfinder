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
                <title>American LinkFinder</title>
                <meta http-equiv="Content-Type" content="text/html;charset=ISO-8859-1" />
            </head>
            <body>
                <h1>American LinkFinder</h1>
                <form method="POST" enctype="multipart/form-data" action="">
                    <label for="aff">AFF (query) file:</label>
                    <input type="file" name="aff" />
                    <br /><br />
                    <input type="submit" value="Go" />
                </form>
                <p><a href="https://github.com/myersjustinc/american_linkfinder">How's it done?</a></p>
                <p><a href="http://www.google.com/recaptcha/mailhide/d?k=01zfAFGGVwaYMLGrppU_E43w==&c=d49xz4RZfPG6pHMyg6aDy0CWSSRUQwGLfUhrXbJYrnU=">Questions? Suggestions?</a></p>
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
                <p><a href="/">Convert another?</a></p>
                <p><a href="https://github.com/myersjustinc/american_linkfinder">How's it done?</a></p>
                <p><a href="http://www.google.com/recaptcha/mailhide/d?k=01zfAFGGVwaYMLGrppU_E43w==&c=d49xz4RZfPG6pHMyg6aDy0CWSSRUQwGLfUhrXbJYrnU=">Questions? Suggestions?</a></p>
            </body>
        </html>""" % {'url': url}

if __name__ == "__main__":
    app.run()

