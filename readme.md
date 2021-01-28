# MVC Example
[![Build Status](https://travis-ci.org/pairing4good/mvc-python.svg?branch=main)](https://travis-ci.org/pairing4good/mvc-python)

This is a bare-bones MVC example.  The intent is to avoid web frameworks 
like [Django](https://www.djangoproject.com/).  While these type of frameworks remove the 
need to reinvent the wheel, they often hide the details of how they actually work.  This 
example is test driven through `test/MvcAcceptanceTest.py`.  This test class starts and 
stops a bare-bones `HTTPServer` on port `8080`.  

## Request Handler
The `handler/RequestHandler.py` is a `BaseHTTPRequestHandler` that processes 
[HTTP Request Methods](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods). 
The `routes` dictionary matches url [paths](https://en.wikipedia.org/wiki/URL#Syntax) 
to `controller/Controller.py` functions. 