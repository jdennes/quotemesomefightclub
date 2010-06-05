#!/usr/bin/env python
import sys, os
import random
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from models import Quote

class MainHandler(webapp.RequestHandler):
  def get_random_quote(self):
    quotes = Quote.all()
    quotes_dict = {}
    i = 0
    for q in quotes:
      quotes_dict[i] = q.quote
      i += 1
    if len(quotes_dict) > 0:
      return quotes_dict[random.randint(0, i - 1)]
    return ''
    
  def get(self):
    path = os.path.join(os.path.dirname(__file__), 'index.html')
    quote = self.get_random_quote()
    vals = { 'quote': quote }
    self.response.out.write(template.render(path, vals))

def main():
  application = webapp.WSGIApplication(
    [('/', MainHandler),], debug=True)
  util.run_wsgi_app(application)

if __name__ == '__main__':
  main()
